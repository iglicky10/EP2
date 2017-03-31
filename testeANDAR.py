#ANDAR
import os
import time
f1 = [1,1,1,1,1]
f2 = [1,0,0,0,1]
f3 = [1,0,8,0,1]
f4 = [1,0,0,0,1]
f5 = [1,1,1,1,1]
fx = [f1,f2,f3,f4,f5]
clear = lambda: os.system('cls')
clear()
for i in fx:
	print(i)
while 1:
	control = input('Para onde você quer ir? | d: Direita | e: Esquerda | f: Frente | a: Para traz')
	if control == "d":
		for i in fx:
			if sum(i) > 5:
				for k in range(len(i)):
					if i[k] == 8 and i[k+1] == 0:
						i[k+1] = 8
						i[k] = 0
						clear = lambda: os.system('cls')
						clear()
						break
					elif i[k] == 8 and i[k+1] == 1:
						print("Esse caminho está bloqueado!")
						time.sleep(1)
						clear = lambda: os.system('cls')
						clear()
	if control == "e":
		for i in fx:
			if sum(i) > 5:
				for k in range(len(i)):
					if i[k] == 8 and i[k-1] == 0:
						i[k-1] = 8
						i[k] = 0
						clear = lambda: os.system('cls')
						clear()
						break
					elif i[k] == 8 and i[k-1] == 1:
						print("Esse caminho está bloqueado!")
						time.sleep(1)
						clear = lambda: os.system('cls')
						clear()
	for i in fx:
		print(i)
						



