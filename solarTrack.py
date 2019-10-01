import pdb, numpy
from solarFunctions import solarFunctions
from objeto import objeto 

tiempo = 0.0;
dia = 1;
longitud = 57.5351404
latitud = 25.2843887
print('Inicio de simulacion')
sol = objeto()
panel = objeto()
panel.rotation(60.0,0.0,0.0)
t_ant = 0.0

while(1):
	if(dia > 365):
		break
	if(tiempo > 86400.0):
		tiempo = 0;
		print('dia: ',dia)
		dia = dia + 1;
		break
	if(tiempo - t_ant > 1):
		print('seg',tiempo)
		t_ant = tiempo
        tiempo = tiempo + 1e-6;
	#pdb.set_trace() 	
	tiempoSolar = solarFunctions.calcularTiempoSolar(tiempo,longitud, dia)
	altitudSolar = solarFunctions.calcularAltitudSolar(tiempoSolar/60.0,latitud,dia)
	azimuthSolar = solarFunctions.calcularAzimuthSolar(tiempoSolar/60.0,altitudSolar,latitud,dia)
	sol.rotation(altitudSolar,azimuthSolar,0)
	#print('prod', numpy.vdot(sol.getOrientacionZ(),-1*panel.getOrientacionY()))	
	#print('t - alt - az',[tiempo,altitudSolar,azimuthSolar])
print('Simulacion completa')
