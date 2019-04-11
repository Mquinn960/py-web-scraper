from services.airline_service import AirlineService
from services.destination_service import DestinationService
from scraping.url_scraper import Scraper

base_url = ""
airlines_url = ""
destinations_url = ""

scraper = Scraper

airline_service = AirlineService(base_url, airlines_url, scraper)
destination_service = DestinationService(base_url, destinations_url, scraper)

print("Starting data extraction... \n")

print("Getting airline data \n")
airline_data = airline_service.get_all_airlines(airline_service)
print("Saving airline data \n")
airline_service.save_airlines_to_csv(airline_service, airline_data)

print("Getting destination data \n")
destination_data = destination_service.get_all_destinations(destination_service)
print("Saving destination data \n")
destination_service.save_destinations_to_csv(destination_service, destination_data)

print("Downloading requested images \n")
destination_service.save_destination_image_data(destination_service)
airline_service.save_airline_image_data(airline_service)

print("Data extraction complete \n")
