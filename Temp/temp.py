import time
import board
import adafruit_dht

#Initialisation du sensor de temperature, sur la pin GPIO 17
dhtDevice = adafruit_dht.DHT11(board.D17, use_pulseio = False)

#Boucle de lecture / écriture de la température/humidité
while True:
    try:
         # Importations des données vers les variables
         temperature_c = dhtDevice.temperature
         temperature_f = temperature_c * (9 / 5) + 32
         humidity = dhtDevice.humidity
         print("Température: {:.1f} F / {:.1f} C    Humidité: {}% "
               .format(temperature_f, temperature_c, humidity))
        # DHT11 pas souvent fiable, message d'erreur en cas de problème
    except RuntimeError as error:     
         print("Erreur, veuillez réessayer")
         # Le DHT11 est pret au 2 secondes, définition d'un timer au 2 secondes.
    time.sleep(2.0)