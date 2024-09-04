import argparse
from appclima import get_weather
import csv
import json

def output_json(temperature, humidity, description):
    return json.dumps({
        "temperatura": temperature,
        "humedad": humidity,
        "descripcion": description
    }, ensure_ascii=False, indent=4)

def output_csv(temperature, humidity, description):
    output = f"temperatura,humedad,descripcion\n{temperature},{humidity},{description}\n"
    return output

def output_text(temperature, humidity, description):
    return f"Temperatura: {temperature}°C\nHumedad: {humidity}%\nDescripción: {description}"
#parser = argparse.ArgumentParser()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obtener el clima de una ciudad.")
    parser.add_argument("-c", "--ciudad", required=True, help="Ingresa -c y el nombre de tu ciudad para obtener los datos.")
    parser.add_argument("-f", "--formato", choices=["json", "csv", "text"], default="text", help="Agrega -f para elegir el formato de salida: json, csv, o text.")
    args = parser.parse_args()
    
    result = get_weather(args.ciudad)
    if result is not None:
        temperature, humidity, description = result                 
        
        if args.formato == "json":
            print(output_json(temperature, humidity, description))
        elif args.formato == "csv":
            print(output_csv(temperature, humidity, description))
        else:
            print(output_text(temperature, humidity, description))
