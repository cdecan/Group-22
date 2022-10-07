from qbnb.user import register, login


def test_r1_7_user_register():
    """
    Testing if the register function works
    """
    # testing for username in this block
    assert register('u0', 'user0@test.com', 'Test123_') is True
    assert register('u1', 'user1@test.com', 'Test123_') is True
    # illegal character
    assert register('u0.', 'test2@test.com', 'Test123_') is False
    # space as a prefix
    assert register(' u0', 'test2@test.com', 'Test123_') is False
    # space as a suffix
    assert register('u0 ', 'test2@test.com', 'Test123_') is False
    # space as a prefix and suffix
    assert register(' u0 ', 'test2@test.com', 'Test123_') is False
    # empty name
    assert register('', 'test2@test.com', 'Test123_') is False
    # name too short
    assert register('X', 'test2@test.com', 'Test123_') is False
    # name too long
    assert register('this is a very long name that the '
                    'program cannot possibly handle',
                    'test2@test.com', 'Test123_') is False
    # different variations of allowed names
    assert register('u 0', 'user2@test.com', 'Test123_') is True
    assert register('u   0', 'user3@test.com', 'Test123_') is True
    assert register('TEST 0', 'user4@test.com', 'Test123_') is True
    assert register('Test', 'user5@test.com', 'Test123_') is True

    # testing for email in this block
    assert register('u0', 'test0@test.com', 'Test123_') is True
    assert register('u0', 'test1@test.com', 'Test123_') is True
    # repeated email
    assert register('u0', 'test0@test.com', 'Test123_') is False
    # illegal email (missing ".")
    assert register('u0', 'test1@testcom', 'Test123_') is False
    # illegal email (multiple @)
    assert register('u0', 'test1@@test.com', 'Test123_') is False
    # illegal email (missing domain after @)
    assert register('u0', 'test1@.com', 'Test123_') is False
    # empty email
    assert register('u0', '', 'Test123_') is False
    # illegal email (missing content before @)
    assert register('u0', '@test.com', 'Test123_') is False
    # one that works to prove username and password is valid
    assert register('u0', 'test3@test.com', 'Test123_') is True

    # Testing password
    assert register('u0', 'p0@test.com', 'Test123_') is True
    # empty password (falls under password too short)
    assert register('u0', 'p1@test.com', '') is False
    # missing special character
    assert register('u0', 'p1@test.com', 'Test123') is False
    # missing number
    assert register('u0', 'p1@test.com', 'Test_') is False
    # missing number and special character
    assert register('u0', 'p1@test.com', 'Test') is False
    # does not have upper case letter
    assert register('u0', 'p1@test.com', 'test_dsak123') is False
    # does not have lower case letter
    assert register('u0', 'p1@test.com', 'TEST123_') is False
    # one that works to prove username and email is valid
    assert register('u0', 'p1@test.com', 'TESTpassword_123*^%') is True


def test_r2_1_login():
    """
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test,
    so we already have many users in database)
    """

    user = login('user0@test.com', 'Test123_')
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', '1234567')
    assert user is None
