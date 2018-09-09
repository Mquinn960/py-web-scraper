from bs4 import BeautifulSoup

from models.destination import Destination

class DestinationService(object):

    def __init__(self, base_url, scraper):
        self.base_url = base_url
        self.scraper = scraper

    @staticmethod
    def get_all_destinations(self):

        destinations = list()
        raw_html = self.scraper.get_from_url(self.scraper, self.base_url)

        if raw_html is not None:
            html  = BeautifulSoup(raw_html, features="html.parser")
            table = html.find('table')
            rows = table.findAll('tr')
            
            for row in rows:

                cells = row.findAll('td')

                if len(cells) > 0:

                    name = cells[0].find('a').getText().strip()

                    links = cells[2].findAll('a')

                    airp_iata_code = links[1]['href'][-3:]

                    destinations.append(Destination(
                        airp_iata_code,
                        name,
                        "img_url",
                        "img_name",
                        "owm_city_code",
                        "owm_name"
                    ))

            for destination in destinations:
                print(destination.name + " - " + destination.airp_iata_code)

            return list(destinations)

        raise Exception('Error retrieving contents at {}'.format(self.base_url))
