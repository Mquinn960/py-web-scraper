from Services.airline_service import AirlineService
from Services.destination_service import DestinationService

airline_service = AirlineService

raw_html = scraper.get_from_url(scraper, 'https://www.edinburghairport.com/flights/destinations/a-to-z')

html = BeautifulSoup(raw_html, 'html.parser')

for i, li in enumerate(html.select('li')):
    print(i, li.text)

#logger.print(len(raw_html)) m