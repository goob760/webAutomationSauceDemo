from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get('https://www.saucedemo.com/')
print(driver.title)

user = driver.find_element("name", "user-name")
user.send_keys("standard_user")
password = driver.find_element("name", "password")
password.send_keys("secret_sauce")
user.send_keys(Keys.RETURN)

backpack = driver.find_element("name", "add-to-cart-sauce-labs-backpack")
backpack.click()

cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart.click()

checkout = driver.find_element(By.ID, "checkout")
checkout.click()

userFirst = driver.find_element(By.ID, "first-name")
userFirst.send_keys("Testy")
userLast = driver.find_element(By.ID, "last-name")
userLast.send_keys("Testerson")
userZip = driver.find_element(By.ID, "postal-code")
userZip.send_keys("85629")

checkoutEnter = driver.find_element(By.ID, "continue")
checkoutEnter.click()

finishCheckout = driver.find_element(By.ID, "finish")
finishCheckout.click()

time.sleep(10)

driver.quit()