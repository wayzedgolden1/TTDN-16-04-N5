# -*- coding: utf-8 -*-
from odoo import fields, models


class MtdnAssetCategory(models.Model):
    _name = "mtdn.asset.category"
    _description = "MTDN Asset Category"
    _order = "name"

    name = fields.Char(string="Tên loại tài sản", required=True, index=True)
    code = fields.Char(string="Mã loại", required=True, index=True, copy=False)
    active = fields.Boolean(default=True)
    description = fields.Text(string="Mô tả")

    _sql_constraints = [
        ("mtdn_asset_category_code_uniq", "unique(code)", "Mã loại tài sản phải là duy nhất."),
    ]
