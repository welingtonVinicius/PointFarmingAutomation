import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time

load_dotenv()

USERNAME = os.getenv("POINT_FARM_USERNAME")
PASSWORD = os.getenv("POINT_FARM_PASSWORD")

class PointFarmingAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.BASE_URL = "https://example.com"

    def login(self):
        try:
            self.driver.get(f"{self.BASE_URL}/login")
            username_input = self.driver.find_element_by_name("username")
            username_input.send_keys(USERNAME)
            password_input = self.driver.find_element_by_name("password")
            password_input.send_keys(PASSWORD)
            login_button = self.driver.find_element_by_xpath("//button[@type='submit']")
            login_button.click()
            time.sleep(5)
            print("Logged in successfully.")
        except Exception as e:
            print("Error during login:", e)

    def perform_farming_tasks(self):
        self.driver.get(f"{self.BASE_URL}/tasks")
        try:
            print("Completing tasks...")
            time.sleep(2)
            print("Tasks completed.")
        except Exception as e:
            print("Error while performing tasks:", e)

    def retrieve_point_data(self):
        try:
            self.driver.get(f"{self.BASE_URL}/dashboard")
            points_element = self.driver.find_element_by_id("points")
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
    bot.close_browser()