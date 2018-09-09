import re

from bs4 import BeautifulSoup
from models.destination import Destination

class DestinationService(object):

    def __init__(self, base_url, destinations_url, scraper):
        self.base_url = base_url
        self.destinations_url = destinations_url
        self.scraper = scraper

    @staticmethod
    def get_all_destinations(self):

        destinations_full_url = self.base_url + self.destinations_url

        airp_iata_code = ""
        name = ""
        img_url = ""
        img_name = ""
        owm_city_code = ""
        owm_name = ""

        destinations = list()
        raw_html = self.scraper.get_from_url(self.scraper, destinations_full_url)

        if raw_html is not None:
            html  = BeautifulSoup(raw_html, features="html.parser")
            table = html.find('table')
            rows = table.findAll('tr')
            
            for row in rows:

                cells = row.findAll('td')

                if len(cells) > 0:

                    # Get destination name
                    name = cells[0].find('a').getText().strip()

                    # Get destination airport IATA code
                    links = cells[2].findAll('a')
                    airp_iata_code = links[1]['href'][-3:]

                    # Get image url
                    destination_page_html = self.scraper.get_from_url(self.scraper, self.base_url + cells[0].find('a')['href'])
                    destination_page = BeautifulSoup(destination_page_html, features="html.parser")
                    main_style = destination_page.find('main')['style']
                    img_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', main_style)[0][:-2]

                    # Set image name
                    img_name = name.lower()

                destinations.append(Destination(
                    airp_iata_code,
                    name,
                    img_url,
                    img_name,
                    owm_city_code,
                    owm_name
                ))

            for destination in destinations:
                print(destination.name + "\n" + 
                      destination.airp_iata_code + "\n" +
                      destination.img_url + "\n" +
                      destination.img_name + "\n" +
                      destination.owm_city_code + "\n" +
                      destination.owm_name)

            return list(destinations)

        raise Exception('Error retrieving contents at {}'.format(self.base_url))
