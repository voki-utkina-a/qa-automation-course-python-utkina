print('Hello, Mystery Matters!')
print('Я', 'учусь', 'программировать', 'на', 'Python!')
print(1991, 'Gvido', 'van', 'Rossum')
print('В тексте есть "двойные" кавычки')
print("В тексте есть 'одинарные' кавычки")
print("I'm", 'learning', "Python", 'here!')
print()
print('4')
print('8')
print('15')
print('16')
print('23')
print('42')
print()
print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')
print()
print('What is your name?')
my_name = input()
print('Hello,', my_name, '!')
print()
first = 'just'
second = 'do it'
print(first, second, '!')
name = 'Тимур'
print('Привет,', name)
name1 = 'Гвидо'
print('Привет,', name1)
name2 = 'Тимур'
print('Привет,', name2)
name3 = 'Python'
print('Привет,', name3)
name4 = 'МИР'
print('Привет,', name4)
name5 = 'нечто из царства тьмы!'
print('Привет,', name5)

name = 'Aleksa'
figure = 'apple'
number = -3.14

print(name, figure, number)

name = 'Aleksa'
number = '2'
number2 = -3.14
print(name, int(number) + number2)

num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))
print("Result: ", num1 + num2)
print("Result: ", num1 - num2)
print("Result: ", num1 * num2)
print("Result: ", num1 / num2)
print("Result: ", num1 % num2)
print("Result: ", num1 ** num2)
print("Result: ", num1 // num2)

word = "Allo"
print(word * 50)

status_code = 404
response_time = 1.4
if status_code == 200 and response_time < 1.0:
    print("Успешно! Ответ получен быстро.")
elif status_code == 200 and response_time >= 1.0:
    print("Успешно, но сервер отвечает медленно.")
elif status_code == 404:
    print("Ошибка: Страница не найдена.")
else:
    print("Ошибка сервера с кодом:", status_code)



user_role = "user"
is_active = True
is_blocked = False
if (user_role == "admin" or user_role == "superuser") and is_active and not is_blocked:
    print("Доступ в админку разрешен")
else:
    print("В доступе отказано")


test_results = ["passed", "failed", "passed", "passed", "failed", "skipped"]
failed_count = 0
for result in test_results:
    if result == "failed":
        failed_count += 1 
print(f"Количество упавших тестов: {failed_count}")