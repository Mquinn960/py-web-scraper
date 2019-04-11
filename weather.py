from services.weather_service import WeatherService
from scraping.url_scraper import Scraper

scraper = Scraper

weather_service = WeatherService(scraper)

file_path = ""
filename = "weather.csv"

print("Starting weather service... \n")

weather_service.start_updating(weather_service, file_path, filename)

print("Weather service stopped \n")
