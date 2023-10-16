import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get("https://www.csdn.net/")
driver.find_element(by=By.ID, value='toolbar-search-input').send_keys('python')

driver.find_element(by=By.ID, value='toolbar-search-button').click()

time.sleep(10)
driver.quit()