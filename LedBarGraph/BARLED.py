#coding:utf-8

#importation des bibliothèques 
from gpiozero import *
import time
import tkinter
from tkinter import messagebox
from tkinter import *

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

#Fonction de fermer programme
def Quit (): 
	exit()

#Afficher cette boite avant la fonction des lumieres
def Action():
	tkinter.messagebox.showinfo("Message Important", "Cliquez et regardez les lumières ...")


#Fonction un Led aprÈs l'autre
def Led1By1 ():
	print("Début 1 By 1") #On affiche dans la console
	Action()
	Led1.on()
	time.sleep(.5)                  
	Led1.off()
	time.sleep(.1)                 
	Led2.on()
	time.sleep(.5)                 
	Led2.off()
	time.sleep(.1)                   
	Led3.on()
	time.sleep(.5)                 
	Led3.off()
	time.sleep(.1)                   
	Led4.on()
	time.sleep(.5)                 
	Led4.off()
	time.sleep(.1)                   
	Led5.on()
	time.sleep(.5)                
	Led5.off()
	time.sleep(.1)                 
	Led6.on()
	time.sleep(.5)                 
	Led6.off()
	time.sleep(.1)                  
	Led7.on()
	time.sleep(.5)                  
	Led7.off()
	time.sleep(.1) 
	Led8.on()
	time.sleep(.5)                  
	Led8.off()
	time.sleep(.1) 
	Led9.on()
	time.sleep(.5)                  
	Led9.off()
	time.sleep(.1)   
	Led10.on()
	time.sleep(.5)                  
	Led10.off()
	time.sleep(.1)   
	Led9.on()
	time.sleep(.5)                 
	Led9.off()
	time.sleep(.1)   
	Led8.on()
	time.sleep(.5)                  
	Led8.off()
	time.sleep(.1)   
	Led7.on()
	time.sleep(.5)                  
	Led7.off()
	time.sleep(.1)   
	Led6.on()
	time.sleep(.5)                
	Led6.off()
	time.sleep(.1)   
	Led5.on()
	time.sleep(.5)                  
	Led5.off()
	time.sleep(.1)   
	Led4.on()
	time.sleep(.5)                  
	Led4.off()
	time.sleep(.1)   
	Led3.on()
	time.sleep(.5)                
	Led3.off()
	time.sleep(.1)   
	Led2.on()
	time.sleep(.5)               
	Led2.off()
	time.sleep(.1)   
	Led1.on()
	time.sleep(.5)               
	Led1.off()
	time.sleep(.1) 
	Led1.off()                
	Led2.off()                   
	Led3.off() 
	Led4.off()       
	Led5.off()     
	Led6.off()                 
	Led7.off()
	Led8.off()
	Led9.off() 
	Led10.off()  
	print ("Fin 1 By 1")		#On affiche dans la console

#Fonction alumer toute les lumieres et en éteindre 1 après l'autre
def Full1By1 ():
	print("Full1By1") #On affiche dans la console
	Action()
	Led1.on()                
	Led2.on()                   
	Led3.on()  
	Led4.on()       
	Led5.on()     
	Led6.on()                 
	Led7.on()
	Led8.on()
	Led9.on() 
	Led10.on()
	time.sleep(.8)  
	Led10.off()
	time.sleep(.5) 
	Led10.on()
	time.sleep(.1)  
	Led9.off()
	time.sleep(.5) 
	Led9.on()
	time.sleep(.1)  
	Led8.off()
	time.sleep(.5) 
	Led8.on()
	time.sleep(.1)  
	Led7.off()
	time.sleep(.5) 
	Led7.on()
	time.sleep(.1)  
	Led6.off()
	time.sleep(.5) 
	Led6.on()
	time.sleep(.1)  
	Led5.off()
	time.sleep(.5) 
	Led5.on()
	time.sleep(.1)  
	Led4.off()
	time.sleep(.5) 
	Led4.on()
	time.sleep(.1)  
	Led3.off()
	time.sleep(.5) 
	Led3.on()
	time.sleep(.1)  
	Led2.off()
	time.sleep(.5) 
	Led2.on()
	time.sleep(.1)  
	Led1.off()
	time.sleep(.5) 
	Led1.on()
	time.sleep(.1)  
	Led2.off()
	time.sleep(.5) 
	Led2.on()
	time.sleep(.1)  
	Led3.off()
	time.sleep(.5) 
	Led3.on()
	time.sleep(.1)  
	Led4.off()
	time.sleep(.5) 
	Led4.on()
	time.sleep(.1)  
	Led5.off()
	time.sleep(.5) 
	Led5.on()
	time.sleep(.1)  
	Led6.off()
	time.sleep(.5) 
	Led6.on()
	time.sleep(.1)  
	Led7.off()
	time.sleep(.5) 
	Led7.on()
	time.sleep(.1)  
	Led8.off()
	time.sleep(.5) 
	Led8.on()
	time.sleep(.1)  
	Led9.off()
	time.sleep(.5) 
	Led9.on()
	time.sleep(.1)  
	Led10.off()
	time.sleep(.5) 
	Led10.on()
	time.sleep(1) 
	Led1.off()                
	Led2.off()                   
	Led3.off()  
	Led4.off()        
	Led5.off()     
	Led6.off()                 
	Led7.off()
	Led8.off()
	Led9.off() 
	Led10.off()
	print ("Fin Full1By1")		#On affiche dans la console

#Fonction pour alumer lumière de l extérieur vers l intérieur
def ExCentre():
	print("ExCentre")
	Action()
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

#Fonction Tout les 3 programes 1 a la suite de lautre
def All ():
	print("All")
	Led1By1()
	Full1By1()
	ExCentre()

#ouvrir 2eme fenetre pour Dimmer
def Dim ():
	Fenetre1 = tkinter.Tk()
	Fenetre1.title("BAR LED") # titre de la fenetre
	Fenetre1.geometry("300x200") # dimention fenetre
	#afficher message dans fenetre
	Message = tkinter.Label(Fenetre1, text= "Regarder les lumières")
	Message.place(x=70, y=30)
	#fabriquer un Dimmer
	Dimmer = tkinter.Scale(Fenetre1, from_=0, to=10, tickinterval=1)
	Dimmer.place(x=40,y=80)
	
		#fonction qui va chercher les info du dimmeur, intégré a un condition en allument lumieres en timming 
	def Chek ():
		ValeurDim = Dimmer.get()
		time.sleep(.04)
		Dimmer.after(5,Chek)
		if ValeurDim == 0:
			print("0")
			Led1.off()                
			Led2.off()                   
			Led3.off()  
			Led4.off()       
			Led5.off()     
			Led6.off()                 
			Led7.off()
			Led8.off()
			Led9.off() 
			Led10.off()

		elif ValeurDim == 1:
			print("1")
			Led1.on()                
			Led2.off()                   
			Led3.off()
			Led4.off()            
			Led5.off()     
			Led6.off()                 
			Led7.off()
			Led8.off()
			Led9.off() 
			Led10.off()

		elif ValeurDim == 2:
			print("2")
			Led1.on()                
			Led2.on()                   
			Led3.off() 
			Led4.off()           
			Led5.off()     
			Led6.off()                 
			Led7.off()
			Led8.off()
			Led9.off() 
			Led10.off()
			
		elif ValeurDim == 3:
			print("3")
			Led1.on()                
			Led2.on()                   
			Led3.on() 
			Led4.off()           
			Led5.off()     
			Led6.off()                 
			Led7.off()
			Led8.off()
			Led9.off() 
			Led10.off()
			
		elif ValeurDim == 4:
			print("4")
			Led1.on()                
			Led2.on()                   
			Led3.on() 
			Led4.on()           
			Led5.off()     
			Led6.off()                 
			Led7.off()
			Led8.off()
			Led9.off() 
			Led10.off()

		elif ValeurDim == 5:
			print("5")
			Led1.on()                
			Led2.on()                   
			Led3.on() 
			Led4.on()        
			Led5.on()     
			Led6.off()                 
			Led7.off()
			Led8.off()
			Led9.off() 
			Led10.off()

		elif ValeurDim == 6:
			print("6")
			Led1.on()                
			Led2.on()                   
			Led3.on() 
			Led4.on()        
			Led5.on()     
			Led6.on()                 
			Led7.off()
			Led8.off()
			Led9.off() 
			Led10.off()

		elif ValeurDim == 7:
			print("7")
			Led1.on()                
			Led2.on()                   
			Led3.on() 
			Led4.on()        
			Led5.on()     
			Led6.on()                 
			Led7.on()
			Led8.off()
			Led9.off() 
			Led10.off()

		elif ValeurDim == 8:
			print("8")
			Led1.on()                
			Led2.on()                   
			Led3.on()  
			Led4.on()       
			Led5.on()     
			Led6.on()                 
			Led7.on()
			Led8.on()
			Led9.off() 
			Led10.off()

		elif ValeurDim == 9:
			print("9")
			Led1.on()                
			Led2.on()                   
			Led3.on()  
			Led4.on()       
			Led5.on()     
			Led6.on()                 
			Led7.on()
			Led8.on()
			Led9.on() 
			Led10.off()

		elif ValeurDim == 10:
			print("10")
			Led1.on()                
			Led2.on()                   
			Led3.on() 
			Led4.on()        
			Led5.on()     
			Led6.on()                 
			Led7.on()
			Led8.on()
			Led9.on() 
			Led10.on()

		else :
			pass
	
	#fermer tout lumiere et fermer 2eme fenetre
	def Fin ():
		Led1.off()                
		Led2.off()                   
		Led3.off() 
		Led4.off()        
		Led5.off()     
		Led6.off()                 
		Led7.off()
		Led8.off()
		Led9.off() 
		Led10.off()
		Fenetre1.destroy()
			
	#Bouton pour Fermer Fenetre1
	Bouton = tkinter.Button(Fenetre1, text="FERMER", command=Fin)
	Bouton.place(x=170,y=130)

	#débuter la fonction chek
	Chek()

	#Maintient de la fenetre en loop
	Fenetre1.mainloop()


#Création de la fenêtre
Fenetre = tkinter.Tk()
Fenetre.title("Programme de BAR LED") # Titre de la fenetre
Fenetre.geometry("575x220") #Dimention fenetre


 #Bouton pour 1 By 1
Ok = tkinter.Button(Fenetre, text="1 PAR 1", command=Led1By1)
Ok.place(x=10,y=30)

#Bouton pour Full 1 By 1 
Ok = tkinter.Button(Fenetre, text="Full 1 PAR 1 ", command=Full1By1)
Ok.place(x=210,y=30)

#Bouton pour ExCentre
Ok = tkinter.Button(Fenetre, text="Ext. vers Centre ", command=ExCentre)
Ok.place(x=410,y=30)

#Bouton pour All
Ok = tkinter.Button(Fenetre, text="Toute la gagne ", command=All)
Ok.place(x=200,y=90)

#Bouton pour Fermer
Ok = tkinter.Button(Fenetre, text="Dimmeur", command=Dim)
Ok.place(x=10,y=160)

#Bouton pour Fermer
Ok = tkinter.Button(Fenetre, text="QUITTER", command=Quit)
Ok.place(x=210,y=160)

#Maintient de la fenetre en loop
Fenetre.mainloop()
