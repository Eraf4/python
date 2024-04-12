from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
driver = webdriver.Edge()

driver.get("http://es.wikipedia.org")
web_element = driver.find_element(By.NAME, 'search')
web_element.send_keys("Flou Paraguay" + Keys.ENTER)
print(driver.title)
time.sleep(10)
driver.quit()