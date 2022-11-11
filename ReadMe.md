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
│   ├── backend  
│   │   ├── __init__.py            ======> Required for a python module (can be empty)
│   │   ├── test_listing.py        ======> Testing code for listing
│   │   ├── test_models.py         ======> Unused
│   │   ├── test_update_listing.py ======> Testing code for updating listing
│   │   ├── test_update_user.py    ======> Testing code for updating user
│   │   └── test_user.py           ======> Testing code for user
│   ├── conftest.py        ======> Code to run before/after all the testing
│   ├── frontend  
│   │   ├── __init__.py          ======> Required for a python module (can be empty)
│   │   ├── test_create_listing  ======> All requirement tests for the Create Listing page
│   │   │   ├── __init__.py              ======> Required for a python module (can be empty)
│   │   │   ├── README.md                ======> Explanation for "create listing page" testing methodology
│   │   │   ├── test_create_listing.in   ======> Series of inputs for testing all "create listing page" requirements
│   │   │   ├── test_create_listing.out  ======> Expected output from all inputs
│   │   │   └── test_create_listing.py   ======> Executes input/output verification create listing page
│   │   ├── test_home_page       ======> All requirement tests for the User Home page
│   │   │   ├── __init__.py              ======> Required for a python module (can be empty)
│   │   │   ├── README.md                ======> Explanation for "home page" testing methodology
│   │   │   ├── test_home_page.in        ======> Series of inputs for testing all "home page" requirements
│   │   │   ├── test_home_page.out       ======> Expected output from all inputs
│   │   │   └── test_home_page.py        ======> Executes input/output verification for home page
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
│   │   ├── test_register            ======> Tests for the user register page (More info in comments)
│   │   │   ├── cases            ======> Cases pulled from A2 register function
│   │   │   │   ├── R1          ======> Test R1-1: Email cannot be empty. password cannot be empty.
│   │   │   │   │   ├── test_register.in          ======> Input for R1-1
│   │   │   │   │   └── test_register.out            ======> Output for R1-1
│   │   │   │   ├── R10            ======> Test R1-10: Balance should be initialized as 100 at the time of registration.
│   │   │   │   │   └── test_register.in            ======> Input for R1-10
│   │   │   │   ├── R2            ======> Test R1-2: A user is uniquely identified by his/her user id - automatically generated.
│   │   │   │   │   ├── test_register.in            ======> Input for R1-2
│   │   │   │   │   └── test_register.out            ======> Output for R1-2
│   │   │   │   ├── R3            ======> Test R1-3: The email has to follow addr-spec defined in RFC 5322
│   │   │   │   │   ├── test_register.in            ======> Input for R1-3
│   │   │   │   │   └── test_register.out            ======> Output for R1-3
│   │   │   │   ├── R4            ======> Test R1-4: Password has to meet the required complexity
│   │   │   │   │   ├── test_register.in            ======> Input for R1-4
│   │   │   │   │   └── test_register.out            ======> Input for R1-4
│   │   │   │   ├── R5            ======> Test R1-5: User name has to be non-empty, etc.
│   │   │   │   │   ├── test_register.in            ======> Input for R1-5
│   │   │   │   │   └── test_register.out            ======> Output for R1-5
│   │   │   │   ├── R6            ======> Test R1-6: User name has to be a certain length.
│   │   │   │   │   ├── test_register.in            ======> Input for R1-6
│   │   │   │   │   └── test_register.out            ======> Output for R1-6
│   │   │   │   ├── R7            ======> Test R1-7: If the email has been used, the operation failed
│   │   │   │   │   ├── test_register.in            ======> Input for R1-7
│   │   │   │   │   └── test_register.out            ======> Output for R1-7
│   │   │   │   ├── R8            ======> Test R1-8: Shipping address is empty at the time of registration
│   │   │   │   │   └── test_register.in            ======> Input for R1-8
│   │   │   │   └── R9            ======> Test R1-9: Postal code is empty at the time of registration
│   │   │   │       └── test_register.in            ======> Input for R1-9
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
│   │   └── test_update_user_profile      ======> Tests for update user profile page
│   │       ├── __init__.py        ======> Required for a python module (can be empty)
│   │       ├── README.md              ======> Explanations for tests (read this)
│   │       ├── test_update_user_profile.in              ======> Input for all tests
│   │       ├── test_update_user_profile.out              ======> Output for all tests
│   │       └── test_update_user_profile.py  
│   ├── __init__.py        ======> Required for a python module (can be empty)
├── requirements.txt  
├── Sprint4ScrumBoard.png  
└── Sprint4Updates.md  
```
