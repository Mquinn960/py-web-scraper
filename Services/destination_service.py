import re
import os
import json

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

            with open("city.list.json", encoding="utf8") as city_list_raw:
                city_list_json = json.loads(city_list_raw.read())

            html  = BeautifulSoup(raw_html, features="html.parser")
            table = html.find('table')
            rows = table.findAll('tr')
            
            for row in rows:

                cells = row.findAll('td')

                if len(cells) > 0:

                    # Set destination name
                    name = cells[0].find('a').getText().strip()

                    # Set destination airport IATA code
                    links = cells[2].findAll('a')
                    airp_iata_code = links[1]['href'][-3:]

                    # Set image url
                    destination_page_html = self.scraper.get_from_url(self.scraper, self.base_url + cells[0].find('a')['href'])
                    destination_page = BeautifulSoup(destination_page_html, features="html.parser")
                    main_style = destination_page.find('main')['style']
                    img_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', main_style)[0][:-2]

                    # Set image name
                    img_name = name.lower()

                    # Set Open Weather Map city code
                    # Set Open Weather Map name
                    for city in city_list_json:
                        if city['name'] == name:
                            owm_city_code = str(city['id'])
                            owm_name = city['name']
                        else:
                            owm_name = ""

                destinations.append(Destination(
                    airp_iata_code,
                    name,
                    img_url,
                    img_name,
                    owm_city_code,
                    owm_name
                ))

            return list(destinations)

        raise Exception('Error retrieving contents at {}'.format(self.base_url))
