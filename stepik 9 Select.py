from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    y = str(int(a) + int(b))
    
    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(y) 
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()
		
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
    