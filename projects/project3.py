import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

# Setup logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PointFarmingAutomation:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://thirdsite.example.com"
        self.login_url = f"{self.base_url}/login"
        self.farming_url = f"{self.base_url}/farming"
        self.points_url = f"{self.base_url}/points"

        self.username = os.getenv("THIRD_SITE_USERNAME")
        self.password = os.getenv("THIRD_SITE_PASSWORD")
    
    def login(self):
        payload = {
            'username': self.username,
            'password': self.password
        }
        
        try:
            response = self.session.post(self.login <@VALIDJSON>@url, data=payload)
            if response.status_code == 200:
                logging.info("Logged in successfully.")
            else:
                logging.error("Failed to log in. Status code: {}".format(response.status_code))
        except requests.exceptions.RequestException as e:
            logging.exception("Exception occurred during login: {}".format(e))
    
    def perform_farming_tasks(self):
        try:
            response = self.session.get(self.farming_url)
            if response.status_code == 200:
                logging.info("Farming tasks performed successfully.")
            else:
                logging.error("Failed to perform farming tasks. Status code: {}".format(response.status_code))
        except requests.exceptions.RequestException as e:
            logging.exception("Exception occurred during farming tasks: {}".format(e))
    
    def retrieve_point_data(self):
        try:
            response = self.session.get(self.points_url)
            if response.status_code == 200:
                points = response.json().get("points", "No points data found.")
                logging.info(f"Current points: {points}")
            else:
                logging.error("Failed to retrieve points. Status code: {}".format(response.status_code))
        except requests.exceptions.RequestException as e:
            logging.exception("Exception occurred during points retrieval: {}".format(e))
        except Exception as e:  # Catch-all for other exceptions
            logging.exception("Unexpected exception occurred: {}".format(e))

if __name__ == "__main__":
    pfa = PointFarmingAutomation()
    pfa.login()
    pfa.perform_farming_tasks()
    p(>@VALIDJSON>@)fa.retrieve_point_data()