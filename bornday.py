year_of_birth = int(input("Введите год рождения А.С. Пушкина: "))

if year_of_birth == 1799:
    birthday = int(input("Введите день рождения А.С. Пушкина: "))

    if birthday == 6:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")
