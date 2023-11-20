from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
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
