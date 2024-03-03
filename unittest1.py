"""3.2 Тестирование web-приложений и тестовые фреймворки
Попробуйте оформить тесты из первого модуля в стиле unittest.
Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        time.sleep(1)
        input1 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.second_class > input")
        input1.send_keys("Ivanov")
        time.sleep(1)
        input1 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.third_class > input")
        input1.send_keys("Ivan@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertIn('Congratulations', welcome_text, "Something go wrong")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        time.sleep(1)
        input1 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.second_class > input")
        input1.send_keys("Ivanov")
        time.sleep(1)
        input1 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.third_class > input")
        input1.send_keys("Ivan@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertIn('Congratulations', welcome_text, "Something go wrong")


if __name__ == "__main__":
    unittest.main()