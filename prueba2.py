import requests

# Obtén un token de MapQuest registrándote en https://developer.mapquest.com/
TOKEN = 'MtEFjPuyLmyJpl3K0FjWTcG8qgZ5H4BH'

def obtener_distancia_duracion(ciudad_origen, ciudad_destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key={TOKEN}&from={ciudad_origen}&to={ciudad_destino}'
    response = requests.get(url)
    data = response.json()

    distancia = data['route']['distance']
    duracion = data['route']['time']

    return distancia, duracion

def calcular_combustible(distancia_km):
    # Supongamos un consumo promedio de 8 litros por cada 100 km
    consumo_litros = distancia_km * 8 / 100
    return consumo_litros

def mostrar_narrativa(distancia_km, duracion_seg, consumo_litros):
    horas = duracion_seg // 3600
    minutos = (duracion_seg % 3600) // 60
    segundos = duracion_seg % 60

    print(f"Distancia: {distancia_km:.2f} km")
    print(f"Duración del viaje: {horas:02d}:{minutos:02d}:{segundos:02d}")
    print(f"Combustible requerido: {consumo_litros:.2f} litros")

# Solicitar ciudad de origen y destino al usuario
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

# Obtener distancia y duración del viaje
distancia, duracion = obtener_distancia_duracion(ciudad_origen, ciudad_destino)

# Calcular el consumo de combustible
consumo = calcular_combustible(distancia)

# Mostrar la narrativa del viaje
mostrar_narrativa(distancia, duracion, consumo)

# Salida del programa
salida = input("Presiona 'q' para salir: ")
if salida.lower() == 'q':
    exit()
