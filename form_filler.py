#form_filler.py: 👉 Selenium logic to fill the form

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def automate_gmail_signup(user_data):
    try:
        driver = webdriver.Chrome()
        driver.get("https://accounts.google.com/signup")
        time.sleep(2)

        driver.find_element(By.ID, "firstName").send_keys(user_data["first_name"])
        driver.find_element(By.ID, "lastName").send_keys(user_data["last_name"])
        driver.find_element(By.ID, "username").send_keys(user_data["username"])
        driver.find_element(By.NAME, "Passwd").send_keys(user_data["password"])
        driver.find_element(By.NAME, "ConfirmPasswd").send_keys(user_data["password"])
        time.sleep(1)

        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(5)

        return "submitted"
    except Exception as e:
        return f"error: {e}"
    finally:
        driver.quit()
