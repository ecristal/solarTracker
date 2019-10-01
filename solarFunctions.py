import math 

class solarFunctions:
	@staticmethod
	def calcularTiempoSolar(tiempo, longitud, dia):
		D = 360.0*(dia-81.0)/365.0
		D = D*math.pi/180
		ET = 9.87*math.sin(2*D) - 7.53*math.cos(D) - 1.5*math.sin(D)
		LSTM = 15.0*math.floor(longitud/15.0)
		TSP = (tiempo/60) + (4*(LSTM - longitud)) + ET
		return TSP*60.0
	
	@staticmethod
	def calcularH(minutos):
		H = ((minutos - 720.0)/4.0)*(math.pi/180.0)
		return H
	
	@staticmethod
	def calcularDelta(dia):
		delta = -23.45*math.sin((((dia + 284.0)/365)*360.0)*(math.pi/180))
		return delta
	
	@staticmethod
	def calcularAltitudSolar(minutos, latitud, dia):
		H = solarFunctions.calcularH(minutos) 
		delta = solarFunctions.calcularDelta(dia)
		altitud = math.asin(math.cos(latitud*math.pi/180.0)*math.cos(delta*math.pi/180.0)*math.cos(H) + math.sin(latitud*math.pi/180)*math.sin(delta*math.pi/180.0))
		return 180.0*altitud/math.pi
	
	@staticmethod
	def calcularAzimuthSolar(minutos,altitud,latitud,dia):
		H = solarFunctions.calcularH(minutos)
		delta = solarFunctions.calcularDelta(dia)
		a = math.sin(latitud*math.pi/180.0)*math.sin(altitud*math.pi/180.0) - math.sin(delta*math.pi/180.0)
		b = math.cos(altitud*math.pi/180.0)*math.cos(latitud*math.pi/180.0)
		return math.copysign(1,H)*(math.acos(a/b)*180.0/math.pi)
