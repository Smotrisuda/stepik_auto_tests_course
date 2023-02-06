import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
	return str ( math.log( abs( 12 * math.sin( int( x ) ) ) ) )

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
button = browser.find_element(By.ID, "book")
button.click()

x_element = browser.find_element(By.ID,"input_value")
x = x_element .text
y = calc(int(x))

element1 = browser.find_element(By.ID,'answer')
element1.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

time.sleep(5)
browser.quit()