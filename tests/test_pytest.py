def test_addition():
    assert 2 + 2 == 4

def test_status():
    actual_status = 'passed'
    expected_status = 'passed'
    assert actual_status == expected_status

import pytest
@pytest.fixture
def user():
    return {
        'name': 'Alyona',
        'status': 'active'
    }
def test_user_name(user):
    assert user['name'] == 'Alyona'
def test_user_status(user):
    assert user['status'] == 'active'

import pytest


@pytest.mark.parametrize(
    'number, expected',
    [
        (2, 4),
        (3, 6),
        (5, 9)
    ]
)
def test_double(number, expected):
    assert number * 2 == expected

def test_login_status():
    actual_status = 401
    expected_status = 200

    assert actual_status == expected_status, (
        f'Expected status: {expected_status}, '
        f'but got: {actual_status}'
    )