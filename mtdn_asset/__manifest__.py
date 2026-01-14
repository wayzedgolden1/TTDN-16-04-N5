# -*- coding: utf-8 -*-
{
    "name": "MTDN - Tài sản (Custom Asset)",
    "version": "19.0.1.0.0",
    "summary": "Quản lý tài sản tự tạo, liên kết trực tiếp với nhân sự (mtdn.employee / mtdn.department).",
    "category": "MTDN",
    "author": "MTDN",
    "license": "LGPL-3",
    "depends": ["base", "web", "mtdn_hr"],
    "data": [
        "security/ir.model.access.csv",
        "data/sequences.xml",
        "views/mtdn_asset_category_views.xml",
        "views/mtdn_asset_views.xml",
        "views/mtdn_asset_actions.xml",
        "views/mtdn_asset_menus.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
    "installable": True,
}
