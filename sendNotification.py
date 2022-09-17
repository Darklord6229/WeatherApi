import os
import time
from database_connection import database_Query
import requests


# function to send the desired weather info to a custom api endpoint
def sendNotifications():
    # setting up required parameters
    messages = []
    api_call = os.getenv('notif_url')
    keys = [os.getenv('notif_key_1'), os.getenv('notif_key_2')]
    data = [database_Query('Lynchburg'), database_Query('Savannah')]
    locations = ('Lynchburg', 'Savannah')

    # creating the message contents for each location, and appending it to the list
    for city in data:
        message = f"High Temp: {city['high_temp']}, Low Temp: {city['low_temp']}, Relative " \
                  f"Humidity: {city['rh']}, Chance of Rain: {city['pop']}%, " \
                  f"Date: {time.strftime('%m-%d-%Y ', time.localtime(city['ts']))}"
        messages.append(message)

    # working through the api keys and messages to then send off the api call
    for key in keys:
        for itr, message in enumerate(messages):
            url = api_call.format(key=key, city=locations[itr], cont=message)
            requests.post(url)
