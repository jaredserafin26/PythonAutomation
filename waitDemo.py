import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'C:\Users\jjpol\AppData\Local\Programs\Python\Python312\chromedriver.exe')
name = "Jared"
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# 5 seconds ang maximum time out, if ma detect ang element in 2 sec (3 seconds save)
driver.implicitly_wait(5)


driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

#Chaining of elements to construct dynamically
#Use find_elements to iterate the list of products with the same class
#the implicitly wait will not word on this (Plural) / It will wait until list is return
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #lists[]
count = len(results)
assert count > 0

for result in results: #iterating the list of products
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

time.sleep(3)