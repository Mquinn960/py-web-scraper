from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from services.logging_service import LoggingService

class Scraper():

    def __init__(self):
        self.logger = LoggingService

    @staticmethod
    def get_from_url(self, url):
        """ Make an HTTP Get to URL """
        try:
            with closing(get(url, stream=True)) as resp:
                if self.is_successful(self, resp):
                    return resp.content
                else:
                    return None
        
        except RequestException as e:
            self.logger.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None

    @staticmethod
    def is_successful(self, resp):
        """ Returns true if HTML found at the input URL """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)
