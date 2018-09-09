from models import airline
from scraping import url_scraper

class AirlineService(object):

    def __init__(self):
        self.url_scraper = url_scraper

    @staticmethod
    def get_all_airlines():
        print("get all airlines")

    def get_all_airline_images():
        print("get all airline images")