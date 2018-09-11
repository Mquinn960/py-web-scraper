import re, os, json, csv

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
                    img_url = cells[2].find('img')['src'].replace("small", "big")
                
                    # Get airline IATA code
                    airl_iata_code = img_url.split("/")[-1][:-4]

                    # Get destination name
                    name = cells[0].getText().strip()

                    print("Parsing " + name)

                    # Set image name
                    img_name = airl_iata_code.lower()

                airlines.append(Airline(
                    airl_iata_code,
                    name,
                    img_url,
                    img_name
                ))

            return list(airlines)

        raise Exception('Error retrieving contents at {}'.format(self.base_url))

    @staticmethod
    def save_airlines_to_csv(self, airlines):
        output_folder = os.getcwd() + "\\output\\"

        with open(output_folder + "airlines" + ".csv",'w') as csv_output:
            writer = csv.writer(csv_output, dialect='excel')
            writer.writerow(airlines[0].__dict__.keys())

            for airline in airlines:
                airline = airline.__dict__
                writer.writerow(airline.values())

        return None

    @staticmethod
    def save_airline_image_data(models, model_type):
        # download each URL in list and create directory structure

        return None
        #print(models)