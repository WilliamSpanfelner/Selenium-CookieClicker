from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/william/Developer/Python/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

url = "http://secure-retreat-92358.herokuapp.com/"

driver.get(url)

# Get the firstname text signup field and print the placeholder text
firstname = driver.find_element(By.NAME, "fName")
print(firstname.get_attribute("placeholder"))

# Send text to the firstname text field and tab to the last name field
firstname.send_keys("Fred")
firstname.send_keys(Keys.TAB)

# Send text to the lastname text field and tab to the email field
lastname = driver.find_element(By.NAME, "lName")
print(lastname.get_attribute("placeholder"))

lastname.send_keys("Flinstone")
lastname.send_keys(Keys.TAB)

# Send text to the email text field and tab to the signup button
email_address = driver.find_element(By.NAME, "email")
print(email_address.get_attribute("placeholder"))

email_address.send_keys("ff@bedrock.az")
# email_address.send_keys(Keys.TAB)

# Click the Sign Up button
# sign_up = driver.find_element(By.TAG_NAME, "button")
sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()

# driver.quit()