import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

# Endpoint URLs
LOGIN_ENDPOINT = 'https://example.com/login'
TASK_FARMING_ENDPOINT = 'https://example.com/farm'
POINTS_RETRIEVAL_ENDPOINT = 'https://example.com/points'

# Credentials
USER_NAME = os.getenv('SITE2_USERNAME')
USER_PASSWORD = os.getenv('SITE2_PASSWORD')

# Initiating the session
web_session = requests.Session()


def log_into_website():
    credentials = {
        'username': USER_NAME,
        'password': USER_PASSWORD,
    }
    response = web_session.post(LOGIN_ENDPOINT, data=credentials)
    if response.status_code == 200:
        print("Logged in successfully.")
    else:
        print("Failed to log in.")


def execute_farming_activities():
    response = web_session.get(TASK_FARMING_ENDPOINT)
    if response.status_code == 200:
        print("Farming tasks completed successfully.")
    else:
        print("Failed to complete farming tasks.")


def fetch_points_information():
    response = web_session.get(POINTS_RETRIEVAL_ENDPOINT)
    if response.status_code == 200:  # This was corrected from 'status_id' to 'status_code'
        points = response.json().get('points')
        print(f"Current points: {points}")
    else:
        print("Failed to retrieve point data.")


def main():
    log_into_website()
    execute_farming_activities()
    fetch_points_information()


if __name__ == "__main__":
    main()