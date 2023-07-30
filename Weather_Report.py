import requests
import os #os is used to access the hidden information (API Key) which is saved at windows enviorment variable
from datetime import datetime
user_api = os.environ['My_API']
location = input("Enter the city name: ")
API_link = 'http://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+user_api
get_api_link = requests.get(API_link)
api_data = get_api_link.json()

if api_data['cod'] == '404':
    print('Invalid city: {}, Please check your city name'.format(location))
else:
    City_Temp = ((api_data['main']['temp']) - 273.15) #For convert the data in the celsius format
    date_time = datetime.now().strftime('%d %b %Y | %I:%M:%S %p')
    print('-----------------------------------------------------------------')
    print('Weather stats for - {} || {}: '.format(location.upper(), date_time))
    print('-----------------------------------------------------------------')
    print('Current Temperature of the city: {:.2f} deg C'.format(City_Temp))