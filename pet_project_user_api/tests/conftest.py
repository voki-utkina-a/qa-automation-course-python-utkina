import pytest

from app.user_service import load_users


@pytest.fixture
def users():
    return load_users()