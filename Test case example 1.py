from selenium import webdriver
import time

driver = webdriver.Chrome("C:\D_drive\Programs\Python projects\Test Automation\webdrivers\chromedriver.exe")
driver.get("https://www.google.bg")
time.sleep(5)  # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('How to test Log-in form')

search_box.submit()

time.sleep(5)  # Let the user actually see something!
driver.quit()
