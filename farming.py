import os
from dotenv import load_dotenv
import time
import random
from sites_module import SiteA, SiteB

load_dotenv()

class PointFarmingAutomation:
    def __init__(self):
        self.is_farming = False
        self.progress = 0
        self.sites = [SiteA(api_key=os.getenv('SITE_A_API_KEY')), SiteB(api_key=os.getenv('SITE_B_API_KEY'))]

    def start_farming(self):
        if self.is_farming:
            print("Farming is already in progress.")
            return
        self.is_farming = True
        print("Starting point farming...")
        for site in self.sites:
            site.start_farming()
        self.monitor_farming()

    def stop_farming(self):
        if not self.is_farming:
            print("Farming is not in progress.")
            return
        print("Stopping point farming...")
        for site in self.sites:
            site.stop_farming()
        self.is_farming = False
        self.progress = 0

    def monitor_farming(self):
        try:
            while self.is_farming:
                time.sleep(10)
                self.progress = sum(site.get_points() for site in self.sites)
                print(f"Current farming progress: {self.progress} points")
        except KeyboardInterrupt:
            print("Farming interrupted by user.")
            self.stop_farming()

    def get_progress(self):
        return self.progress

if __name__ == '__main__':
    farming_automation = PointFarmingAutomation()
    try:
        farming_automation.start_farming()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        farming_automation.stop_farming()