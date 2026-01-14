# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MtdnMeetingBooking(models.Model):
    _name = "mtdn.meeting.booking"
    _description = "MTDN Meeting Booking"
    _order = "start_datetime desc"

    name = fields.Char(string="Tiêu đề", required=True, index=True)

    room_id = fields.Many2one(
        "mtdn.meeting.room",
        string="Phòng họp",
        required=True,
        ondelete="restrict",
        index=True,
    )

    start_datetime = fields.Datetime(string="Bắt đầu", required=True, default=fields.Datetime.now)
    end_datetime = fields.Datetime(
        string="Kết thúc",
        required=True,
        default=lambda self: fields.Datetime.now() + relativedelta(hours=1),
    )

    host_id = fields.Many2one(
        "mtdn.employee",
        string="Chủ trì (Host)",
        required=True,
        ondelete="restrict",
        default=lambda self: self._default_host_employee(),
        index=True,
    )

    participant_ids = fields.Many2many(
        "mtdn.employee",
        "mtdn_meeting_booking_employee_rel",
        "booking_id",
        "employee_id",
        string="Thành phần tham gia",
    )

    equipment_ids = fields.Many2many(
        "mtdn.asset",
        "mtdn_meeting_booking_asset_rel",
        "booking_id",
        "asset_id",
        string="Thiết bị sử dụng",
        domain="[('state','!=','broken')]",
        help="Thiết bị bổ sung (có thể trùng với thiết bị của phòng).",
    )

    state = fields.Selection(
        selection=[
            ("draft", "Nháp"),
            ("confirmed", "Xác nhận"),
            ("cancelled", "Hủy"),
        ],
        string="Trạng thái",
        required=True,
        default="draft",
        index=True,
    )

    note = fields.Text(string="Ghi chú")
    company_id = fields.Many2one(related="room_id.company_id", store=True, readonly=True)

    # ------------------------------------------------------------
    # Defaults
    # ------------------------------------------------------------
    @api.model
    def _default_host_employee(self):
        emp = self.env["mtdn.employee"].search([("user_id", "=", self.env.user.id)], limit=1)
        return emp.id if emp else False

    # ------------------------------------------------------------
    # Actions (buttons)
    # ------------------------------------------------------------
    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_cancel(self):
        self.write({"state": "cancelled"})

    def action_set_draft(self):
        self.write({"state": "draft"})

    # ------------------------------------------------------------
    # Constraints
    # ------------------------------------------------------------
    @api.constrains("start_datetime", "end_datetime")
    def _check_time_range(self):
        for rec in self:
            if rec.start_datetime and rec.end_datetime and rec.end_datetime <= rec.start_datetime:
                raise ValidationError("Thời gian kết thúc phải lớn hơn thời gian bắt đầu.")

    @api.constrains("room_id", "start_datetime", "end_datetime", "state")
    def _check_overlapping_booking(self):
        for rec in self:
            if not rec.room_id or not rec.start_datetime or not rec.end_datetime:
                continue
            if rec.state == "cancelled":
                continue

            domain = [
                ("id", "!=", rec.id),
                ("room_id", "=", rec.room_id.id),
                ("state", "!=", "cancelled"),
                ("start_datetime", "<", rec.end_datetime),
                ("end_datetime", ">", rec.start_datetime),
            ]
            if self.search_count(domain):
                raise ValidationError(
                    "Phòng họp đã có lịch trùng trong khoảng thời gian này. "
                    "Vui lòng chọn phòng khác hoặc đổi thời gian."
                )

    # ------------------------------------------------------------
    # Onchange helpers
    # ------------------------------------------------------------
    @api.onchange("room_id")
    def _onchange_room_id(self):
        for rec in self:
            if rec.room_id and not rec.equipment_ids:
                rec.equipment_ids = rec.room_id.equipment_ids

    @api.onchange("start_datetime", "end_datetime")
    def _onchange_time_domain_room(self):
        for rec in self:
            if not rec.start_datetime or not rec.end_datetime:
                continue

            if rec.end_datetime <= rec.start_datetime:
                return {
                    "warning": {
                        "title": "Thời gian không hợp lệ",
                        "message": "Giờ kết thúc phải lớn hơn giờ bắt đầu.",
                    }
                }

            domain = [
                ("state", "!=", "cancelled"),
                ("start_datetime", "<", rec.end_datetime),
                ("end_datetime", ">", rec.start_datetime),
            ]
            if rec.id:
                domain.append(("id", "!=", rec.id))

            busy_room_ids = self.env["mtdn.meeting.booking"].search(domain).mapped("room_id").ids
            return {
                "domain": {
                    "room_id": [("id", "not in", busy_room_ids), ("state", "=", "available")]
                }
            }
