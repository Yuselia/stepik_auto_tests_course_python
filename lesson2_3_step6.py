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
    
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
   
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    


