import time
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get("https://suninjuly.github.io/execute_script.html")
    number = browser.find_element(By.ID, "input_value").text
    number = calc(int(number))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(number)

    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # скролл страницы

    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()

    button.click()


finally:
    time.sleep(10)
    browser.quit()
