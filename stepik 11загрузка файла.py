from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("name")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("last")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("mail.ru")
	
    import os
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"    
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)    
    print(current_dir)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

#
