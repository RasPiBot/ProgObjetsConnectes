#coding:utf-8

#importation des bibliothèques 
from gpiozero import *
import time

"""
---LED utilisé---
LED #1 - GPIO-4  
LED #2 - GPIO-17 
LED #3 - GPIO-27 
LED #4 - GPIO-22 
LED #5 - GPIO-5  
LED #6 - GPIO-18 
LED #7 - GPIO-23 
LED #8 - GPIO-24 
LED #9 - GPIO-12 
LED #10- GPIO-16 
"""
Led1 = LED(4)
Led2 = LED(17)
Led3 = LED(27)
Led4 = LED(22)
Led5 = LED(5)
Led6 = LED(18)
Led7 = LED(23)
Led8 = LED(24)
Led9 = LED(12)
Led10 = LED(16)


print("ExCentre")
Led1.off()                
Led2.off()                   
Led3.off()         
Led5.off()     
Led6.off()                 
Led7.off()
Led8.off()
Led9.off() 
Led10.off()

Led5.on()
Led6.on()
time.sleep(.5)                  
Led5.off()
Led6.off()
time.sleep(.1)    

Led4.on()
Led7.on()
time.sleep(.5)                  
Led4.off()
Led7.off()
time.sleep(.1)

Led3.on()
Led8.on()
time.sleep(.5)                  
Led3.off()
Led8.off()
time.sleep(.1)

Led2.on()
Led9.on()
time.sleep(.5)                  
Led2.off()
Led9.off()
time.sleep(.1)

Led1.on()
Led10.on()
time.sleep(.5)                  
Led1.off()
Led10.off()
time.sleep(.1)

Led2.on()
Led9.on()
time.sleep(.5)                  
Led2.off()
Led9.off()
time.sleep(.1)

Led3.on()
Led8.on()
time.sleep(.5)                  
Led3.off()
Led8.off()
time.sleep(.1)

Led4.on()
Led7.on()
time.sleep(.5)                  
Led4.off()
Led7.off()
time.sleep(.1)

Led5.on()
Led6.on()
time.sleep(.8)                  
Led5.off()
Led6.off()
time.sleep(.1)

Led1.off()                
Led2.off()                   
Led3.off()         
Led5.off()     
Led6.off()                 
Led7.off()
Led8.off()
Led9.off() 
Led10.off()
print("Fin ExCentre")

