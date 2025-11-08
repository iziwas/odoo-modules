{
    'name': 'User Company Preferences',
    'version': '17.0.1.0.0',
    'category': 'Technical',
    'summary': 'Automatically select preferred companies on login',
    'description': """
        User Company Preferences
        ========================
        
        This module allows users to define their preferred companies among their allowed companies.
        
        Features:
        ---------
        * Users can select multiple preferred companies from their allowed companies
        * Preferred companies are automatically selected when the user logs in
        * Simple configuration through user preferences
        * Multi-company environment support
        
        Usage:
        ------
        1. Go to user preferences/settings
        2. Select your preferred companies from the list of allowed companies
        3. Save your preferences
        4. On next login, your preferred companies will be automatically selected
    """,
    'author': 'Iziwas',
    'license': 'LGPL-3',
    'depends': [
        "base", "web"
    ],
    'data': [
        "views/res_users_views.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "preferred_companies/static/src/js/company_service.js"
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}