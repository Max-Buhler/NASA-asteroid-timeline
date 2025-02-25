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
        objectList = next(iter(objectList.values()))
        asteroids = []
        for asteroid in objectList:
            name = asteroid.get('name')
            link = asteroid.get('nasa_jpl_url')
            diameter = asteroid.get('estimated_diameter').get('meters').get('estimated_diameter_max')
            hazardous = asteroid.get('is_potentially_hazardous_asteroid')
            velocity = asteroid.get('close_approach_data')[0].get('relative_velocity').get('kilometers_per_second')
            time = asteroid.get('close_approach_data')[0].get('close_approach_date_full')
            time = time.split()[1]
            distance = asteroid.get('close_approach_data')[0].get('miss_distance').get('kilometers')
            
            newAsteroid = {
                "name": name,
                "link": link,
                "diamter_m": diameter,
                "hazardous": hazardous,
                "velocity_kms": velocity,
                "time": time,
                "distance_km": distance
            }
            asteroids.append(newAsteroid)

        return asteroids
