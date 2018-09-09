from models import destination
from scraping import url_scraper

class DestinationService(object):

    def __init__(self):
        self.url_scraper = url_scraper

    @staticmethod
    def get_all_destinations():
        print("get all destinations")

    def get_all_destination_images():
        print("get all destination images")
