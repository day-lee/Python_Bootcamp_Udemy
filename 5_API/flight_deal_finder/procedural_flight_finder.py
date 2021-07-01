#Procedural Ver

import requests
from pprint import pprint
SHEETY_ENDPOINT = "https://api.sheety.co/aa4d1bc6b9a52d5ae93174997b4fe413/flightDeals/prices"

#Get sheety data
sheety_response = requests.get(url=SHEETY_ENDPOINT)
sheety_response.raise_for_status()
data            = sheety_response.json()
sheet_data      = data
# pprint(sheet_data)

#TEST: Check if iataCode is empty in sheet_data and append 'testing' into iataCode in sheet_data
# if sheet_data['prices'][0]['iataCode'] == '':
#     for data in sheet_data['prices']:
#         data['iataCode'] = 'testing'
#
#     print('------------------------')
#     pprint(sheet_data)

#Fetch iata code from tequila API
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/"
TEQUILA_APIKEY   = "BOqwdmxWFCBqflG5JMlVXpEsTaCJ1FZG"

for city in sheet_data['prices']:
    params      = {
                "term": city['city'],
                "location_types": "city"
    }
    headers     = {
                "apikey": TEQUILA_APIKEY
    }
    response    = requests.get(
                url=f"{TEQUILA_ENDPOINT}locations/query",
                params=params,
                headers=headers
    )
    response.raise_for_status()
    # print('tequila data printed')
    # pprint(response.json())
    data        = response.json()
    iata_code   = data['locations'][0]['code']
    # print(iata_code)

#Update new sheet_data with iataCode into sheety
    if city['iataCode'] == '':
        # print('Works')
        id     = city['id']
        params = {
                "price": {
                    "iataCode": iata_code
            }
        }
        headers = {
                "Content-Type": "application/json"
        }
        response = requests.put(
                url    =f'{SHEETY_ENDPOINT}/{id}',
                json   =params,
                headers=headers
        )
        response.raise_for_status()
        print(response.text)
    else:
        #iataCode in sheet is already filled out

#Fetch the flight data from Tequila-api.kiwi
        # import requests
        # from pprint import pprint

        from datetime import datetime, timedelta
        TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/"
        TEQUILA_APIKEY   = "BOqwdmxWFCBqflG5JMlVXpEsTaCJ1FZG"

        today            = datetime.now()
        TODAY            = str(today).split()[0]
        six_month_time   = today + timedelta(days=180)
        SIX_MONTH_TIME   = str(six_month_time).split()[0]

        FLY_FROM         = "SEL"
        FLY_TO           = city['iataCode']
        PRICE_TO         = city['price']

        params           = {
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
                            "limit": 1
        }
        headers         = {
                            "apikey": TEQUILA_APIKEY
        }
        response        = requests.get(
                            url    =f"{TEQUILA_ENDPOINT}v2/search",
                            params =params,
                            headers=headers
        )
        response.raise_for_status()
        print("✈️Daylee's Flight Deal Finder ✈️")
        print(f"Price search completed for: {city['city']}")
        # pprint(response.json())
        tequila_result_data = response.json()

        #Rrint low price alert
        if tequila_result_data['_results'] > 0:
            citycode_from   = tequila_result_data['data'][0]['cityCodeFrom']
            city_from       = tequila_result_data['data'][0]['cityFrom']
            citycode_to     = tequila_result_data['data'][0]['cityCodeTo']
            city_to         = tequila_result_data['data'][0]['cityTo']
            price           = tequila_result_data['data'][0]['price']

            raw_start_date  = tequila_result_data['data'][0]['route'][0]['local_arrival']
            raw_return_date = tequila_result_data['data'][0]['route'][1]['local_arrival']
            start_date      = raw_start_date.split("T")[0]
            return_date     = raw_return_date.split("T")[0]

            print(f'Price: {price}')
            print(f'Departure City Name: {city_from}')
            print(f'Departure Airport IATA Code: {citycode_from}')
            print(f'Arrival City Name: {city_to}')
            print(f'Arrival Airport IATA Code: {citycode_to}')
            print(f'Outbound Date: {start_date}')
            print(f'Inbound Date: {return_date}')

        else:
            print("No Result")
        print("--------------------------------------------------------------")


