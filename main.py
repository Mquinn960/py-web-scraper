from services.airline_service import AirlineService
from services.destination_service import DestinationService
from services.file_helper_service import FileHelper

airline_service = AirlineService
destination_service = DestinationService
file_helper_service = FileHelper

print("Starting data extraction...")

print("Getting airline data")
airline_data = AirlineService.get_all_airlines
airline_images = AirlineService.get_all_airline_images

print("Saving airline data")
file_helper_service.save_local_csv(airline_data)
file_helper_service.save_local_image_data(airline_images)

print("Getting destination data")
destination_data = DestinationService.get_all_destinations
destination_images = DestinationService.get_all_destination_images

print("Saving destination data")
file_helper_service.save_local_csv(destination_data)
file_helper_service.save_local_image_data(destination_images)

print("Data extraction complete")