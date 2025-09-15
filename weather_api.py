import secrets
import time
import urequests

def weather_api_call():
    print('fetching weather data')
    try:
        api_key = secrets.WEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/forecast?lat={secrets.LAT}&lon={secrets.LONG}&appid={api_key}&units=metric"
        r = urequests.get(url)
        print(r.status_code)
        if r.status_code == 200:
            return r
        else:
            return 0 # handle where data is passed to.
    except Exception as e:
        print('failed to get weather data:', e)
        

def parse_weather_api_response(response):
    print('test')
    l1 = []
    for i in response.content:
        l1.append(i)
        print(i, '\n')
        time.sleep(1)
