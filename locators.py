import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r'C:\Users\jjpol\AppData\Local\Programs\Python\Python312\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME,"email").send_keys("js@2doit.nu")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

# XPATH - //tagname[@attribute='value] -> //input[@type='submit']
# CSSSelector - tagname[attribute='value] -> #id -> .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Jared")
driver.find_element(By.CSS_SELECTOR,'#inlineRadio1').click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)



# Xpath -> //tagname[@attribute='value'] -> //input[@type='submit'] <- syntax for xpath
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message #pass or fail validation

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello Again!")

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

time.sleep(2)

driver.quit()




#XPATH = //*[@id="slider-k6540ce9ae3b2ed1c0251ebe8"]/div[1]/div[4]/ul/li/div/ul[2]/li[1]/a



time.sleep(5)