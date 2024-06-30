import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 15).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '100'))
browser.find_element(By.ID, "book").click()

input1 = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);",input1 )

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


number = browser.find_element(By.ID, "input_value").text
number = int(number)

input1.send_keys(calc(number))
browser.find_element(By.XPATH, "//*[@id='solve']").click()

time.sleep(6)