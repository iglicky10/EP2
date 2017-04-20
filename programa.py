
#INSPERMON
import os
import time
import sys
import json
import random
from random import randint

clear = lambda: os.system('cls')
clear()

#CLASSES E FUNÇÕES
class Alunos:
	def __init__(self,nome,ataque,defesa,vida,lvl):
		self.ataque = ataque
		self.defesa = defesa
		self.vida = vida
		self.nome = nome
		self.lvl = lvl

def batalhar(player,playerLVL,oponente,nomeSeuAluno):
	if player == "alunoMecatronica":
		player = alunoMecatronica
	elif player == "alunoMecanica":
		player = alunoMecanica
	elif player == "alunoComputacao":
		player = alunoComputacao
	clear()
	print("Você encontrou um {} ! O level dele é: {}".format(oponente.nome,oponente.lvl))
	time.sleep(4)

	if oponente.lvl > player.lvl:
		print("ATENÇÃO! O LEVEL DO ADVERSÁRIO É MAIOR DO QUE O SEU!")
		time.sleep(2)

	vidaOponente = oponente.vida
	suaVida = player.vida

	print("Prepare-se para a batalha!")
	time.sleep(2)

	#LOOP DA BATALHA
	while suaVida and vidaOponente > 0:
		clear()
		print("Pontos de vida de {}: {}".format(nomeSeuAluno,suaVida))
		print("Pontos de vida do {}: {}".format(oponente.nome,vidaOponente))

		atacarChoice = input("Você quer atacar (a) ou tentar fugir (f)? ")

		if atacarChoice == "f" or atacarChoice == "F":
			clear()
			print("Você fugiu da batalha com êxito!")
			time.sleep(2)
			return

		elif atacarChoice == "a" or atacarChoice == "A":
			clear()
			danoSeuAluno = abs((player.ataque + randint(-5,5) + randint(0,playerLVL)) -oponente.defesa)
			danoOponente = abs((oponente.ataque + randint (-5,5) + randint(0,oponente.lvl)) -player.defesa)
			vidaOponente = vidaOponente - danoSeuAluno
			suaVida = suaVida - danoOponente
			print("{} atacou e inflingiu {} de dano!".format(nomeSeuAluno,danoSeuAluno))
			time.sleep(2)
			print("O {} inimigo atacou e inflingiu {} de dano!".format(oponente.nome,danoOponente))
			time.sleep(3)

		else:
			print("Você precisa digitar (a) para atacar ou (f) para fugir!")

	if suaVida <= 0 and vidaOponente <=0:
		print("Foi um empate!")
		time.sleep(3)
		print("Ambos saíram feridos da batalha...")
		time.sleep(3)
		return

	elif suaVida <= 0:
		clear()
		print("Você perdeu a batalha...")
		time.sleep(1)
		print("Mas não se preocupe! Como esse jogo foi feito para se divertir, o seu Aluno já se recuperou e está pronto para continuar com você em sua jornada!")
		time.sleep(5)
		return

	elif vidaOponente <= 0: 
		clear()
		print("Parabéns! Você venceu a batalha!")
		time.sleep(2)
		print("Continue jogando para treinar seu aluno!")
		time.sleep(3)
		return


#DADOS
###INICIAIS
alunoMecatronica = Alunos("Name",10,5,30,1)
alunoMecanica = Alunos("Name",10,5,30,1)
alunoComputacao = Alunos("Name",10,5,30,1)
####NPCs
bixoADM = Alunos("Bixo de ADM",4,3,25,1)
bixoECONO = Alunos("Bixo de ECONOMIA",7,2,22,1)
bixoMECATRONICA = Alunos("Bixo de MECATRÔNICA",7,4,25,1)
bixoMECANICA = Alunos("Bixo de MECÂNICA",9,3,22,1)
bixoCOMPUTACAO = Alunos("Bixo de COMPUTAÇÃO",6,4,30,1)
veteranoADM = Alunos("Veterano de ADM",10,7,40,2)
veteranoECONO = Alunos("Veterano de ECONOMIA",15,4,36,2)
listaNPC = [bixoADM,bixoECONO,bixoMECATRONICA,bixoMECANICA,bixoCOMPUTACAO,veteranoADM,veteranoECONO]



logo = """

	   `:',` `:'',`   ,':`   :''';`  .:''''',`  .:'''''', .:''''';.   `:'';.     .;'':`    .;''''.    .:'',`   :':`
	   `'@;` .+@@+.   ;@'. `:#@@@#'. ,+@@@@@+;. ,+@@@@@@:`.+@@@@@@+.  ,+@@@:`    ;#@@+.  `:+#@@@@+;.  .+@@+.   '@'.
	   `'@;` .+#@@:`  ;@'. :#@;,,;+, ,#@;,,+@#: ,#@',,,,. .+@',,;#@'. ,#@##'.   .+##@+.  :#@':,,+@@:` .+##@:`  ;@'.
	   `'@;` .+#'+'.  ;@'. '@+.  `,` ,#@,  ,#@;`,#@:      .+@:  `'@#, ,#@'+#,   ,#++#+. .+@'.   .+@+. .+#'+'.  ;@'.
	   `'@;` .+#,'#,  ;@'. '@#:`     ,#@,  .+@;`,#@,      .+@:   ;@#, ,#@:'@;`  ;@;'@+. ;##:     ;#@, .+#,'#,  ;@'.
	   `'@;` .+#,,#'. ;@'. ,#@+':`   ,#@,  :#@: ,#@+''':` .+@:  .+@'. ,#@,;#+. `'#,'@+. '@+,     :#@: .+#,,#'. ;@'.
	   `'@;` .+#,`'#, ;@'. `,#@@#'.  ,#@+''#@+. ,#@@@@@+. .+@+''+#+,  :#@,,+#, :#+.;@+. '@+.     ,#@: .+#,`'#, ;@'.
	   `'@;` .+#, ,#'.;@'.  `.:+@@+. ,#@@@@@;.` ,#@;,,,.` .+@@@@@+,`  ,#@,`'@;`'@;`;@+. '@+.     ,#@: .+#, ,#'.;@'.
	   `'@;` .+#, `'@,;@'.    `,'#@;`,#@;,,,`   ,#@,      .+@',;##:`  ,#@, ;@+:+@, '@+. '@#,     :#@: .+#, `'#,'@'.
	   `'@;` .+#,  ,#;;#'.      .+@;`,#@,       ,#@,      .+@: `;@#,  ,#@, ,+@##'. '@+. ;#@,    `;@#, .+#,  ,#;;#'.
	   `'@;` .+#,  `'#+#'.`:.   ,+@;`,#@,       ,#@,      .+@:  .+@;` ,#@, `'@@@:  ;@+. .+@+.   :#@;` .+#,  `'#+#'.
	   `'@;` .+#,   ,#@@'.`'+'''+@+, ,#@,       ,#@+'''',`.+@:  `'@#, ,#@,  ;@@#,  ;@+.  :#@+'''#@'.  .+#,   ,##@'.
	   `'@;` .+#,   `'@@;``,+@@@@;.` :#@,       ,+@@@@@@;`.+@:`  ,#@'`:#@,  ,#@'`  '@#,  `,+@@@@#;.   .+@,   `'@@'`
	   `.,.  `,,`    .,,.   .:,,,`   `,,`       `,,,,,,,. `,,.   `,,,``,,`  `,,.   .,,`    .,,,,,`    `,,`    .,,.

	  Bem vindos ao Inspermon! Um jogo completamente inovador, nunca visto antes, onde você anda por um mundo virtual e 
	  batalha contra criaturas fantásticas pelo caminho (também conhecidas como alunos do Insper)!
	  Siga as instruções para jogar.
	  *** JOGUE COM O O CONSOLE EM TELA CHEIA ***

	  Jogo produzido por Rafael e Ariel - Engenharia Turma C - Insper 2017/1
"""
#INICIA O JOGO
while 1:
	print(logo)
	start = input("Digite 1 para começar ou 0 para fechar, e aperte enter: ")
	if start == "0":
		clear()
		quit()
	elif start == "1":
		clear()
		print("Vamos começar!")
		time.sleep(2)
		clear()
		break
	else:
		print("Você precisa digitar ou 0 ou 1!")
		time.sleep(3)
		clear()
#CARREGA UM LOAD OU INICIA UM NOVO SAVE
with open("save.json") as arquivoEntra:
	saveGeneral = json.load(arquivoEntra)
while 1:
	clear()
	loadSaveOption = input("Você deseja carregar seu save (s) ou iniciar uma nova jornada (n) ? ")
	if loadSaveOption == "s" or loadSaveOption == "S":
		print("Esta é sua lista de saves: ")
		for i in saveGeneral.keys():
			print(i)
		chooseSave = input("Qual save você quer carregar?")
		if chooseSave in saveGeneral:
				clear()
				saveAtual = saveGeneral[chooseSave]
				print("Loading")
				time.sleep(1)
				clear()
				print("Loading.")
				time.sleep(1)
				clear()
				print("Loading..")
				time.sleep(1)
				clear()
				print("Loading...")
				time.sleep(1)
				clear()
				break
		else:
			print("Esse save não existe!")
			time.sleep(3)

	elif loadSaveOption == "n" or loadSaveOption == "N":
		clear()
		for i in range(3,0,-1):
			print(i)
			time.sleep(1)
			clear()
		   #PEGAR OS DADOS DO JOGADOR
		clear()
		print("Bem vindo ao Kanto do Insper, o mundo de Inspermon!")
		time.sleep(5)
		clear()
		print("Meu nome é professor Samuel Carvalho e eu serei seu guia nessa jornada.")
		time.sleep(5)
		clear()
		print("Primeiramente vamos precisar saber algumas coisas sobre você.")
		time.sleep(5)
		clear()

		while 1:
			name = input("Digite seu nome: ")
			clear()
			sex = input("Você é menino (0) ou menina (1)? ")
			if sex == "0":
				sex = "Você é um menino"
			elif sex == "1":
				sex = "Você é uma menina"
			else:
				print("Como você não digitou nem 0 nem 1, você não será considerado nem um menino, nem uma menina")
				time.sleep(5)
				sex = "Você não é nem menino, nem menina"
			clear()
			print("Nome: ",name)
			print(sex)
			entrevistaConfirma = input("As informações estão corretas? SIM (s) | NÃO (n)")
			clear()
			if entrevistaConfirma == "S" or entrevistaConfirma=="s":
				saveName = input("Escolha um nome para seu novo save: ")
				saveGeneral[saveName] = {"name":name,"sex":sex,"alunos":{},"alunodex":[]}
				saveAtual = saveGeneral[saveName]
				with open("save.json","w") as arquivoSai:
					json.dump(saveGeneral,arquivoSai)
				clear()
				print("Muito bem! Você será levado para o lado de fora para começar sua Aventura!")
				time.sleep(5)
				clear()
				break

		if entrevistaConfirma == "S" or entrevistaConfirma=="s":
			break

	else:
		print("Você precisa digitar (s) ou (n)!")
		time.sleep(3)
		clear()

###########PROGRAMA PRINCIPAL#########################


###INTRO - ESCOLHE O POKEMON INICIAL
with open("save.json") as arquivoEntra:
	saveGeneral = json.load(arquivoEntra)

if loadSaveOption == "n" or loadSaveOption == "N":
	clear()
	print("Bem-vindo ao jardim do Kanto do Insper!")
	time.sleep(3)
	clear()
	print("Aqui você encontrará criaturas às quais chamamos de Alunos. Eles são perigosos e poderosos!")
	time.sleep(5)
	clear()
	print("Para te ajudar, tenho aqui 3 Alunos iniciais. Você pode escolher apenas um deles como seu Aluno inicial!")
	time.sleep(5)
	while 1:
		print("Bixo de MECATRÔNICA (0)")
		print("Bixo de MECÂNICA (1)")
		print("Bixo de COMPUTAÇÃO (2)")
		alunoInicialChoose = input("Qual deles você quer ter como seu inicial?")
		clear()
		if alunoInicialChoose == "0":
			print("Você escolheu um aluno de MECATRÔNICA para ser seu aluno inicial! Estes são os stats dele:")
			print("Ataque: {}".format(alunoMecatronica.ataque))
			print("Defesa: {}".format(alunoMecatronica.defesa))
			print("Vida: {}".format(alunoMecatronica.vida))
			print("Level: {}".format(alunoMecatronica.lvl))
			time.sleep(2)
			alunoMecatronica.nome = input("Digite qual será o nome do seu Aluno inicial: ")
			alunoInicial = alunoMecatronica
			saveAtual["alunos"] = {}
			saveAtual["alunos"] = {alunoMecatronica.nome:{"tipo":"alunoMecatronica","lvl":1}}
			saveGeneral[saveName] = saveAtual
			###COLOCA O ALUNO COM NOME NO SAVE
			with open("save.json","w") as arquivoSai:
				json.dump(saveGeneral,arquivoSai)
			clear()
			print("Muito bem! Agora você já pode ir passear para batalhar contra outros alunos!")
			time.sleep(4)
			print("Boa sorte!")
			time.sleep(2)
			break

		elif alunoInicialChoose == "1":
			print("Você escolheu um aluno de MECÂNICA para ser seu aluno inicial! Estes são os stats dele:")
			print("Ataque: {}".format(alunoMecanica.ataque))
			print("Defesa: {}".format(alunoMecanica.defesa))
			print("Vida: {}".format(alunoMecanica.vida))
			print("Level: {}".format(alunoMecanica.lvl))
			time.sleep(2)
			alunoMecanica.nome = input("Digite qual será o nome do seu Aluno inicial: ")
			alunoInicial = alunoMecanica
			saveAtual["alunos"] = {}
			saveAtual["alunos"] = {alunoMecanica.nome:{"tipo":"alunoMecanica","lvl":1}}
			saveGeneral[saveName] = saveAtual
			###COLOCA O ALUNO COM NOME NO SAVE
			with open("save.json","w") as arquivoSai:
				json.dump(saveGeneral,arquivoSai)
			clear()
			print("Muito bem! Agora você já pode ir passear para batalhar contra outros alunos!")
			time.sleep(4)
			print("Boa sorte!")
			time.sleep(2)
			break

		elif alunoInicialChoose == "2":
			print("Você escolheu um aluno de COMPUTAÇÃO para ser seu aluno inicial! Estes são os stats dele:")
			print("Ataque: {}".format(alunoComputacao.ataque))
			print("Defesa: {}".format(alunoComputacao.defesa))
			print("Vida: {}".format(alunoComputacao.vida))
			print("Level: {}".format(alunoComputacao.lvl))
			time.sleep(2)
			alunoComputacao.nome = input("Digite qual será o nome do seu Aluno inicial: ")
			alunoInicial = alunoComputacao
			saveAtual["alunos"] = {}
			saveAtual["alunos"] = {alunoComputacao.nome:{"tipo":"alunoComputacao","lvl":1}}
			saveGeneral[saveName] = saveAtual
			###COLOCA O ALUNO COM NOME NO SAVE
			with open("save.json","w") as arquivoSai:
				json.dump(saveGeneral,arquivoSai)
			clear()
			print("Muito bem! Agora você já pode ir passear para batalhar contra outros alunos!")
			time.sleep(4)
			print("Boa sorte!")
			time.sleep(2)
			break
		else:
			print("Você precisa escolher qual Aluno inicial você quer!")
			time.sleep(3)

else:
	#O saveAtual JA CARREGA OS VALORES DO SAVE
	print("Bem-vindo de volta ao jardim do Kanto do Insper!")
	time.sleep(3)


while 1: #LOOP INFINITO PRINCIPAL DO JOGO
	clear()
	print("Estes são seus alunos:")
	for i in saveAtual["alunos"].keys():
		print(i)
	alunoAtual = input("Digite com qual aluno você quer passear: ")
	while 1: #LOOP DO PASSEAR OU DORMIR
		clear()
		if alunoAtual in saveAtual["alunos"]:	
			clear()
			print("Passeando com {}".format(alunoAtual))
			passearOuDormir = input("Você quer passear (p), dormir (d) ou ver a Alunodex (a) ? ") ###PASSEAR OU DORMIR
			if passearOuDormir == "d" or passearOuDormir == "D":
				break

			elif passearOuDormir == "p" or passearOuDormir == "P":
				clear()
				print("Passeando")
				time.sleep(1)
				clear()
				print("Passeando.")
				time.sleep(1)
				clear()
				print("Passeando..")
				time.sleep(1)
				clear()
				print("Passeando...")
				time.sleep(1)
				clear()
				indexDoOponente = randint(0,len(listaNPC)-1)
				oponente = listaNPC[indexDoOponente]
				#CHAMA A FUNÇÃO BATALHAR
				batalhar(saveAtual["alunos"][alunoAtual]["tipo"],saveAtual["alunos"][alunoAtual]["lvl"],oponente,alunoAtual)
				clear()
				#CHAMA A FUNÇÃO CHECK DA ALUNODEX
				#saveAtual["alunodex"] = alunodexCheck(saveAtual["alunodex"],listaNPC,indexDoOponente)
				if str(indexDoOponente) not in saveAtual["alunodex"]:
					saveAtual["alunodex"].append(str(indexDoOponente))
					print("{} foi adicionado a sua Alunodex!".format(listaNPC[indexDoOponente].nome))
					time.sleep(3)
				with open("save.json","w") as arquivoSai:
					json.dump(saveGeneral,arquivoSai)

			elif passearOuDormir == "a" or passearOuDormir == "A":
				clear()
				print("Estes são os tipos de aluno que você já econtrou por ai: ") 
				for k in saveAtual["alunodex"]:
					print(listaNPC[int(k)].nome)
				time.sleep(6)

			else:
				print("Você precisa digitar (p) para passear ou (d) para dormir!")
				time.sleep(3)
		else:
			print("Escolha um Aluno que está na sua lista!")
			time.sleep(2)
			break	
	clear()
	if alunoAtual in saveAtual["alunos"]:
		continuarOuSair = input("Você quer sair do jogo? Para sair digite (s). Para continuar aperte ENTER")
		if continuarOuSair == "s" or continuarOuSair == "S":
			clear()
			print("Até a próxima, {}!".format(saveAtual["name"]))
			time.sleep(2)
			clear()
			exit()





