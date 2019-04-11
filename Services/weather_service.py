import re, os, json, csv, urllib, schedule, time, pyowm

from models.destination import Destination

class WeatherService(object):

    api_key = ""
    api_endpoint = "http://api.openweathermap.org/data/2.5/"

    def __init__(self, scraper, file_path, filename):
        self.scraper = scraper
        self.file_path = file_path
        self.filename = filename

    @staticmethod
    def start_updating(self):
        schedule.every(50).seconds.do(self.update_destinations(self))

        while True:
            schedule.run_pending()
            time.sleep(1)

    @staticmethod
    def update_destinations(self):
        destinations = self.get_destinations(self)

        for i in range (0, 50)
            city_id_request = api_endpoint + "weather?id={}&APPID={}".format(row[i], api_key)
            self.scraper.get_from_url

        for destination in destinations:
            print(destination.airp_iata_code)

    @staticmethod
    def get_destinations(self):
        input_folder = os.getcwd() + "\\input\\"
        destinations = list()
        
        with open(input_folder + "destinations" + ".csv",'r') as csv_input:

            reader = csv.reader(csv_input, delimiter=',')

            next(reader)

            for row in reader:
                
                destinations.append(Destination(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6]
                ))

        return destinations.sort(key=timestamp)

    @staticmethod
    def flatten_json(y):
    out = {}

        @staticmethod
        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
            else:
                out[name[:-1]] = x

        flatten(y)
        return out