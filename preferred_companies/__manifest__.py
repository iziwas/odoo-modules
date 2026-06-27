{
    "name": "User Company Preferences",
    "version": "17.0.1.2.0",
    "category": "Technical",
    "summary": "Restore the user's preferred companies automatically on login",
    "description": """
User Company Preferences
========================

Allow users to define a set of preferred companies that are automatically
activated each time they log in, without having to reselect them manually
after each session.

Features
--------

* Users choose their preferred companies from their list of allowed companies
* Preferred companies are automatically activated on login (when no active
  session is detected)
* The user's default company is always placed first so it appears as the
  primary company in the interface
* Preferred companies are automatically cleaned up when company access is
  revoked by an administrator
* Server-side validation prevents selecting companies outside the user's
  allowed scope

Configuration
-------------

1. Go to **Settings → Users & Companies → Users**
2. Open a user form and navigate to the **Preferences** tab
3. Select one or more **Preferred companies** from the list of allowed companies
4. Save. On next login, those companies will be automatically activated.

Notes
-----

* Preferred companies are only applied when no company selection is already
  stored in the current session (URL hash or browser cookie).
* If the user's default company (``company_id``) is among the preferred
  companies, it is placed first in the active company list.
    """,
    "author": "Iziwas",
    "license": "LGPL-3",
    "icon": "/preferred_companies/static/description/icon.png",
    "images": [
        "/preferred_companies/static/description/icon.png",
        "/preferred_companies/static/description/banner.png",
    ],
    "depends": ["base", "web"],
    "data": ["views/res_users_views.xml"],
    "assets": {
        "web.assets_backend": [
            "preferred_companies/static/src/js/company_service.js",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
