import json


def load_users():
    with open('data/users.json', 'r') as file:
        users = json.load(file)

    return users


def get_user_by_id(users, user_id):
    for user in users:
        if user['id'] == user_id:
            return user

    return None


def get_active_users(users):
    active_users = []

    for user in users:
        if user['status'] == 'active':
            active_users.append(user)

    return active_users


def get_user_email(users, user_id):
    user = get_user_by_id(users, user_id)

    if user is None:
        return None

    return user['email']