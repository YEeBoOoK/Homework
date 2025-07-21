# Задача 1
def task_1(a:int, b:float, c:str, d:list, e:bool):
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))

task_1(1, 1.12, 'meow', [1, 2, 3], True)


# Задача 2
def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])
    print('Это последовательность чисел Фибоначчи')

task_2()


# Задача 3
def task_3(a:int) -> int:
    return a**2

print(task_3(6))