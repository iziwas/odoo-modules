{
    "name": "save_discard_buttons_form",
    "summary": """ Override Save / Discard buttons aesthetics in forms """,
    "website": "https://couriat.info",
    "licence": "AGPL-3",
    "category": "Extra Tools",
    "version": "17.0.0.0",
    "depends": [
        "web"
    ],
    "assets": {
        "web.assets_backend": [
            "save_discard_buttons_form/static/src/views/**/*",
            "save_discard_buttons_form/static/src/scss/*"
        ]
    },
    "installable": True,
    "application": True,
}