from Pole import *
#main - logic
ship = Pole()
ship.set_pola_polozenia() 
while ship.trafienia != len(ship.pola_polozenia):
	choice = int(input("Podaj pole statku: "))
	ship.sprawdz(choice)
print("Zatopiłeś statek. Twój wynik to ", ship.trafienia)