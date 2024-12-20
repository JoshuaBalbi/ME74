import requests
import airtable as airtable

apikey = "453bfd727b6d487481e165717232003"
city = "Boston"

def req_infoapi(locale):
    url = f"http://api.weatherapi.com/v1/current.json?key={apikey}&q={locale}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # location = data['location']['name']
        # print(data['current'])
        temperature = data['current']['temp_f']
        humidity = data['current']['humidity']
        percipitation = data['current']['precip_in']
        uv = data['current']['uv']
        wind = data['current']['wind_mph']

        # print(f"Weather in {location}:")
        # print(f"Temperature: {temperature}°F")
        # print(f"Humidity: {humidity}")
        # print(f"UV: {uv}")
        # print(f"Percipitation: {percipitation} Inches")
        # print(f"Wind: {wind}")
        weather_data = [temperature, humidity, uv, percipitation, wind]
        return weather_data
    else:
        print("Error fetching data:", response.status_code)



#true is action
#false is remain the same
def decision(weather_array, status,winfo):
    if status == "Opened":
        return Do_we_close(weather_array,winfo)
    else:
        return Do_we_open(weather_array,winfo)
    
def Do_we_close(weather_array,winfo):
    temp = weather_array[0]
    pref_temp = winfo[0]
    temp_diff = pref_temp - temp

    humidity = weather_array[1]
    pref_hum = winfo[1]
    hum_diff = pref_hum - humidity
    
    percipitation = weather_array[3]

    UV = weather_array[2]
    pref_UV = winfo[2]
    UV_diff = pref_UV - UV
    
    wind = weather_array[4]
    pref_wind = winfo[4]
    wind_diff = pref_wind - wind
    
    if (percipitation > 0):
        print("rain")
        return True
    elif (temp_diff > 15):
        print("temperature")
        return True
    elif (UV_diff > 5):
        print("UV index")
        return True
    elif (hum_diff > 35):
        print("Humidity")
        return True
    elif (wind_diff > 13):
        print("wind")
        return False
    else:
        return False

    
def Do_we_open(weather_array,winfo):
    temp = weather_array[0]
    print(winfo)
    pref_temp = float(winfo[0])
    temp_diff = pref_temp - temp

    humidity = weather_array[1]
    pref_hum = int(winfo[1])
    hum_diff = pref_hum - humidity
    
    percipitation = weather_array[3]

    UV = weather_array[2]
    pref_UV = winfo[2]
    UV_diff = pref_UV - UV
    
    wind = weather_array[4]
    pref_wind = winfo[4]
    wind_diff = pref_wind - wind

    if (percipitation > 0):
        print("rain")
        return False
    elif (temp_diff > 15):
        print("temperature")
        return False
    elif (UV_diff  > 4):
        print("UV index")
        return False
    elif (hum_diff > 30):
        print("Humidity")
        return False
    elif (wind_diff > 10):
        print("Humidity")
        return False
    else:
        return True

def action(status, decision):
    if ((status == "Opened") and (decision)):
        airtable.post_info("Closed")
        status = "Closed"
        print("New status: " + status)
    elif ((status == "Closed") and (decision)):
        airtable.post_info("Opened")
        status = "Opened"
        print("New status: " + status)
    else:
        print("status remained the same: " + status)
    return status

def automate():
    status = airtable.req_info()
    winfo = airtable.req_weather_info()
    weather_Arr = req_infoapi(city)
    move = decision(weather_Arr, status,winfo,)
    status = action(status, move)
    return status


print(decision(req_infoapi("Boston"), airtable.req_info(),airtable.req_weather_info()))
# print(req_infoapi(city))
# print( type(airtable.req_weather_info()[0]))
# print(airtable.req_weather_info())