from selenium import webdriver
driver = webdriver.Chrome("C:\D_drive\Programs\Python projects\Test Automation\webdrivers\chromedriver.exe")


driver.get("https://www.abv.bg/")
driver.find_element_by_id("username").send_keys("your_username_here")

driver.find_element_by_id ("password").send_keys("your_password_here")
driver.find_element_by_id("loginBut").click()
