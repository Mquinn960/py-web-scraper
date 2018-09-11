import re
import os
import json

from bs4 import BeautifulSoup
from models.airline import Airline

class AirlineService(object):

    def __init__(self, base_url, airlines_url, scraper):
        self.base_url = base_url
        self.airlines_url = airlines_url
        self.scraper = scraper

    @staticmethod
    def get_all_airlines(self):

        airlines_full_url = self.base_url + self.airlines_url

        airl_iata_code = ""
        name = ""
        img_url = ""
        img_name = ""

        airlines = list()
        raw_html = self.scraper.get_from_url(self.scraper, airlines_full_url)

        if raw_html is not None:

            html  = BeautifulSoup(raw_html, features="html.parser")
            table = html.find('table')
            rows = table.findAll('tr')
            
            for row in rows:

                cells = row.findAll('td')

                if len(cells) > 0:

                    # Get image url
                    img_url = cells[2].find('img')['src']
                
                    # Get airline IATA code
                    airl_iata_code = re.find('/[\w-]+\.(jpg)/g', img_url)[:-4]

                    # Get destination name
                    name = cells[0].getText().strip()

                    # Set image name
                    img_name = airl_iata_code.lower()

                airlines.append(Airline(
                    airl_iata_code,
                    name,
                    img_url,
                    img_name
                ))

                for airline in airlines:
                    print (airl_iata_code + "\n" +
                           name + "\n" +
                           img_url + "\n" +
                           img_name)

            return list(airlines)

        raise Exception('Error retrieving contents at {}'.format(self.base_url))
