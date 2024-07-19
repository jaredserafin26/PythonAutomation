import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver serivce Selenium 160->160 chrome driver

#if company has VPN unable to download chromedriver
#service_obj = Service(r'C:\Users\jjpol\AppData\Local\Programs\Python\Python312\chromedriver.exe')
#driver = webdriver.Chrome(service=service_obj)


driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()

#grab title of webpage
driver.title
print(driver.title)
print(driver.current_url)














time.sleep(2)