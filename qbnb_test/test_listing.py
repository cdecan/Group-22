from qbnb.listing import create_listing


def test_r4_1_create_listing():
    '''
    Testing R4-1: If title is not alphanumeric or has spaces at the front or back, then it fails.
    '''

    user = User(user_id=1, email="test@test.com")
    assert create_listing('1','Title', 'DescriptionDescription', 20.00) is True
    assert create_listing('1', 'Title2', 'DescriptionDescription', 20.00) is True
    assert create_listing('1', 'Title!', 'DescriptionDescription', 20.00) is False
    assert create_listing('1', 'Title ', 'DescriptionDescription', 20.00) is False
    assert create_listing('1', ' Title', 'DescriptionDescription', 20.00) is False
    assert create_listing('1', ' Title ', 'DescriptionDescription', 20.00) is False


def test_r4_2_create_listing():
    '''
    Testing R4-2: If the title of the product is longer than 80 characters then it fails.
    '''

    user = User(user_id=1, email="test@test.com")
    assert create_listing('1', 'Title', 'DescriptionDescription', 20.00) is True
    assert create_listing('1', 'Titleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                               'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
                          'Descriptionnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
                          'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn',
                          20.00) is False


def test_r4_3_create_listing():
    '''
    Testing R4-3: If the description has under 20 or over 2000 characters, then it fails
    '''

    user = User(user_id=1, email="test@test.com")
    assert create_listing('1', 'Title', 'DescriptionDescription', 20.00) is True
    assert create_listing('1', 'Title2', 'Description', 20.00) is False
    longword = "a"
    for i in range(3000):
        longword += 'a'
    assert create_listing('1', 'Title3', longword, 20.00) is False


def test_r4_4_create_listing():
    '''
    Testing R4-4: If description is shorter than product's title, it fails
    '''

    user = User(user_id=1, email="test@test.com")
    assert create_listing('1', 'Title', 'DescriptionDescription', 20.00) is True
    assert create_listing('1', 'TitleTitleTitleTitleTitleTitleTitleTitleTitle',
                          'DescriptionDescription', 20.00) is False


def test_r4_5_create_listing():
    '''
    Testing R4-5: If price is lower than 10 or higher than 10,000, it fails
    '''

    user = User(user_id=1, email="test@test.com")
    assert create_listing('1', 'Title', 'DescriptionDescription', 20.00) is True
    assert create_listing('1', 'Title2', 'DescriptionDescription', 9.00) is False
    assert create_listing('1', 'Title3', 'DescriptionDescription', 10001.00) is False


def test_r4_6_create_listing():
    '''
    Testing R4-6: If last_modified_date is not after 2021-01-02 and before 2025-01-02, it fails
    '''

    user = User(user_id=1, email="test@test.com")
    assert create_listing('1', 'Title', 'DescriptionDescription', 20.00) is True


def test_r4_7_create_listing():
    '''
    Testing R4-7: The corresponding email cannot be empty and must exist
    '''

    user = User(user_id=1, email="test@test.com")
    user2 = User(user_id=2, email="")
    assert create_listing('1', 'Title', 'DescriptionDescription', 20.00) is True
    assert create_listing('2', 'Title2', 'DescriptionDescription', 20.00) is False
    assert create_listing('3', 'Title3', 'DescriptionDescription', 20.00) is False


def test_r4_8_create_listing():
    '''
    Testing r4-8: Two listings cannot have the same title
    '''

    user = User(user_id=1, email="test@test.com")
    assert create_listing('1', 'Title', 'DescriptionDescription', 20.00) is True
    assert create_listing('1', 'Title', 'DescriptionDescription', 20.00) is False