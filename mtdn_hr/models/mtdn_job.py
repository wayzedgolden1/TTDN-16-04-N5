# -*- coding: utf-8 -*-
from odoo import fields, models


class MtdnJob(models.Model):
    _name = "mtdn.job"
    _description = "MTDN Job Position"
    _order = "name"

    name = fields.Char(string="Tên chức danh", required=True, index=True)
    code = fields.Char(string="Mã chức danh", required=True, index=True, copy=False)
    active = fields.Boolean(default=True)
    description = fields.Text(string="Mô tả")

    _sql_constraints = [
        ("mtdn_job_code_uniq", "unique(code)", "Mã chức danh phải là duy nhất."),
    ]
