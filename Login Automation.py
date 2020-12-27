from selenium import webdriver
import time
driver = webdriver.Chrome("PATH")


driver.get("your_website")
time.sleep(5)
driver.find_element_by_id("username").send_keys("your_username_here")

driver.find_element_by_id ("password").send_keys("your_password_here")
time.sleep(5)
driver.find_element_by_id("login").click()
