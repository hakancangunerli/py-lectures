# api key = f6a538901dbee2dc6e2124217af10e60
# syntax  http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=f6a538901dbee2dc6e2124217af10e60 
# api.openweathermap.org/data/2.5/weather?q=[CITY]&]APPID=[apikey]


import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=f6a538901dbee2dc6e2124217af10e60&q='

city= input("name of the city:")
url= api_address+city
json_data= requests.get(url).json()


#description section 
weather_description=json_data['weather'][0]['description'] 



#temperature section
temperature=json_data['main']['temp'] 
temp_celcius= temperature-273.15


#windspeed section
windspeed= json_data['wind']['speed']

#country section
location= json_data['sys']['country'] 

#print section
print("your city is in " + location)
print(weather_description)
print( str(round(temp_celcius,2)) + " Celcius" )
print(   str (round(windspeed,2))  + " knots -> " , str(round((windspeed*1.852),2)) + " kilometres per hour/" , str(round((windspeed*1.15078),2)) + " miles per hour" )
