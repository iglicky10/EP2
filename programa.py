#INSPERMON
import os
import time
import sys
clear = lambda: os.system('cls')
clear()
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

       Bem vindos ao Inspermon! Um jogo completamente inovador, nunca visto antes, onde você anda por um mundo virtual e encontra os Inspermons! 
       *** JOGUE COM O O CONSOLE EM TELA CHEIA *** 
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
		time.sleep(3)
		clear()
		for i in range(5,0,-1):
			print(i)
			time.sleep(1)
			clear()
		break
	else:
		print("Você precisa digitar ou 0 ou 1!")
		time.sleep(3)
		clear()
#PEGAR OS DADOS DO JOGADOR
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
	sex = int(input("Você é menino (0) ou menina (1)?" ))
	if sex == 0:
		sex = "Você é um menino"
	elif sex == 1:
		sex = "Você é uma menina"
	else:
		print("Como você não digitou nem 0 nem 1, você será considerado asexuado")
		time.sleep(5)
		sex = "Você é asexuado"
	clear()
	print("Nome: ",name)
	print(sex)
	entrevistaConfirma = input("As informações estão corretas? SIM (s) | NÃO (n)")
	clear()
	if entrevistaConfirma == "S" or entrevistaConfirma=="s":
		print("Muito bem! Você será levado para o lado de fora para começar sua Aventura!")
		time.sleep(5)
		break
