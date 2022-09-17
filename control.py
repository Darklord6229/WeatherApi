from sendNotification import sendNotifications
from weather_call import weatherCall
from database_connection import database_Upload


# getting weather info
weatherInfo = [weatherCall('lyh'), weatherCall('sav')]

# uploading weather info
for weather in weatherInfo:
    database_Upload(weather)

# sending notifications
sendNotifications()


