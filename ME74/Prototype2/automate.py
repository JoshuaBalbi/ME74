import requests
import airtable as airtable

apikey = "453bfd727b6d487481e165717232003"
city = "Boston"

def req_infoapi(locale):
    url = f"http://api.weatherapi.com/v1/current.json?key={apikey}&q={locale}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        temperature = data['current']['temp_f']
        humidity = data['current']['humidity']
        percipitation = data['current']['precip_in']
        uv = data['current']['uv']

        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°F")
        print(f"Humidity: {humidity}")
        print(f"Percipitation: {percipitation} Inches")
        print(f"UV: {uv}")
        weather_data = [temperature, humidity, percipitation, uv]
        return weather_data
    else:
        print("Error fetching data:", response.status_code)

#true is action
#false is remain the same
def decision(weather_array, status):
    if status == "Opened":
        return Do_we_close(weather_array)
    else:
        return Do_we_open(weather_array)
    
def Do_we_close(weather_array):
    temp = weather_array[0]
    humidity= weather_array[1]
    percipitation = weather_array[2]
    UV = weather_array[3]
    if (percipitation > 0):
        print("rain")
        return True
    elif (temp < 50):
        print("temperature")
        return True
    elif (temp > 80):
        print("temperature")
        return True
    elif (UV > 6):
        print("UV index")
        return True
    elif (humidity > 60):
        print("Humidity")
        return True
    else:
        return False
    
def Do_we_open(weather_array):
    temp = weather_array[0]
    humidity= weather_array[1]
    percipitation = weather_array[2]
    UV = weather_array[3]
    if (percipitation > 0):
        print("rain")
        return False
    if (temp < 55):
        print("temperature")
        return False
    if (temp > 77):
        print("temperature")
        return False
    if (UV > 5):
        print("UV index")
        return False
    if (humidity > 55):
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
    weather_Arr = req_infoapi(city)
    move = decision(weather_Arr, status)
    status = action(status, move)
    return status

