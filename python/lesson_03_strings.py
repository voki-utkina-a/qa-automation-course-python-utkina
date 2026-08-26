name = 'Alyona'
status = 'passed'
print(f'User {name} has status: {status}')

roles = 'admin,user,guest'
roles_list = roles.split(',')
print(roles_list)

username = '   alyona   '
username = username.strip()
print(username)

message = 'Test failed'
message = message.replace('failed', 'passed')
print(message)

errors = ['Login', 'Password', 'Email']
result = ' | '.join(errors)
print(result)

error_message = 'Invalid password'
if 'password' in error_message:
    print('Password error found')


text = '  login, password, email  '
text = text.strip()
items = text.split(',')
result = ' | '.join(items)
print(result)