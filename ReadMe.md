```
.
├── LICENSE.md  
├── PULL_REQUEST_TEMPLATE.md  
├── .github  
│   └── workflows
|       ├── pytest.yml    ======> CI settings for running test automatically (trigger test for commits/pull-requests)
│       └── style_check.yml    ======> CI settings for running test automatically (trigger test for commits/pull-requests)
├── qbnb                 ======> Application source code
│   ├── booking.py        ======> Booking model
│   ├── cli.py        ======> Front-end command-line-interface
│   ├── __init__.py        ======> Required for a python module (can be empty)
│   ├── listing.py            ======> Listing model
│   ├── __main__.py        ======> Program entry point
│   ├── review.py        ======> Review model
│   └── user.py          ======> User model
├── qbnb_test          ======> Testing code
│   ├── backend  
│   │   ├── __init__.py        ======> Required for a python module (can be empty)
│   │   ├── test_listing.py        ======> Testing code for listing
│   │   ├── test_models.py         ======> Unused
│   │   ├── test_update_listing.py ======> Testing code for updating listing
│   │   ├── test_update_user.py    ======> Testing code for updating user
│   │   └── test_user.py           ======> Testing code for user
│   ├── conftest.py        ======> Code to run before/after all the testing
│   ├── frontend  
│   │   ├── __init__.py        ======> Required for a python module (can be empty)
│   │   ├── test_create_listing  
│   │   │   ├── __init__.py          ======> Required for a python module (can be empty)
│   │   │   ├── README.md  
│   │   │   ├── test_create_listing.in  
│   │   │   ├── test_create_listing.out  
│   │   │   └── test_create_listing.py  
│   │   ├── test_home_page  
│   │   │   ├── __init__.py        ======> Required for a python module (can be empty)
│   │   │   ├── README.md  
│   │   │   ├── test_home_page.in  
│   │   │   ├── test_home_page.out  
│   │   │   └── test_home_page.py  
│   │   ├── test_login  
│   │   │   ├── cases  
│   │   │   │   ├── R1  
│   │   │   │   │   ├── test_login.in  
│   │   │   │   │   └── test_login.out  
│   │   │   │   └── R2  
│   │   │   │       ├── test_login.in  
│   │   │   │       └── test_login.out  
│   │   │   ├── __init__.py        ======> Required for a python module (can be empty)
│   │   │   └── test_login.py  
│   │   ├── test_register  
│   │   │   ├── cases  
│   │   │   │   ├── R1  
│   │   │   │   │   ├── test_register.in  
│   │   │   │   │   └── test_register.out  
│   │   │   │   ├── R10  
│   │   │   │   │   └── test_register.in  
│   │   │   │   ├── R2  
│   │   │   │   │   ├── test_register.in  
│   │   │   │   │   └── test_register.out  
│   │   │   │   ├── R3  
│   │   │   │   │   ├── test_register.in  
│   │   │   │   │   └── test_register.out  
│   │   │   │   ├── R4  
│   │   │   │   │   ├── test_register.in  
│   │   │   │   │   └── test_register.out  
│   │   │   │   ├── R5  
│   │   │   │   │   ├── test_register.in  
│   │   │   │   │   └── test_register.out  
│   │   │   │   ├── R6  
│   │   │   │   │   ├── test_register.in  
│   │   │   │   │   └── test_register.out  
│   │   │   │   ├── R7  
│   │   │   │   │   ├── test_register.in  
│   │   │   │   │   └── test_register.out  
│   │   │   │   ├── R8  
│   │   │   │   │   └── test_register.in  
│   │   │   │   └── R9  
│   │   │   │       └── test_register.in  
│   │   │   ├── __init__.py        ======> Required for a python module (can be empty)
│   │   │   └── test_register.py  
│   │   ├── test_update_listing  
│   │   │   ├── cases  
│   │   │   │   ├── R1  
│   │   │   │   │   ├── test_update_listing.in  
│   │   │   │   │   └── test_update_listing.out  
│   │   │   │   ├── R2  
│   │   │   │   │   ├── test_update_listing.in  
│   │   │   │   │   └── test_update_listing.out  
│   │   │   │   ├── R3  
│   │   │   │   │   ├── test_update_listing.in  
│   │   │   │   │   └── test_update_listing.out  
│   │   │   │   └── R4  
│   │   │   │       ├── test_update_listing.in  
│   │   │   │       └── test_update_listing.out  
│   │   │   └── test_update_listing.py  
│   │   └── test_update_user_profile  
│   │       ├── __init__.py        ======> Required for a python module (can be empty)
│   │       ├── README.md  
│   │       ├── test_update_user_profile.in  
│   │       ├── test_update_user_profile.out  
│   │       └── test_update_user_profile.py  
│   ├── __init__.py        ======> Required for a python module (can be empty)
├── requirements.txt  
├── Sprint4ScrumBoard.png  
└── Sprint4Updates.md  
```
