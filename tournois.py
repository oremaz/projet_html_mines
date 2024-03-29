import requests
from bs4 import BeautifulSoup
import json

def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal_degrees = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def convert_coordinates(dms_latitude, dms_longitude):
    # Diviser les parties de la coordonnée en degrés, minutes, secondes et direction
    latitude_parts = dms_latitude.replace('°', '').split(' ')
    longitude_parts = dms_longitude.replace('°', '').split(' ')

    # Extraire les parties numériques et la direction
    lat_deg, lat_min, lat_sec, lat_dir = int(latitude_parts[0]), int(latitude_parts[1]), float(latitude_parts[2]), latitude_parts[3]
    lon_deg, lon_min, lon_sec, lon_dir = int(longitude_parts[0]), int(longitude_parts[1]), float(longitude_parts[2]), longitude_parts[3]

    # Convertir en décimal
    latitude = dms_to_decimal(lat_deg, lat_min, lat_sec, lat_dir)
    longitude = dms_to_decimal(lon_deg, lon_min, lon_sec, lon_dir)

    return [latitude, longitude]

# Coordonnées des tournois considérés (source : Wikipédia)
dms_latitude_sudfr = "43° 34' 24\" N"
dms_longitude_sudfr = "3° 57' 06\" E"
coordinates_sudfr = convert_coordinates(dms_latitude_sudfr, dms_longitude_sudfr)

dms_latitude_op13 = "43° 16′ 14\" N"
dms_longitude_op13 = "5° 24′ 05\" E"
coordinates_op13 = convert_coordinates (dms_latitude_op13,dms_longitude_op13)

dms_latitude_lyon = "45° 46′ 50\" N"
dms_longitude_lyon = "4° 51′ 15\" E"
coordinates_lyon = convert_coordinates (dms_latitude_lyon,dms_longitude_lyon)

dms_latitude_metz = "49° 06′ 31\" N"
dms_longitude_metz = "6° 11′ 03\" E"
coordinates_metz = convert_coordinates (dms_latitude_metz,dms_longitude_metz)

# URL du site avec le calendrier des tournois ATP 250
url = "https://www.fft.fr/node/2101"

# Faire la requête HTTP
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Utiliser BeautifulSoup pour extraire les informations HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraire les dates des tournois ATP 250
    atp250_tournois = []
    atp250_villes = []
    atp250_dates = []
    atp250_dates_elements = soup.select("div.field--name-field-date-debut div.field-content, div.field--name-field-date-fin div.field-content")
    for element in atp250_dates_elements:
        atp250_dates.append(element.text.strip())
    atp250_elements2 = soup.select("div.field--name-field-tournoi div.field-content")
    for element in atp250_elements2:
        # La colonne "tournoi" est sous la forme "Nom du tournoi - Ville du tournoi"
        # Nous allons séparer le nom et la ville en utilisant le séparateur " - "
        tournament_info = element.text.strip().split(" - ")
        
        # Ajouter le nom du tournoi à la liste des tournois
        atp250_tournois.append(tournament_info[0])
        
        # Ajouter la ville du tournoi à la liste des villes
        atp250_villes.append(tournament_info[1])

    # Coordonnées fictives pour illustrer l'exemple
    atp250_coordinates = [coordinates_sudfr, coordinates_op13, coordinates_lyon, coordinates_metz]
    
    # Coordonnées pour Masters 1000 et Grand Chelem
    dms_latitude_mm = "48° 50′ 19\" N", 
    dms_longitude_mm = "2° 22′ 43\" E"
    masters1000_coordinates = [dms_latitude_mm,dms_longitude_mm]  

    dms_latitude_gs = "48° 50′ 50\" N"
    dms_longitude_gs = "2° 14′ 57\" E"
    grandSlam_coordinates = [dms_latitude_gs,dms_longitude_gs] 

    # Nom pour Masters 1000 et Grand Chelem
    masters1000_name = "Rolex Paris Masters"
    grandSlam_name = "Roland-Garros"

    # Villes pour Masters 1000 et Grand Chelem
    masters1000_ville = "Paris"
    grandSlam_ville = "Paris"

    # Dates pour Masters 1000 et Grand Chelem
    masters1000_dates = "26/10/2024 - 3/11/2024"
    grandSlam_dates = "26/05/2024 - 09/06/2024"

    # Créer le dictionnaire avec les données
    data = {
        "atp250": [{"coordinates": coord, "nom" : nom, "ville" : lieu, "date": date} for coord, nom, lieu, date in zip(atp250_coordinates, atp250_tournois, atp250_villes, atp250_dates)],
        "masters1000": {"coordinates": masters1000_coordinates, "nom" : masters1000_name, "ville" : masters1000_ville, "date": masters1000_dates},
        "grandSlam": {"coordinates": grandSlam_coordinates, "nom" : grandSlam_name, "ville" : grandSlam_ville, "date": grandSlam_dates}
    }

    # Imprimer le dictionnaire JSON pour vérification
    with open('tennis_tournaments.json', 'w') as json_file:
        json.dump(data, json_file)

    print("JSON généré avec succès.")
else:
    print("La requête a échoué. Code de statut :", response.status_code)

