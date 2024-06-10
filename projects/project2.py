import os
import requests
from dotenv import load_dotenv

load_dotenv()

LOGIN_URL = 'https://example.com/login'
FARMING_TASK_URL = 'https://example.com/farm'
POINT_URL = 'https://example.com/points'
USERNAME = os.getenv('SITE2_USERNAME')
PASSWORD = os.getenv('SITE2_PASSWORD')

session = requests.Session()

def login():
    payload = {
        'username': USERNAME,
        'password': PASSWORD,
    }
    response = session.post(LOGIN_URL, data=payload)
    if response.status_code == 200:
        print("Logged in successfully.")
    else:
        print("Failed to log in.")

def perform_farming_tasks():
    response = session.get(FARMING_TASK_URL)
    if response.status_code == 200:
        print("Farming tasks completed successfully.")
    else:
        print("Failed to complete farming tasks.")

def retrieve_point_data():
    response = session.get(POINT_URL)
    if response.status_id == 200:
        points = response.json().get('points')
        print(f"Current points: {points}")
    else:
        print("Failed to retrieve point data.")

def main():
    login()
    perform_farming_tasks()
    retrieve_point_data()

if __name__ == "__main__":
    main()