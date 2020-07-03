class AccessToken:
    def __init__(self, token, tokenSecret):
        self.accessToken = token
        self.accessTokenSecret = tokenSecret


class APIkey:
    def __init__(self, apiKey, apiSecret):
        self.apiKey = apiKey
        self.apiSecret = apiSecret

class WeatherKey:
    def __init__(self, weatherKey):
        self.key = weatherKey


token = '1279127567866331136-2wloUkbYj8K851NGxlEHll7YgLRzXw'
token_secret = '3a4pom8bz2Vp1XTTlQvOenrrw1WO3tB5nwyhw8UiV0SXj'

accessToken = AccessToken(token, token_secret)

api_key = 'nWI6Sv0SCBx94daPRif88F5nq'
api_secret_key = '3P6DnCTk2CuOlNDvwfTtqpKFlFG4p4EYtuyQIBdkAYM0JXUeHI'
consumerAPI = APIkey(api_key, api_secret_key)

weather_key = '5ced4c2f9009f053832987673fc8ed03'

weatherKey = WeatherKey(weather_key)


