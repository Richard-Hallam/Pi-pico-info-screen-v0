import secrets
import time
import urequests
import ujson


def weather_api_call():
    print('fetching weather data')
    try:
        api_key = secrets.WEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/forecast?lat={secrets.LAT}&lon={secrets.LONG}&appid={api_key}&units=metric"
        r = urequests.get(url)
        print(r.status_code)
        if r.status_code == 200:
            return r.text
        else:
            return 0 # handle where data is passed to.
    except Exception as e:
        print('failed to get weather data:', e)
        

def parse_weather_api_response(response):
    #data = json.loads(response)
    #print(data['list'])
    try:
        data = ujson.loads(response)
    except ValueError as e:
        print("error: ", e)
        
    
    list_of_lists = [
    [
        entry["dt_txt"],
        entry["main"]["temp"],
        entry["main"]["humidity"],
        entry["wind"]["speed"],
        entry["weather"][0]["description"]
    ]
    for entry in data["list"]
]
    return list_of_lists
