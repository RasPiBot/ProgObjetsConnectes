# Importation des librairies

import time
import digitalio
import board
import adafruit_matrixkeypad

# Definitions des pin et touches

rows = [digitalio.DigitalInOut(x) for x in (board.D18, board.D23, board.D24, board.D25)]
cols = [digitalio.DigitalInOut(x) for x in (board.D10, board.D22, board.D27, board.D17)]
keys = ((1, 2, 3, 'A'),
        (4, 5, 6, 'B'),
        (7, 8, 9, 'C'),
        ('*', 0, '#', 'D'))

# Initialisation de la matrice

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

# Impression des touches a l'ecran

while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
        time.sleep(0.1)