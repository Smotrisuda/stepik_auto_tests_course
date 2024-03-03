import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1_element = browser.find_element(By.ID, 'num1')
    num1 = num1_element.text
    print(num1)
    num2_element = browser.find_element(By.ID, 'num2')
    num2 = num2_element.text
    print(num2)
    result = int(num1) + int(num2)
    print(result)
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(result)) 
    
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()