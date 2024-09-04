#importamo la librerias necesarias
import requests 
import json
from googletrans import Translator
def get_weather (city_name):
    API_KEY = "79871eea9ec4529e61d9ef8c2984233a"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    URL = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperatura = main['temp']
        humedad = main['humidity']
        report = data['weather']
        description = report[0]['description']
        # Traducir la descripción al español
        translator = Translator()
        translated_description = translator.translate(description, src='en', dest='es').text
        
        return temperatura, humedad, translated_description
    else:
        print("No se pudo obtener informacion de clima")
