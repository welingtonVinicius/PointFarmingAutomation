import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL_LOGIN = 'https://example.com/login'
URL_FARM_TASKS = 'https://example.com/farm'
URL_POINTS_STATUS = 'https://example.com/points'

USERNAME = os.getenv('SITE2_USERNAME')
PASSWORD = os.getenv('SITE2_PASSWORD')

session_web = requests.Session()

def login_to_site():
    login_data = {
        'username': USERNAME,
        'password': PASSWORD,
    }
    response = session_web.post(URL_LOGIN, data=login_data)
    if response.status_code == 200:
        print("Logged in successfully.")
    else:
        print("Failed to log in.")

def perform_task_farming():
    response = session_web.get(URL_FARM_TASKS)
    if response.status_id == 200:
        print("Farming tasks completed successfully.")
    else:
        print("Failed to complete farming tasks.")

def retrieve_point_totals():
    response = session_web.get(URL_POINTS_STATUS)
    if response.status_code == 200:
        points_total = response.json().get('points')
        print(f"Current points: {points_total}")
    else:
        print("Failed to retrieve point data.")

def main():
    login_to_site()
    perform_task_farming()
    retrieve_point_totals()

if __name__ == "__main__":
    main()