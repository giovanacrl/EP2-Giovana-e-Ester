import json
from random import randint

def batalha (vida_jogador, poder_jogador, defesa_jogador,
             vida_oponente, poder_oponente, defesa_oponente):
    
    while vida_jogador >0 and vida_oponente>0:
        fugir=input("Batalha em andamento...você deseja:\n 1-continuar\n2-fugir")
        if fugir == 2:
            if poder_jogador>poder_oponente:
                print("Você não conseguiu fugir...")
            else:
                return "empate"
        else:
            vida_oponente= vida_oponente - ( poder_jogador - defesa_oponente)
            print("A vida do seu oponente é: {0}".format(vida_oponente))
    
        vida_jogador= vida_jogador - (poder_oponente - defesa_jogador)
        print("A sua vida é: {0}".format(vida_jogador))

        if vida_oponente == 0:
            return "ganhou"
        elif vida_jogador==0:
            return "perdeu"



# Le a lista de tipos de Inspermon.
with open('inspermons.json') as arquivo:
     inspermons = json.load(arquivo)
     
insperdex = []

while True:
    
    opcoes = int(input("Escolha uma das opções:\n 1-Dormir\n 2-Passear\n 3-Exibir Inspèrdex"))
    if opcoes==1:
        print("zZzZzZzZzZz")
        break
    elif opcoes == 3:
        print(insperdex)
    elif opcoes == 2:
        print("Escolha um Inspermon para voce:")
        for i in range(len(inspermons)):
            print("{0} : {1} (poder = {2}, vida = {3}, defesa = {4}"
                  .format(i,
                          inspermons[i]["nome"],
                          inspermons[i]["poder"],
                          inspermons[i]["vida"], 
                          inspermons[i]["defesa"]))
        escolha = int(input("Qual a sua escolha?"))
        voce = inspermons[escolha]
    
        i = randint(0,3)
        
        
        insperdex.append(inspermons[i])
        print("O seu adversário será: \n{0}".format(inspermons[i]["nome"]))
        print("poder = {0}".format(inspermons[i]["poder"]))
        print("vida = {0}".format(inspermons[i]["vida"]))
        print("defesa = {0}\n".format(inspermons[i]["defesa"]))
        
        print("Travada a batalha!")
        vida_jogador= inspermons[escolha]["vida"]
        poder_jogador= inspermons[escolha]["poder"]
        defesa_jogador= inspermons[escolha]["defesa"]

        vida_oponente= inspermons[i]["vida"]
        poder_oponente= inspermons[i]["poder"]
        defesa_oponente= inspermons[i]["defesa"]
    
        resultado = batalha (vida_jogador, poder_jogador, defesa_jogador,
             vida_oponente, poder_oponente, defesa_oponente)
    

        if resultado == "ganhou":
            print("Você ganhou!")
        elif resultado == "perdeu":
            print("Você perdeu!")
         
        
        
	
