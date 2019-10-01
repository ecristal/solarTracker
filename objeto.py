import numpy as np
import math

class objeto:
	orientacion = np.array([])
	def __init__(self):
		self.orientacion = np.array([[1,0,0],[0,1,0],[0,0,1]])
		self.refFrame =  np.array([[1,0,0],[0,1,0],[0,0,1]])
		
	def rotation(self,X,Y,Z):
		X = X*math.pi/180.0
		Y = Y*math.pi/180.0
		Z = Z*math.pi/180.0

		cx = math.cos(X)
		sx = math.sin(X)

		cy = math.cos(Y)
		sy = math.sin(Y)

		cz = math.cos(Z)
		sz = math.sin(Z)		

		xRotMat = np.array([[1,0,0],[0,cx,-sx],[0,sx,cx]])
		yRotMat = np.array([[cy,0,sy],[0,1,0],[-sy,0,cy]])
		zRotMat = np.array([[cz,-sz,0],[sz,cz,0],[0,0,1]])

		a = xRotMat.dot(self.refFrame)
		b = yRotMat.dot(a)
		c = zRotMat.dot(b)
		self.orientacion = c
		return c
	
	def getOrientacionX(self):
		return self.orientacion[:,0]

	def getOrientacionY(self):
		return self.orientacion[:,1]

	def getOrientacionZ(self):
		return self.orientacion[:,2] 	

	def toString(self):
		print('orientacion',self.orientacion)	
