import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'C:\Users\jjpol\AppData\Local\Programs\Python\Python312\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


#ADD TO CART

driver.find_element(By.XPATH,"//div[@class='products']//div[2]//div[2]//a[2]").click()
driver.find_element(By.XPATH, "//div[@class='products']//div[2]//button").click()
time.sleep(1)

driver.find_element(By.XPATH,"//div[@class='products']//div[3]//div[2]//a[2]").click()
driver.find_element(By.XPATH, "//div[@class='products']//div[3]//div[3]//button").click()
time.sleep(1)

driver.find_element(By.XPATH,"//div[@class='products']//div[4]//div[2]//a[2]").click()
driver.find_element(By.XPATH, "//div[@class='products']//div[4]//button").click()
time.sleep(1)

#SEARCH
driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("Carrot")
time.sleep(1)

driver.find_element(By.XPATH,"//div[@class='products']//div[1]//div[2]//a[2]").click()
driver.find_element(By.XPATH, "//div[@class='product']//div[3]//button").click()
time.sleep(1)










time.sleep(3)
