import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
    input1.send_keys("Ivan")
    time.sleep(1)
    input1 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.second_class > input")
    input1.send_keys("Ivanov")
    time.sleep(1)
    input1 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.third_class > input")
    input1.send_keys("Ivan@mail.ru")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()