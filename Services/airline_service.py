from bs4 import BeautifulSoup

from models.airline import Airline

class AirlineService(object):

    def __init__(self, base_url, airlines_url, scraper):
        self.base_url = base_url
        self.scraper = scraper

    @staticmethod
    def get_all_airlines(self):
        return "All Airlines"
