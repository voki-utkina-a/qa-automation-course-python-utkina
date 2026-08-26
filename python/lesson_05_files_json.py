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