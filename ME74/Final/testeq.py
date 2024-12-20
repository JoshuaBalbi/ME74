import airtable as airtable
import automate as automate
import math


actual_weather = automate.req_infoapi("Boston")
# print(actual_weather)

prefered_weather = airtable.req_weather_info()
prefered_weather[0] = 55
# print(prefered_weather)
print(actual_weather[0])
print(prefered_weather[0])


# hum = (prefered_weather[1] - abs(prefered_weather[1] - actual_weather[1]))/prefered_weather[1]


# uv = (prefered_weather[2] - abs(prefered_weather[2] - actual_weather[2]))/12


# wind  = (prefered_weather[4] - abs(prefered_weather[4] - actual_weather[4]))/prefered_weather[4]

# eq = (-2.2*10**-5)*temp**3 + 0.001737*temp**2 - 0.048182*temp + 1 
# print(hum,wind,uv)

# eq2hot = hum/2 + wind/3 + uv/6

# eq2cold =  hum/3 + wind/2 + uv/6


#eq = (-2.2*10**-5)*temp**3 + 0.001737*temp**2 - 0.048182*temp + 1 
#eq = math.e ** (-1*(0.0288 * temp)) #range .60 to .87 to move onto second equation 


def tempeq(temp):
    return (-2.2*10**-5)*temp**3 + 0.001737*temp**2 - 0.048182*temp + 1 


def humeq(hum):
    return .6


def windeq(wind):
    return .6

def UVeq(UV):
    return .6


def openchecktemp(value,temp):
    if (value > .8):
        return 0
    elif (value < .65):
        return 1  
    else:
        if temp < 0:
            return 2 #humcheck()
        else:
            return 3 #windcheck()
        
def closechecktemp(value, temp):
    if (value < .6):
        return 0
    elif (value > .85):
        return 1
    else:
        if temp < 0:
            return 2 #humcheck()
        else:
            return 3  #windcheck()
        
def humcheck(hum,wind,UV):
    return humeq(hum)/2 + windeq(wind)/3 + UVeq(UV)/6
        
def windcheck(hum, wind,UV):
    return humeq(hum)/3 + windeq(wind)/2 + UVeq(UV)/6
        
def openchecksecond(val):
    if (val > .8) :
        return True
    else:
        return False

def closechecksecond(val):
    if (val < .7) :
        return True
    else:
        return False

def automationforopenq(weather_array,winfo):
    temp = weather_array[0]
    pref_temp = winfo[0]
    temp_diff = pref_temp - temp
    print(temp_diff )
    tempval= tempeq(abs(temp_diff))
    print(tempval)   
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

    decision = openchecktemp(tempval,temp_diff)
    print(decision )
    if (percipitation > 0):
        print("rain")
        return False
    elif (decision == 0):
        print("temp true")
        return True
    elif (decision == 1):
        print("temp false")
        return False
    elif (decision == 2):
        val = humcheck(hum_diff, UV_diff ,wind_diff )
        print("temp hum")
        return openchecksecond(val)
    else: 
        print("temp wind")
        val = windcheck(hum_diff, UV_diff ,wind_diff )
        return openchecksecond(val)
    



def automationforcloseq(weather_array,winfo):
    temp = weather_array[0]
    pref_temp = winfo[0]
    temp_diff = pref_temp - temp
    print(temp_diff )
    tempval= tempeq(abs(temp_diff))
    print(tempval)  

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
    decision = closechecktemp(tempval,temp_diff)
    print(decision )
    if (percipitation > 0):
        print("rain")
        return True
    elif (decision == 0):
        print("temp true")
        return True
    elif (decision == 1):
        print("temp false")
        return False
    elif (decision == 2):
        print("temp hum")
        val = humcheck(hum_diff, UV_diff ,wind_diff )
        return closechecksecond(val)
    else: 
        print("temp wind")
        val = windcheck(hum_diff, UV_diff ,wind_diff )
        return closechecksecond(val)

print("should we open?")
print(automationforopenq(actual_weather,prefered_weather))
print("should we close?")
print(automationforcloseq(actual_weather,prefered_weather))