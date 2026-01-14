# -*- coding: utf-8 -*-
from odoo import fields, models


class MtdnMeetingRoom(models.Model):
    _name = "mtdn.meeting.room"
    _description = "MTDN Meeting Room"
    _order = "code, name"

    code = fields.Char(string="Mã phòng", required=True, copy=False, index=True)
    name = fields.Char(string="Tên phòng", required=True, index=True)

    location = fields.Char(string="Vị trí", help="VD: Tầng 3 - Khu A")
    capacity = fields.Integer(string="Sức chứa", default=6)

    state = fields.Selection(
        selection=[
            ("available", "Sẵn sàng"),
            ("maintenance", "Bảo trì"),
        ],
        string="Trạng thái",
        required=True,
        default="available",
        index=True,
    )

    company_id = fields.Many2one(
        "res.company",
        string="Công ty",
        default=lambda self: self.env.company,
        required=True,
        index=True,
    )

    equipment_ids = fields.Many2many(
        "mtdn.asset",
        "mtdn_meeting_room_asset_rel",
        "room_id",
        "asset_id",
        string="Thiết bị trong phòng",
        domain="[('state','!=','broken')]",
        help="Liên kết trực tiếp với module Tài sản (mtdn.asset).",
    )

    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("mtdn_meeting_room_code_uniq", "unique(code)", "Mã phòng họp phải là duy nhất."),
    ]
