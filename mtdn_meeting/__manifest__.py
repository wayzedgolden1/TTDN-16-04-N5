# -*- coding: utf-8 -*-
{
    "name": "MTDN - Phòng họp (Meeting Room Booking)",
    "version": "19.0.1.0.0",
    "summary": "Quản lý phòng họp & đặt lịch, liên kết nhân sự (mtdn.employee) và tài sản (mtdn.asset).",
    "category": "MTDN",
    "author": "MTDN",
    "license": "LGPL-3",
    "depends": ["base", "web", "mtdn_hr", "mtdn_asset"],
    "data": [
        "security/ir.model.access.csv",
        "views/mtdn_meeting_room_views.xml",
        "views/mtdn_meeting_booking_views.xml",
        "views/mtdn_meeting_actions.xml",
        "views/mtdn_meeting_menus.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
    "installable": True,
}
