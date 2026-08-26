file = open('Hi.txt', 'w')
file.write('Hello, Mystery Matters')
file.write('!')
file.close()

file = open('Hi.txt', 'a')
file.write('Hello, Mystery Matters\n')
file.write('!')
file.close()

answer = input("Введите текст:")
file = open('Hi.txt', 'a')
file.write(answer + '\n')
file.close()

file = open('Hi.txt', 'r')
file.read(3)
file.close()

file = open('Hi.txt', 'r')
for line in file:
    print(line)
file.close()

try:
    with open('my_file.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не найден")

with open('Hi.txt', 'a') as file:
    file.write('\nAlyona')

import json

with open('user.json', 'r') as file:
    data = json.load(file)
print(data)
print(data['password'])

build = {
    'version': '1.2.0',
    'environment': 'staging',
    'status': 'failed'
}
with open('build.json', 'w') as file:
    json.dump(build, file, indent=4)

with open('build.json', 'r') as file:
    build_data = json.load(file)
if build_data['status'] == 'passed':
    print('Build passed')
else:
    print('Build failed')