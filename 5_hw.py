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