import requests
from datetime import datetime

api_key = '041581fcaf8365711c29bf93977d763b'
location = input("Enter city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#assigning the statements to the variables to store in text file
a = "-------------------------------------------------------------"
b = "Weather Stats for - {}  || {}".format(location.upper(), date_time)
c = "-------------------------------------------------------------"

d = "Current temperature   : {:.2f} deg C".format(temp_city)
e = "Current weather desc  : {}".format(weather_desc)
f = "Current Humidity      : {}{}".format(hmdt, ' %')
g = "Current wind speed    : {}{}".format(wind_spd ,' kmph')

#storing in text file line by line
with open('weather_report.txt','w') as r:
    r.write(a+"\n")
    r.write(b+"\n")
    r.write(c+"\n")
    r.write(d+"\n")
    r.write(e+"\n")
    r.write(f+"\n")
    r.write(g+"\n")
#Now everything is saved in the text file with name weather_report
