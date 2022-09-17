import requests
import os
import decimal


# Gets the weather info for the selected city from weatherbit
def weatherCall(city):
    # setting the end goal keys
    wanted_keys = ['high_temp', 'low_temp', 'app_max_temp', 'app_min_temp', 'pop',
                   'precip', 'rh', 'ts']

    # hardcoded city coordinates
    if city == 'lyh':
        lat = 37.4137536
        long = -79.1422464
        location = 'Lynchburg'
    if city == 'sav':
        lat = 32.0809263
        long = -81.0911768
        location = 'Savannah'

    # setting up API url
    url = f'https://api.weatherbit.io/v2.0/forecast/daily?lat={lat}&lon={long}&days=1' \
          f'&units=I&key={os.getenv("weather_api_key")}'

    # executing API call
    r = requests.get(url)
    data = r.json()
    data = data['data'][0]

    # filtering data to what was wanted and then rounding float data
    filtered = {x: data[x] for x in wanted_keys}
    for key, value in filtered.items():
        if type(value) == float:
            filtered[key] = round(decimal.Decimal(value), 2)

    # returning the appropriate info
    filtered['location'] = location
    return filtered
