from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    х_el = browser.find_element(By.ID, "input_value")
    x = х_el.text
    input = browser.find_element(By.ID, "answer")
    y = calc(x)
    input.send_keys(y)
    	
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

#
