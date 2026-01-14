# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MtdnAsset(models.Model):
    _name = "mtdn.asset"
    _description = "MTDN Asset"
    _order = "code, name"

    code = fields.Char(string="Mã tài sản", required=True, copy=False, default="New", index=True)
    name = fields.Char(string="Tên tài sản", required=True, index=True)

    category_id = fields.Many2one(
        "mtdn.asset.category",
        string="Loại tài sản",
        ondelete="restrict",
        required=True,
        index=True,
    )

    company_id = fields.Many2one(
        "res.company",
        string="Công ty",
        default=lambda self: self.env.company,
        required=True,
        index=True,
    )

    purchase_date = fields.Date(string="Ngày mua")
    in_service_date = fields.Date(string="Ngày đưa vào sử dụng")

    currency_id = fields.Many2one(
        "res.currency",
        string="Tiền tệ",
        default=lambda self: self.env.company.currency_id,
        required=True,
    )
    value = fields.Monetary(string="Giá trị", currency_field="currency_id")

    state = fields.Selection(
        selection=[
            ("available", "Sẵn sàng"),
            ("in_use", "Đang sử dụng"),
            ("maintenance", "Bảo trì"),
            ("broken", "Hỏng"),
        ],
        string="Trạng thái",
        required=True,
        default="available",
        index=True,
    )

    # Assignment (link directly to custom HR models)
    employee_id = fields.Many2one(
        "mtdn.employee",
        string="Gán cho nhân viên",
        ondelete="set null",
        index=True,
    )
    department_id = fields.Many2one(
        "mtdn.department",
        string="Gán cho phòng ban",
        ondelete="set null",
        index=True,
    )

    active = fields.Boolean(default=True)
    note = fields.Text(string="Ghi chú")

    _sql_constraints = [
        ("mtdn_asset_code_uniq", "unique(code)", "Mã tài sản phải là duy nhất."),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("code") or vals.get("code") == "New":
                vals["code"] = self.env["ir.sequence"].next_by_code("mtdn.asset") or "New"
        return super().create(vals_list)

    @api.constrains("employee_id", "department_id")
    def _check_single_assignment(self):
        for rec in self:
            if rec.employee_id and rec.department_id:
                raise ValidationError("Một tài sản chỉ được gán cho Nhân viên hoặc Phòng ban (không được chọn cả hai).")

    @api.constrains("state", "employee_id", "department_id")
    def _check_assignment_when_in_use(self):
        for rec in self:
            if rec.state == "in_use" and not (rec.employee_id or rec.department_id):
                raise ValidationError("Tài sản ở trạng thái 'Đang sử dụng' phải được gán cho Nhân viên hoặc Phòng ban.")
