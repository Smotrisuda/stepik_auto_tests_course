import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
directory = "/Users/ihate/environments/selenium_env/Scripts"

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
first_name.send_keys('Ivan')

last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
last_name.send_keys('Ivanov')

email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
email.send_keys('ivan@ivanov.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

time.sleep(1)
browser.quit()