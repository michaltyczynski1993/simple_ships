import random
class Pole(object):
	def __init__(self, pola_polozenia=[], trafienia = 0 ):
		self.pola_polozenia= pola_polozenia
		self.trafienia = trafienia
	
	def set_pola_polozenia(self):
		x = random.randint(1,5)
		pola = [x, x+1, x+2]
		self.pola_polozenia = pola
	
	def sprawdz(self, choice):
		if choice in self.pola_polozenia:
			print("trafiony")
			self.trafienia += 1
		else:
			print("Pudło")