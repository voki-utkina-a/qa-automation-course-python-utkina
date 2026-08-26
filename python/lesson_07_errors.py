age = '25'
result = age + 5
print(result)

TypeError: can only concatenate str (not "int") to str

age = '25'
result = int(age) + 5
print(result)



numbers = [1, 2, 3]
print(numbers.upper())

AttributeError: 'list' object has no attribute 'upper'

text = 'hello'
print(text.upper())



user = {
    'name': 'Alyona',
    'age': 34
}
print(user['password'])

KeyError: 'password'

user = {
    'name': 'Alyona',
    'age': 34,
    'password': '123456'
}
print(user['password'])



users = ['Alyona', 'Olya', 'Kate']
print(users[3])

IndexError: list index out of range

print(users[2])



response = {
    'status': 200,
    'message': 'Success'
}
expected_status = 201
assert response['status'] == expected_status

AssertionError

assert response['status'] == expected_status, (
    f'Expected status: {expected_status}, '
    f'but got: {response["status"]}'
)