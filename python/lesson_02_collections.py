users = ["Alyona", "Shasha", "Olya"]
print(users[0])

users = ["Alyona", "Shasha", "Olya"]
users.append("Kate")
print(users)

users = ["Alyona", "Shasha", "Olya"]
for user in users:
    print(user)

user = {
    "name": "Alyona",
    "age": 34,
    "email": "aly@gmail.com"
}   
print(user['name'])

build = {
    "version": "1.2.0",
    "environment": "staging",
    "status": "failed"
}
if  build["status"] == "passed":
    print("Build passed")
else:
    print("Build failed")

