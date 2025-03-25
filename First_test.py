import time

from selenium.webdriver.common.by import By
from selenium import webdriver

# Variable Declaration
wait = 5
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
first_name = "Fateemah"
last_name = "Animashaun"
postal_code = "100101"

# Browser Initialization
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

 # Login Details
UserName = driver.find_element(By.ID, "user-name")
UserName.send_keys(username)

PassWord = driver.find_element(By.ID, "password")
PassWord.send_keys(password)

Login = driver.find_element(By.ID, "login-button")
Login.click()

time.sleep(wait)

 # Add to Cart
AddToCart1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
AddToCart1.click()

AddToCart2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
AddToCart2.click()

AddToCart3 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
AddToCart3.click()

AddToCart4 = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
AddToCart4.click()

AddToCart5 = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
AddToCart5.click()

time.sleep(wait)

# Go to Checkout
ShoppingCart = driver.find_element(By.ID, "shopping_cart_container")
ShoppingCart.click()

Checkout = driver.find_element(By.ID, "checkout")
Checkout.click()

time.sleep(wait)

# Input Checkout Details
FirstName = driver.find_element(By.ID, "first-name")
FirstName.send_keys(first_name)

LastName = driver.find_element(By.ID, "last-name")
LastName.send_keys(last_name)

PostalCode = driver.find_element(By.ID, "postal-code")
PostalCode.send_keys(postal_code)

Continue = driver.find_element(By.ID, "continue")
Continue.click()

time.sleep(wait)

# Navigate to Product
Finish = driver.find_element(By.ID, "finish")
Finish.click()

BackToProducts = driver.find_element(By.ID, "back-to-products")
BackToProducts.click()

time.sleep(wait)
