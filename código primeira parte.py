#Código inicial
while True:
    opcoes=int(input("Escolha uma das opções: 1-Dormir ou 2-Passear"))
    if opcoes==1:
        print("zZzZzZzZzZz")
        break
    elif opcoes==2:
        voce=input("Escolha um Inspérmon para você:\n picaxu\n xamando\n pidijet")
        from random import randint
        bonecos=[
		"nome : picaxu\n poder : 20\n vida : 200\n defesa : 12",
	
		"nome : xamando\n poder : 25\n vida : 100\n defesa : 10",
		"nome : pidijet\n poder : 15\n vida : 300\n defesa : 10"]
        i = randint(0,3)
        

        print("O seu adversário será: \n {0}".format(bonecos[i]))
#Código batalha
    picaxu={"nome" : "picaxu", "poder" : 20, "vida" : 200,"defesa" : 12}
    xamando={"nome" : "xamando", "poder" : 25, "vida" : 100, "defesa" : 10}
    pidijet={"nome":"pidijet","poder":15,"vida":300,"defesa":10}
    if voce in picaxu:
        vida_jogador=picaxu["vida"]
        print(vida_jogador)
    elif voce in xamando:
        vida_jogador=xamando["vida"]
        print(vida_jogador)
    elif voce in pidijet:
        vida_jogador=pidijet["vida"]
        print(vida_jogador)
    if bonecos[i] in picaxu:
        vida_oponente=picaxu["vida"]
        print(vida_oponente)
    elif bonecos[i] in xamando:
        vida_oponente=xamando["vida"]
        print(vida_oponente)
    elif bonecos[i] in pidijet:
        vida_oponente=pidijet["vida"]
        print(vida_oponente)
         
        
        
	
