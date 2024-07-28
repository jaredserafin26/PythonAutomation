import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r'C:\Users\jjpol\AppData\Local\Programs\Python\Python312\chromedriver.exe')
name = "Jared"
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# 5 seconds ang maximum time out, if ma detect ang element in 2 sec (3 seconds save)
driver.implicitly_wait(2)


driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

#Chaining of elements to construct dynamically
#Use find_elements to iterate the list of products with the same class
#the implicitly wait will not word on this (Plural) / It will wait until list is return
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #lists[]
count = len(results)
assert count > 0
print(count)

for result in results: #iterating the list of products
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#COUNT NO. OF ITEMS / SUM VALIDATION
#results2 = driver.find_elements(By.XPATH,"//table[@id='productCartTables']/tbody/tr/td[5]/p")#lists[]
#OR
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")#lists[]
#countTotal = len(prices)
#print(countTotal)
#assert countTotal > 0
sum = 0

#Extract text out of web element
for price in prices: #iterating the list of products
    sum = sum + int(price.text)  #48 + 160 + 180 / string converted to integer

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) #string converted to integer
assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#explicit wait / will just target 1 element to show up
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

time.sleep(3)






