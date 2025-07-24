# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Создаем объекты
rectangle1 = Rectangle(5, 6)
rectangle2 = Rectangle(7, 8)
rectangle3 = Rectangle(9, 10)

# Выводим площадь и периметр первого прямоугольника
print(f'Площадь прямоугольника №1: {rectangle1.area()}')
print(f'Периметр прямоугольника №1: {rectangle1.perimeter()}')

# Выводим площадь и периметр второго прямоугольника
print(f'Площадь прямоугольника №2: {rectangle2.area()}')
print(f'Периметр прямоугольника №2: {rectangle2.perimeter()}')

# Выводим площадь и периметр третьего прямоугольника
print(f'Площадь прямоугольника №3: {rectangle3.area()}')
print(f'Периметр прямоугольника №3: {rectangle3.perimeter()}')




# 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a // self.b

    def subtraction(self):
        return self.a - self.b

example = Math(2, 2)

print(example.a, '+', example.b, '=', example.addition())
print(example.a, '*', example.b, '=', example.multiplication())
print(example.a, '/', example.b, '=', example.division())
print(example.a, '-', example.b, '=', example.subtraction())




# 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box”, “Check Box”, "Radio Button", "Web Tables", "Buttons", "Links", "Broken Links - Images", "Upload and Download", "Dynamic Properties")
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

# class Elements:
#     def __init__(self, text, butt_type = "Кнопка", loc = None):
#         self.text = text
#         self.butt_type = butt_type
#         self.loc = loc
#
#     def click(self):
#         return print(f"Клик по кнопке {self.text}")
#
# # Создаем объекты для каждой кнопки
# text_box = Elements('Text Box')
# check_box = Elements('Check Box')
# radio_button = Elements('Radio Button')
# web_tables = Elements('Web Tables')
# buttons = Elements('Buttons')
# links = Elements('Links')
# broken_links_images = Elements('Broken Links - Images')
# upload_and_download = Elements('Upload and Download')
# dynamic_properties = Elements('Dynamic Properties')
#
# # Выводим текст для каждой кнопки
# print(text_box.text)
# print(check_box.text)
# print(radio_button.text)
# print(web_tables.text)
# print(buttons.text)
# print(links.text)
# print(broken_links_images.text)
# print(upload_and_download.text)
# print(dynamic_properties.text)
#
# # "Кликаем" по каждой кнопке
# text_box.click()
# check_box.click()
# radio_button.click()
# web_tables.click()
# buttons.click()
# links.click()
# broken_links_images.click()
# upload_and_download.click()
# dynamic_properties.click()

# Оптимизированный вариант
class Elements:
    def __init__(self, text, butt_type = "Кнопка", loc = None):
        self.text = text
        self.butt_type = butt_type
        self.loc = loc

    def click(self):
        return f"Клик по кнопке {self.text}"

# Создаём список всех кнопок
buttons_data = [
    'Text Box',
    'Check Box',
    'Radio Button',
    'Web Tables',
    'Buttons',
    'Links',
    'Broken Links - Images',
    'Upload and Download',
    'Dynamic Properties'
]

# Создаём объекты кнопок
buttons = [Elements(text) for text in buttons_data]

# Выводим текст и "кликаем" по каждой кнопке
for button in buttons:
    print(f'Текст: {button.text}')
    print(f'Тип: {button.butt_type}')
    print(button.click())
    print('-' * 40)




# 4. В отдельном файле напишите программу с классом Car.
# a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i.   Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii.  Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска.
# iv.  Четвертый метод — присвоение автомобилю типа.
# v.   Пятый — присвоение автомобилю цвета.
class Car:
    def __init__(self, color, type_car, year):
        self.color = color
        self.type_car = type_car
        self.year = year

    # Запуск автомобиля
    def starting(self):
        print('Автомобиль заведен')

    # Отключение автомобиля
    def turning_off (self):
        print('Автомобиль заглушен')

    # Присвоение года выпуска автомобилю
    def assigning_year(self, new_year):
        self.year = new_year
        print(f'Год выпуска изменён на {self.year}')

    # Присвоение автомобилю типа
    def assigning_type(self, new_type):
        self.type_car = new_type
        print(f'Тип автомобиля изменён на {self.type_car}')

    # Присвоение автомобилю цвета
    def assigning_color(self, new_color):
        self.color = new_color
        print(f'Цвет автомобиля изменён на {self.color}')

# Создаём авто
my_car = Car('Красный', 'Coupe', '2023')

# Вызываем методы
my_car.starting()
my_car.assigning_color('cерый')
my_car.turning_off()