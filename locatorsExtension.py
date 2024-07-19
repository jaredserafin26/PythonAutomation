import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'C:\Users\jjpol\AppData\Local\Programs\Python\Python312\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")

#use this if element has "a" tag.
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "password?").click()

driver.find_element(By.XPATH, '//form/div[1]/input').send_keys("demo@gmail.com") #XPATH
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(2) input').send_keys("Hello@1234") #CSSSELECTOR #Traverse
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys("Hello@1234") #CSSSELECTOR #ID

time.sleep(1)
#driver.find_element(By.XPATH,'//form/div[4]/button').click() #XPATH
#driver.find_element(By.CSS_SELECTOR,'form div:nth-child(4) button').click() #CSSSelector
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click() #XPATH

time.sleep(3)




#NOTES

#XPATH
#XPATH Traverse= //form/div[1]/input
#XPATH = //button[text()='Save New Password']

#a href TAG
#a tag = By.LINK_TEXT,"Forgot password? use keyword

#CSS SELECTOR
# "input[name='name']
# form div:nth-child(2) input
# #confirmPassword
#CSSSelector Traverse= form div:nth-child(2) input
#CSSSelector ID = #confirmPassword