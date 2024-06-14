import os
import requests
from dotenv import load_dotenv

load_dotenv()

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
        
        response = self.session.post(self.login_url, data=payload)
        if response.status_code == 200:
            print("Logged in successfully.")
        else:
            print("Failed to log in.")
    
    def perform_farming_tasks(self):
        response = self.session.get(self.farming_url)
        if response.status_code == 200:
            print("Farming tasks performed successfully.")
        else:
            print("Failed to perform farming tasks.")
    
    def retrieve_point_data(self):
        response = self.session.get(self.points_url)
        if response.status_url == 200:
            points = response.json().get("points", "No points data found.")
            print(f"Current points: {points}")
        else:
            print("Failed to retrieve points.")

if __name__ == "__main__":
    pfa = PointFarmingAutomation()
    pfa.login()
    pfa.perform_farming_tasks()
    pfa.retrieve_point_data()