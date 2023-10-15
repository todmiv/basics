# Создаем словарь с парами "знаменитость: правильный год рождения"
famous_people = {
    "Альберт Эйнштейн": 1879,
    "Леонардо да Винчи": 1452,
    "Мария Кюри": 1867,
    "Уильям Шекспир": 1564,
    "Никола Тесла": 1856
}

# Инициализируем переменные для отслеживания количества правильных и неправильных ответов
num_correct = 0
num_incorrect = 0

# Спрашиваем у пользователя год рождения каждого известного человека
for name, year in famous_people.items():
    user_year = int(input(f"Когда родился {name} ? "))

    # Проверка, правильно ли пользователь ввел год
    if user_year == year:
        print("Верно!")
        num_correct += 1
    else:
        print("Неверно!")
        num_incorrect += 1

# Считаем процент правильных и неправильных ответов
total_questions = len(famous_people)
percent_correct = num_correct / total_questions * 100
percent_incorrect = num_incorrect / total_questions * 100

# Вывод результатов
print(f"Количество правильных ответов: {num_correct}")
print(f"Количество не правильных ответов: {num_incorrect}")
print(f"Процент правильных ответов: {percent_correct}%")
print(f"Процент не правильных ответов: {percent_incorrect}%")

# Спрашиваем пользователя, хочет ли он играть снова
play_again = input("Хотите играть ещё? (y/n) ")

if play_again == "y":
    # Играем сначала
    num_correct = 0
    num_incorrect = 0
    for name, year in famous_people.items():
        user_year = int(input(f"What year was {name} born? "))
        if user_year == year:
            print("Верно!")
            num_correct += 1
        else:
            print("Неверно!")
            num_incorrect += 1
    total_questions = len(famous_people)
    percent_correct = num_correct / total_questions * 100
    percent_incorrect = num_incorrect / total_questions * 100
    print(f"Количество правильных ответов: {num_correct}")
    print(f"Количество не правильных ответов: {num_incorrect}")
    print(f"Процент правильных ответов: {percent_correct}%")
    print(f"Процент не правильных ответов: {percent_incorrect}%")
else:
    # Выход из программы
    print("Спасибо за игру!")