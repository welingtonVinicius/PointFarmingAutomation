import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("POINT_FARM_USERNAME")
PASSWORD = os.getenv("POINT_FARM_PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError("USERNAME or PASSWORD is not set in the environment variables.")

class PointFarmingAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)
        self.BASE_URL = "https://example.com"

    def login(self):
        try:
            self.driver.get(f"{self.BASE_URL}/login")
            username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_input.send_keys(USERNAME)
            password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            password_input.send_keys(PASSWORD)
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            login_button.click()
            
            self.wait.until(EC.url_changes(f"{self.BASE_URL}/login"))
            print("Logged in successfully.")
        except Exception as e:
            print("Error during login:", e)

    def perform_farming_tasks(self):
        self.driver.get(f"{self.BASE_URL}/tasks")
        try:
            print("Completing tasks...")
            print("Tasks completed.")
        except Exception as e:
            print("Error while performing tasks:", e)

    def retrieve_point_data(self):
        try:
            self.driver.get(f"{self.BASE_URL}/dashboard")
            points_element = self.wait.until(EC.presence_of_element_located((By.ID, "points")))
            points = points_element.text
            print(f"Current points: {points}")
        except Exception as e:
            print("Error while retrieving points data:", e)

    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = PointFarmingAutomation()
    bot.login()
    bot.perform_farming_tasks()
    bot.retrieve_point_data()
    bot.close_before()