import numpy as np 
import matplotlib.pyplot as plt
import random

g=9.8

V0=10*np.random.random(1000000)+35
tetha=np.pi/2.0*np.random.random(1000000)

sirvenV=np.copy(V0)

#hallar la distancia
def sacarDistancias(g, velocidad, angulo):
	
	d=((velocidad**2)*np.sin(2*angulo))/g
	return d
		

for i in range(len(V0)):
	sirven=0
	w=sacarDistancias(g, V0[i], tetha[i])
	if(56<=w<=66):
		sirven+=1
	else:	
		sirvenV[i]=0


Vel=[vel for vel in sirvenV if vel !=0]

plt.figure()
plt.title("Velocidades")
plt.hist(Vel, bins=100)
plt.savefig("1observacion.png")

#ahora con dos observaciones
tetha1=np.pi/2.0*np.random.random(len(Vel))
sirvenV1=np.copy(Vel)

for i in range(len(Vel)):
	sirven=0
	w=sacarDistancias(g, Vel[i], tetha1[i])
	if(110<=w<=120):
		sirven+=1
	else:	
		sirvenV1[i]=0

Vel1=[vel for vel in sirvenV1 if vel !=0]
plt.figure()
plt.title("Velocidades")
plt.hist(Vel1, bins=100)
plt.savefig("2observacion.png")

#ahora con 3 observaciones
tetha2=np.pi/2.0*np.random.random(len(Vel1))
sirvenV2=np.copy(Vel1)

for i in range(len(Vel1)):
	sirven=0
	w=sacarDistancias(g, Vel1[i], tetha2[i])
	if(26<=w<=36):
		sirven+=1
	else:	
		sirvenV2[i]=0

Vel2=[vel for vel in sirvenV2 if vel !=0]
plt.figure()
plt.title("Velocidades")
plt.hist(Vel2, bins=100)
plt.savefig("3observacion.png")

#4 observaciones
tetha3=np.pi/2.0*np.random.random(len(Vel2))
sirvenV3=np.copy(Vel2)

for i in range(len(Vel2)):
	sirven=0
	w=sacarDistancias(g, Vel2[i], tetha3[i])
	if(172<=w<=182):
		sirven+=1
	else:	
		sirvenV3[i]=0

Vel3=[vel for vel in sirvenV3 if vel !=0]
plt.figure()
plt.title("Velocidades")
plt.hist(Vel3, bins=100)
plt.savefig("4observacion.png")