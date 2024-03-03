from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/registration1.html'
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input1.send_keys('First')
        input2 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys('Second')
        input3 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys('Email')
        input4 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.first_class > input")
        input4.send_keys('Phone')
        input5 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.second_class > input")
        input5.send_keys('Address')
        button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
        button.click()
        time.sleep(1)
        res = browser.find_element(By.TAG_NAME, 'h1').text
        browser.quit()
        print(res)
        self.assertIn('Congratulations', res, "Something go wrong")

    def test_abs2(self):
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/registration2.html'
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input1.send_keys('First')
        input2 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys('Second')
        input3 = browser.find_element(By.CSS_SELECTOR, "div > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys('Email')
        input4 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.first_class > input")
        input4.send_keys('Phone')
        input5 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.second_class > input")
        input5.send_keys('Address')
        button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
        button.click()
        time.sleep(1)
        res = browser.find_element(By.TAG_NAME, 'h1').text
        browser.quit()
        print(res)
        self.assertIn('Congratulations', res, "Something go wrong")


if __name__ == "__main__":
    unittest.main()