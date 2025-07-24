# 2. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.
def max_number(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    elif a == b:
        print('Числа равны')
    else:
        print('Что-то неладное')

max_number(1, 2)

# 3. Функция на вход получает два произвольных числа. Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”
def difference_135(a, b):
    if abs(a - b) == 135:
        print('yes')
    else:
        print('no')

difference_135(0, 135)

# 4. Функция на вход получает произвольное число от 1 до 12 (номер месяца). Вывести название сезона года в консоль (зима, весна, лето, осень)
def the_seasons(month_num):
    if month_num in (1, 2, 12):
        print('Зима')
    elif month_num in range (3, 6):
        print('Весна')
    elif month_num in range (6, 9):
        print('Лето')
    elif month_num in range (9, 12):
        print('Осень')
    else:
        print('Такого месяца не существует -_-')

the_seasons(11)


# 5. Функция на вход получает три произвольных числа. Если все числа больше 10, то вывести на экран “yes”, иначе “no”;
def numbers_greater_10(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        print('yes')
    else:
        print('no')

numbers_greater_10(11, 11, 11)

# 6. Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.
def positive_numbers(numlist:list) -> int:
    for number in numlist:
        if number > 0:
            print(number)

positive_numbers([-1, -2, 3, -4, -5])


# 7. Функция на вход получает 2 переменные.
# a. Кол-во лет (int)
# b. Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
def number_of_days(years:int, months:int)->int:
    return years * 12 * 29 + months * 29

print('Количество дней за это время = ', + number_of_days(26, 2))