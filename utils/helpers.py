
from selenium.webdriver.common.by import By

def login(driver, user="standard_user", password="secret_sauce"):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
