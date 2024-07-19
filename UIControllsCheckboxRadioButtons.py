import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'C:\Users\jjpol\AppData\Local\Programs\Python\Python312\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Use this if positions changed
#driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#print(len(checkboxes))

#for checkbox in checkboxes:
#    if checkbox.get_attribute("value") == "option2":
#        checkbox.click()
#        assert checkbox.is_selected() #check if it is selected / if not selected the test will fail
#        break


#ASSIGNMENT
#USING XPATH
#driver.find_elements(By.XPATH, "//input[@type='radio']")
#radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
#print(len(radios))

#for radio in radios:
#    if radio.get_attribute("value") == "radio2":
#        radio.click()
#        assert radio.is_selected()
#        break

#use this if positions will not change
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

time.sleep(2)

assert driver.find_element(By.ID,"displayed-text").is_displayed() #check if displayed
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed() #check if not displayed
time.sleep(2)
driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.ID,"displayed-text").is_displayed() #check if displayed
driver.find_element(By.ID,"displayed-text").send_keys("THIS IS A TEST")


time.sleep(2)