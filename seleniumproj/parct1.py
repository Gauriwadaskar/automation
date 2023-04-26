#E:\gauri python\automation\seleniumproj\chromedriver_win32
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="E:\gauri python\\automation\seleniumproj\chromedriver_win32\chromedriver.exe")
driver.get('https://www.facebook.com')
print(driver.title)
driver.maximize_window()
driver.get('https://www.instagram.com/accounts/login/')
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("abc@12")
time.sleep(5)
driver.quit()