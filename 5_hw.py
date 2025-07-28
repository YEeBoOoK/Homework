# 1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”


# Первый вариант (там, где поиск элементов по ..., можно любое раскомментировать)

# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
# def search_loginform_elements():
#     driver = webdriver.Chrome()
#     driver.get("https://www.saucedemo.com/")

    # Поиск элементов по имени
    # username = driver.find_element(By.NAME, 'user-name')
    # password = driver.find_element(By.NAME, 'password')
    # button = driver.find_element(By.NAME, 'login-button')

    # Поиск элементов по атрибуту data-test
    # username = driver.find_element(By.CSS_SELECTOR, '[data-test="username"]')
    # password = driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')
    # button = driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]')

    # Поиск элементов по ID
    # username = driver.find_element(By.ID, 'user-name')
    # password = driver.find_element(By.ID, 'password')
    # button = driver.find_element(By.ID, 'login-button')

    # Проверка, что все элементы найдены
    # if username and password and button:
    #     print('Элементы найдены')
    # else:
    #     print('Элементы не найдены')

# search_loginform_elements()



# Второе решение
# Вывод "Элементы не найдены" вместо ошибок

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

# def search_loginform_elements():
#     driver = webdriver.Chrome()
#     driver.get("https://www.saucedemo.com/")
#
#     # Проверка, что все элементы найдены
#     try:
#         # Поиск элементов по атрибуту data-test
#         # В username допущена ошибка, чтобы проверить, что выводится "Элементы не найдены", если хоть 1 элемент не находится
#         username = driver.find_element(By.CSS_SELECTOR, '[data-test="username1"]')
#         password = driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')
#         button = driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]')
#         print('Элементы найдены')
#     except NoSuchElementException:
#         print('Элементы не найдены')
#
# search_loginform_elements()


# Третий вариант
# Вывод найденных и ненайденных элементов

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def search_loginform_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    elements = {
        "username": '[data-test="username"]',
        "password": '[data-test="password"]',
        "button": '[data-test="login-button"]'
    }

    for name, selector in elements.items():
        try:
            driver.find_element(By.CSS_SELECTOR, selector)
            print(f'Элемент "{name}" найден')
        except NoSuchElementException:
            print(f'Ошибка при поиске элемента: {name}')

search_loginform_elements()