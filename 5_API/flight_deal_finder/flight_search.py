import requests
from pprint import pprint
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/"
TEQUILA_API_KEY  = '-'

class FlightSearch:
    '''This class is responsible for talking to the Flight Search (tequila-kwi) API.'''
    def search_flight_iatacode(self, city):
        '''return iatacode fetched from tequila API'''
        params          = {
                        "term": city,
                        "location_types": "city"
        }
        headers         = {
                        "apikey": TEQUILA_API_KEY
        }
        response        = requests.get(
                        url=f"{TEQUILA_ENDPOINT}locations/query",
                        params=params,
                        headers=headers
        )
        response.raise_for_status()
        # print('tequila data printed')
        pprint(response.json())
        data            = response.json()
        iata_code       = data['locations'][0]['code']
        return iata_code
        # print(iata_code)

    def search_flight(self, fly_to, price_to):
        '''return cheapest flight data from tequila API'''
        today          = datetime.now()
        TODAY          = str(today).split()[0]
        six_month_time = today + timedelta(days=180)
        SIX_MONTH_TIME = str(six_month_time).split()[0]

        FLY_FROM       = "SEL"
        FLY_TO         = fly_to  #city['iataCode']
        PRICE_TO       = price_to  #city['price']

        params         = {
                        "fly_from": FLY_FROM,
                        "fly_to": FLY_TO,
                        "dateFrom": TODAY,
                        "dateTo": SIX_MONTH_TIME,
                        "nights_in_dst_from": 5,
                        "nights_in_dst_to": 30,
                        "flight_type": "round",
                        "curr": "KRW",
                        "max_stopovers": 0,
                        "price_to": PRICE_TO,  # historically low price
                        "limit": 5
        }
        headers       = {
                        "apikey": TEQUILA_API_KEY
        }
        response      = requests.get(
                        url    =f"{TEQUILA_ENDPOINT}v2/search",
                        params =params,
                        headers=headers
        )
        response.raise_for_status()
        tequila_result_data = response.json()
        return tequila_result_data



