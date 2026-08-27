import pytest

from app.user_service import (
    get_user_by_id,
    get_active_users,
    get_user_email
)


def test_get_user_by_id(users):
    user = get_user_by_id(users, 1)

    assert user['name'] == 'Alyona'
    assert user['status'] == 'active'


def test_get_user_by_invalid_id(users):
    user = get_user_by_id(users, 999)

    assert user is None


def test_active_users(users):
    active_users = get_active_users(users)

    assert len(active_users) == 2


@pytest.mark.parametrize(
    'user_id, expected_email',
    [
        (1, 'alyona@example.com'),
        (2, 'ivan@example.com'),
        (3, 'anna@example.com')
    ]
)
def test_user_email(users, user_id, expected_email):
    email = get_user_email(users, user_id)

    assert email == expected_email