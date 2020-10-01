import requests
import datetime
import math
from tokens import *


# returns string of weather for the week
# changing lat an lon will change location of weather
def get_weather():
    base_url = "http://api.openweathermap.org/data/2.5/onecall?"
    lat = "37.3382"
    lon = "-121.8863"
    city_name = "San Jose"  # corresponds to the lat and lon
    complete_url = base_url + "lat=" + lat + "&lon=" + lon + "&units=imperial&appid=" + weatherKey.key
    response = requests.get(complete_url)
    x = response.json()

    # Get today's day and month
    today = datetime.date.today()
    today_month = today.month
    today_day = today.day
    today_weather = ""

    for day in x['daily']:
        date = day['dt']
        day_of_week = datetime.datetime.utcfromtimestamp(date)
        day_format = day_of_week.strftime('%b %d, %Y')

        temperature = str(math.floor(day['temp']['max']))
        description = str(day['weather'][0]['description'])
        if "clear" in description:
            description = "Clear skies! Go outside and enjoy the sun."
        elif "clouds" in description:
            description = "Cloudy today..."
        elif "rain" in description:
            description = "It's going to rain! Bring an umbrella!!"
        elif "drizzle" in description:
            description = "It's going to drizzle! Maybe bring an umbrella?"
        elif "thunder" in description:
            description = "Thunderstorms! Stay inside or bring an umbrella!"

        if today_day == day_of_week.day and today_month == day_of_week.month:
            today_weather = "Today in " + city_name + " it's " + temperature + "°F. " + description

        nice = day_format + " " + temperature + "°F. " + description
        print(nice)

    return today_weather


