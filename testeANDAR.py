#ANDAR
import os
import time
from msvcrt import getch
f1 = [1,1,1,1,1]
f2 = [1,0,0,0,1]
f3 = [1,0,8,0,1]
f4 = [1,0,0,0,1]
f5 = [1,1,1,1,1]
fx = [f1,f2,f3,f4,f5]
clear = lambda: os.system('cls')
clear()
def moveA(fx):
	for i in range(len(fx)):
		if sum(fx[i]) > 5:
			for k in range(len(fx[i])):
				if fx[i][k] == 8 and fx[i+1][k] == 0:
					fx[i+1][k] = 8
					fx[i][k] = 0
					clear()
					return fx
				elif fx[i][k] == 8 and fx[i+1][k] == 1:
					print("Esse caminho está bloqueado!")
					time.sleep(1)
					clear()
					return fx
def moveF(fx):
	for i in range(len(fx)):
		if sum(fx[i]) > 5:
			for k in range(len(fx[i])):
				if fx[i][k] == 8 and fx[i-1][k] == 0:
					fx[i-1][k] = 8
					fx[i][k] = 0
					clear()
					return fx
				elif fx[i][k] == 8 and fx[i-1][k] == 1:
					print("Esse caminho está bloqueado!")
					time.sleep(1)
					clear()
					return fx
def moveE(fx):
	for i in range(len(fx)):
		if sum(fx[i]) > 5:
			for k in range(len(fx[i])):
				if fx[i][k] == 8 and fx[i][k-1] == 0:
					fx[i][k-1] = 8
					fx[i][k] = 0
					clear()
					return fx
				elif fx[i][k] == 8 and fx[i][k-1] == 1:
					print("Esse caminho está bloqueado!")
					time.sleep(1)
					clear()
					return fx
def moveD(fx):
	for i in range(len(fx)):
		if sum(fx[i]) > 5:
			for k in range(len(fx[i])):
				if fx[i][k] == 8 and fx[i][k+1] == 0:
					fx[i][k+1] = 8
					fx[i][k] = 0
					clear()
					return fx
				elif fx[i][k] == 8 and fx[i][k+1] == 1:
					print("Esse caminho está bloqueado!")
					time.sleep(1)
					clear()
					return fx
for i in fx:
	print(i)
while 1:
	control = ord(getch())

	if control == 77: #D direita
		fx = moveD(fx)
	elif control == 75: #A esquerda
		fx = moveE(fx)
	elif control == 72: #W frente
		fx = moveF(fx)
	elif control == 80: #S atras
		fx = moveA(fx)

	clear()
	for i in fx:
		print(i)	



