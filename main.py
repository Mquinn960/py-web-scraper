from services.airline_service import AirlineService
from services.destination_service import DestinationService
from services.file_helper_service import FileHelper
from scraping.url_scraper import Scraper

base_url = "https://www.edinburghairport.com"
airlines_url = "/help/contact-us/airline-contacts"
destinations_url = "/flights/destinations/a-to-z"

scraper = Scraper

airline_service = AirlineService(base_url, airlines_url, scraper)
destination_service = DestinationService(base_url, destinations_url, scraper)
file_helper_service = FileHelper

print("Starting data extraction... \n")

print("Getting airline data \n")
airline_data = airline_service.get_all_airlines(airline_service)

print("Saving airline data \n")
file_helper_service.save_local_csv(airline_data)
file_helper_service.save_local_image_data(airline_data)

print("Getting destination data \n")
destination_data = destination_service.get_all_destinations(destination_service)

print("Saving destination data \n")
file_helper_service.save_local_csv(destination_data)
file_helper_service.save_local_image_data(destination_data)

print("Data extraction complete \n")
