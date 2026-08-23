users = ['Alyona', 'Shasha', 'Olya']
print(users[0])
print(users[-1])
users[2] = 'new_Olya'
print(users[-1])

users = ['Alyona', 'Shasha', 'Olya']
users.append('Kate')
print(users)

users = ['Alyona', 'Shasha', 'Olya']
for user in users:
    print(user)

user = {
    'name': 'Alyona',
    'age': 34,
    'email': 'aly@gmail.com'
}   
print(user['name'])
user['age'] -= 5
print(user['age'])
for key, value in user.items():
    print(key, value)
for key in user:
    print(key)
for value in user.values():
    print(value)
    
build = {
    'version': '1.2.0',
    'environment': 'staging',
    'status': 'failed'
}
if  build['status'] == 'passed':
    print('Build passed')
else:
    print('Build failed')

game_settings = ('1920x1080', 'high', True)
print(game_settings[0])
print(game_settings[1])
print(game_settings[2])
for setting in game_settings:
    print(setting)
if 'high' in game_settings:
    print('High quality enabled')

bugs = [
    'login_error',
    'crash',
    'login_error',
    'ui_bug',
    'crash',
]
unique_bugs = set(bugs)
print(unique_bugs)
unique_bugs.add('sound_bug')
for bug in unique_bugs:
    print(bug)
if 'crash' in unique_bugs:
    print('crash found')

test_results = [
    {'name': 'Login', 'status': 'passed'},
    {'name': 'Payment', 'status': 'failed'},
]
for test in test_results:
    if test['status'] == 'failed':
        print(test['name'])