class LoggingService():

    @staticmethod
    def print(msg):
        """ Helper function to print messages to console """
        print("MESSAGE: " + msg)
 
    @staticmethod
    def log(error):
        """ Print errors """
        print("ERROR :" + error)
