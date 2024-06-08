import os
import time
import random
import asyncio
import logging
from dotenv import load_dotenv
from sites_module import SiteA, SiteB

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

class PointFarmingAutomation:
    def __init__(self):
        self.is_farming = False
        self.progress = 0
        self.sites = [SiteA(api_key=os.getenv('SITE_A_API_KEY')), SiteB(api_key=os.getenv('SITE_B_API_KEY'))]

    async def start_farming(self):
        if self.is_farming:
            logging.info("Farming is already in progress.")
            return
        self.is_farming = True
        logging.info("Starting point farming asynchronously...")
        await asyncio.gather(*(site.start_farming() for site in self.sites))
        await self.monitor_farming()

    async def stop_farming(self):
        if not self.is_farming:
            logging.info("Farming is not in progress.")
            return
        logging.info("Stopping point farming...")
        await asyncio.gather(*(site.stop_farming() for site in self.sites))
        self.is_farming = False
        self.progress = 0

    async def monitor_farming(self):
        try:
            while self.is_farming:
                await asyncio.sleep(10)  # Use asyncio.sleep() for asynchronous sleep
                self.progress = sum(await site.get_points() for site in self.sites)
                logging.info(f"Current farming progress: {self.progress} points")
        except KeyboardInterrupt:
            logging.info("Farming interrupted by user.")
            await self.stop_farming()

    def get_progress(self):
        return self.progress

async def main():
    farming_automation = PointFarmingAutomation()
    try:
        await farming_automation.start_farming()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        await farming_automation.stop_farming()

if __name__ == '__main__':
    asyncio.run(main())