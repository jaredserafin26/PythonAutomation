import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'C:\Users\jjpol\AppData\Local\Programs\Python\Python312\chromedriver.exe')
name = "Jared"
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

#switch browser mode to alert mode
alert = driver.switch_to.alert #place alert into object
alertText = alert.text
print(alertText)
alert.accept() #OK
#alert.dismiss() #CANCEL
assert name in alertText

time.sleep(2)