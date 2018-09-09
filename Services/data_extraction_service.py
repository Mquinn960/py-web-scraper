class DataExtractionService():

    def __init__(self, airline_service, destination_service):
        self.airline_service = airline_service
        self.destination_service = destination_service

    @staticmethod
    def save_local_data():
        print("saved all local data")

    def save_airline_data():
        print("saved all airline data locally")

    def save_destination_data():
        print("saved all desintation data locally")
    