#OOP ver
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

#Get sheety data
data_manager                    = DataManager()
sheet_data                      = data_manager.get_destination_data()
search_flight_iata              = FlightSearch()
# pprint(sheet_data)

#Check if iataCode is empty in sheet_data
if sheet_data[0]['iataCode'] == '':
    # if empty, append iatacode from flight_search API and Update new sheet_data with iataCode into sheety
    for data in sheet_data:
        city                    = data['city']
        iatacode                = search_flight_iata.search_flight_iatacode(city)
        id                      = data['id']
        data_manager.add_iata_codes(iatacode, id)
else:
    # if filled in, fetch the flight data from Tequila-api.kiwi
    # print('filled in')

#Fetch the flight data from Tequila-api.kiwi
    for data in sheet_data:
        cheapest_flight         = FlightSearch()
        tequila_result          = cheapest_flight.search_flight(data['iataCode'], data['price'])
        # pprint(tequila_result)
        print("✈️Daylee's Flight Deal Finder ✈️")
        print(f"price search completed for: {data['city']}")

        from flight_data import FlightData
        if tequila_result['_results'] > 0:
            raw_start_date      = tequila_result['data'][0]['route'][0]['local_arrival']
            raw_return_date     = tequila_result['data'][0]['route'][1]['local_arrival']
            start_date          = raw_start_date.split("T")[0]
            return_date         = raw_return_date.split("T")[0]

            price               = tequila_result['data'][0]['price']
            origin_city         = tequila_result['data'][0]['cityCodeFrom']
            destination_city    = tequila_result['data'][0]['cityFrom']
            destination_airport = tequila_result['data'][0]['cityCodeTo']
            origin_airport      = tequila_result['data'][0]['cityTo']
            link                = tequila_result['data'][0]['deep_link']

            flight_data = FlightData(price, origin_city, origin_airport, destination_city, destination_airport,
                                     start_date, return_date, link)

        # print low price alert
            print(f'Price: {flight_data.price}')
            print(f'Origin City Name: {flight_data.origin_city}')
            print(f'Destination Airport IATA Code: {flight_data.destination_city}')
            print(f'Origin City Name: {flight_data.origin_airport}')
            print(f'Destination Airport IATA Code: {flight_data.destination_airport}')
            print(f'Outbound Date: {flight_data.out_date}')
            print(f'Inbound Date: {flight_data.return_date}')
            print(f'Booking Link: {flight_data.link}')
        else:
            print("No result")
        print("--------------------------------------------------------------")
