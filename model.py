import requests
import json
from datetime import datetime

class UserModel:
    def __init__(self,key):
        self.accessId = key

    def request(self):
        now = datetime.now()

        currentDate = now.strftime("%Y-%m-%d") # Formatér til"YYYY-MM-DD"

        params = {
        "start_date" : currentDate,
        "end_date": currentDate,
        "api_key" : self.accessId,
        }
        
        self.endPoint = f'https://api.nasa.gov/neo/rest/v1/feed'

        url = self.endPoint

        return requests.get(url,params=params)

    def fetchData(self):
            response = self.request()

            objectList = response.json()['near_earth_objects']

            return objectList
