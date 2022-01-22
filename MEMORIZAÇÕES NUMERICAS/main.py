from random import randint
from operator import itemgetter
from time import sleep
import os
import menu

def linha ():
	print("=-="*20)

def titulo (txt):
	print("=-="*20)
	print(txt.center(60))
	print("=-="*20)


while True:
    try:
        arq = open ('Records.txt','r')
        lista = arq.readlines()
    except FileNotFoundError:
        arq = open ('Records.txt','a')
        arq = open ('Records.txt','r')
        lista = arq.readlines()
    arq.close()
    dicto = {}

    recodnum = []
    z = 0
    os.system('cls')
    modo=vez=continuar=opç=multiplayer=0
    multi4=4
    numero=[]
    cont=1
    cont2=rodada=0
    ok=False
    multi3=3
    colocados=[]
    jogadores=[]
    rank=[]
    okk=oi=sim=True
    sim=True
    menu.cadasmenu(['SOLO','MULTIPLAYER','RECORDS','COMO JOGAR','SAIR DO JOGO'],'JOGO DE DECORAR NUMEROS')

    while True:
        try:
            modo=int(input(menu.amarelo("digite o modo aqui: ")))
            if modo == 2:
                os.system('cls')
                while True:
                    try:
                        menu.cadasmenu(['2 players','3 players','4 players','voltar'],'MULTIPLAYER')
                        multiplayer=int(input('Escolha um modo: '))

                    except ValueError:
                        print(menu.vermelho("por favor, digite um numero"))
                        sleep(1)
                        os.system('cls')

                    else:
                        if multiplayer >= 1 and multiplayer <= 5:
                            print("continuando...")
                            if not multiplayer == 4:
                                sleep(1)
                            break
                        else:
                            print(menu.vermelho("por favor, digite um numero valido"))
                            sleep(1)
                            os.system('cls')




        except ValueError:
            print(menu.vermelho("por favor, digite um numero"))
            sleep(1)
            os.system('cls')
            menu.cadasmenu(['SOLO','MULTIPLAYER','RECORDS','COMO JOGAR','SAIR DO JOGO'],'JOGO DE DECORAR NUMEROS')
        else:
            if modo >= 1 and modo <= 5:
                break
            else:
                print(menu.vermelho("por favor, digite um numero valido"))
                sleep(1)
                os.system('cls')
                menu.cadasmenu(['SOLO','MULTIPLAYER','RECORDS','COMO JOGAR','SAIR DO JOGO'],'JOGO DE DECORAR NUMEROS')


    if modo == 1:
        while True:
            os.system('cls')
            cont+=1
            numero.append(randint(1,5))
            for a in range (0,len(numero)):
                titulo("1 player")
                print(f"{cont-1}° rodada")
                print(f"{a+1}°: {numero[a]}")
                sleep(0.9)
                os.system("cls")
            for b in range(0,len(numero)):
                titulo("1 player")
                print(f"{cont-1}° rodada")
                while True:
                    try:
                        os.system('cls')
                        titulo("1 player")
                        resp=int(input(f"digite o {b+1}° numero: "))
                    except ValueError:
                        print(menu.vermelho('Digite um numero porfavor.'))
                        sleep(1)
                        os.system('cls')
                    else:
                        break
                if resp == numero[b]:
                    print("ACERTOU! continuando...")
                    sleep(1)
                    os.system("cls")
                else:
                    ok=True
                    print(f"errou, a sequencia era {numero}, você aguentou até {cont-1} rodadas")
                    if len(lista) < 9:
                        while True:
                             try:
                                per = int(input('você pode entrar na lista de records, deseja entrar? [1/sim] [2/não]: '))
                             except ValueError:
                                 print(menu.vermelho('digite um numero'))
                             else:
                                if per != 1 and per != 2:
                                    print('porfavor, digite um numero valido')
                                    sleep(1)
                                    os.system("cls")
                                else:
                                    break
                        if per == 1:
                            nome = str(input('qual é seu nome? '))
                            arq = open ('Records.txt','a')
                            arq.write(f'{nome}\n{cont-1}'+'\n')
                            arq.close()
                    else:
                        arq = open ('Records.txt','r')
                        lista = arq.readlines()
                        for a in range (0,len(lista),2):
                            dicto[lista[a]] = lista[a+1]
                            recodnum.append(lista[a+1])
                        for a in range(0,len(recodnum)):
                            recodnum[a] = int(recodnum[a].replace('\n',''))
                        recodnum.sort(reverse = True)
                        if int(recodnum[4]) < cont-1:
                            while True:
                                try:
                                    per = int(input('você pode entrar na lista de records, deseja entrar? [1/sim] [2/não]: '))
                                except ValueError:
                                    print(menu.vermelho('digite um numero'))
                                else:
                                    if per != 1 and per != 2:
                                        print('porfavor, digite um numero valido')
                                        sleep(1)
                                        os.system("cls")
                                    else:
                                        break
                            if per == 1:
                                 nome = str(input('qual é seu nome? '))
                                 arq = open ('Records.txt','a')
                                 arq.write(f'{nome}\n{cont-1}'+'\n')
                                 arq.close()
                    break
            if ok:
                break
    elif modo == 2:
        os.system('cls')



        if multiplayer == 1:
            titulo("2 players")
            player1=str(input("nome do player 1: "))
            player2=str(input("nome do player 2: "))
            print("continuando...")
            sleep(1)
            os.system("cls")
            while True:
                    cont+=1
                    numero.append(randint(1,5))
                    for c in range(0,len(numero)):
                        if cont%2==0:
                            titulo(f"VEZ DO {player1}")
                        else:
                            titulo(f"VEZ DO {player2}")
                        print(f"{cont-1}° rodada")

                        print(f"{c+1}: {numero[c]}")
                        sleep(0.9)
                        os.system("cls")
                    for d in range(0,len(numero)):
                        if cont %2 == 0:
                            titulo(f"VEZ DO {player1}")
                        elif cont%2 == 1:
                            titulo(f"VEZ DO {player2}")
                        print(f"{cont-1}° rodada")
                        if oi:
                            while True:
                                try:
                                    os.system('cls')
                                    if cont %2 == 0:
                                        titulo(f"VEZ DO {player1}")
                                    elif cont%2 == 1:
                                        titulo(f"VEZ DO {player2}")
                                    resp = int(input(f"digite o {d+1}° numero:  "))
                                except ValueError:
                                    print(menu.vermelho('digite um numero, por favor'))
                                    sleep(1)
                                    os.system('cls')
                                else:
                                    break
                                
                        if resp == numero[d]:
                            print("ACERTOU! continuando...")
                            sleep(1)
                            os.system("cls")
                        else:
                            oi = False
                            ok = True
                            print(menu.ciano(f'a sequencia era {numero}'))
                            if cont%2 == 0:
                                print(menu.vermelho(f"o(a)  {player1} PERDEU!"))
                                print(menu.verde(f"o(a) {player2} VENCEU!\n"))
                                break
                            else:
                                ok = True

                                print(menu.vermelho(f"o {player2} PERDEU!"))
                                print(menu.verde(f"o {player1} VENCEU!\n"))
                                break
                    if ok:
                        break
        elif multiplayer == 2:
            os.system('cls')
            titulo("3 players")
            jogadores.append(str(input("qual é seu nome, player 1?: ")))
            jogadores.append(str(input("qual é seu nome, player 2?: ")))
            jogadores.append(str(input("qual é seu nome, player 3?: ")))
            print("continuando...")
            sleep(1)
            os.system("cls")
            while True:
                okk = True
                rodada+=1	
                numero.append(randint(1,5))

                for a in range(0,len(numero)):
                    titulo(f"VEZ DO {jogadores[vez%multi3]}")
                    print(f"{rodada}° rodada")
                    print(f"{a+1}° {numero[a]}")
                    sleep(0.9)
                    os.system("cls")

                for b in range(0,len(numero)):
                    titulo(f"VEZ DO {jogadores[vez%multi3]}")
                    print(f"{rodada}° rodada")
                    while True:
                        try:
                            os.system('cls')
                            titulo(f"VEZ DO {jogadores[vez%multi3]}")
                            resp=int(input(f"qual é o {b+1}° numero: "))
                        except ValueError:
                            print(menu.vermelho('digite um numero, por favor'))
                            sleep(1)
                            os.system('cls')
                        else:
                            break
                    
                    if resp == numero[b]:
                        print("ACERTOU! continuando...")
                        sleep(1)
                        os.system("cls")
                    else:
                        print(f"o {jogadores[vez%multi3]} foi derrotado...")
                        rank.append(jogadores[vez%multi3])
                        print("continuando...")
                        sleep(1)
                        os.system("cls")
                        del jogadores[vez%multi3]
                        multi3-=1
                        okk=False
                        break
                if multi3 == 1:
                    print(menu.ciano(f"a sequencia era {numero} "))
                    rank.append(jogadores[0])
                    menu.rank(rank)
                    print(f'o {jogadores[0]} venceu! ')
                    print("Fim de jogo\n")
                    break

                if okk:		
                    vez+=1
        elif multiplayer == 3:
            os.system('cls')
            titulo("4 players")
            jogadores.append(str(input("qual é seu nome, player 1?: ")))
            jogadores.append(str(input("qual é seu nome, player 2?: ")))
            jogadores.append(str(input("qual é seu nome, player 3?: ")))
            jogadores.append(str(input("qual é seu nome, player 4?: ")))
            print("continuando...")
            sleep(1)
            os.system("cls")

            while True:
                okk = True
                rodada+=1	
                numero.append(randint(1,5))

                for a in range(0,len(numero)):
                    titulo(f"VEZ DO {jogadores[vez%multi4]}")
                    print(f"{rodada}° rodada")
                    print(f"{a+1}° {numero[a]}")
                    sleep(0.9)
                    os.system("cls")

                for b in range(0,len(numero)):
                    titulo(f"VEZ DO {jogadores[vez%multi4]}")
                    print(jogadores)
                    print(f"{rodada}° rodada")
                    while True:
                        try:
                            os.system('cls')
                            titulo(f"VEZ DO {jogadores[vez%multi4]}")
                            resp=int(input(f"qual é o {b+1}° numero: "))
                        except ValueError:
                            print(menu.vermelho('digite um numero, por favor'))
                            sleep(1)
                            os.system('cls')
                        else:
                            break
                    if resp == numero[b]:
                        print("ACERTOU! continuando...")
                        sleep(1)
                        os.system("cls")
                    else:
                        print(f"o {jogadores[vez%multi4]} foi derrotado...")
                        rank.append(jogadores[vez%multi4])
                        print("continuando...")
                        sleep(1)
                        os.system("cls")
                        del jogadores[vez%multi4]
                        print(jogadores)
                        multi4-=1
                        okk=False
                        break
                if multi4 == 1:
                    print(f"a sequencia era {numero} ")
                    rank.append(jogadores[0])
                    menu.rank(rank)
                    print(f'o {jogadores[0]} venceu! ')
                    print("Fim de jogo\n")
                    break
                if okk:
                    vez+=1
                if not okk and rodada > 4:
                    vez-=1 
        elif multiplayer== 4:
            sim=False

    elif modo == 3:
        sim = False
        try:
            os.system('cls')
            titulo('TOP 5 MELHORES JOGADORES')
            arq = open ('Records.txt','r')
            lista = arq.readlines()
            for a in range (0,len(lista),2):
                la = lista[a].replace('\n','')
                lo = lista[a+1].replace('\n','')
                dicto[la] = int(lo)
                recodnum.append(lista[a+1])
            for nome,pontos in sorted(dicto.items(),key = itemgetter(1),reverse = True):
                z += 1
                print(f'{z}° {nome:<47} score: {pontos}')
                if z == 5:
                    break
        except FileNotFoundError:
            print('Arquirvo não encontrado ou excluido durante a execução do programa.\nvolte ao menu e teste essa opção novamente\nse o problema persistir, deixe seu feedback em https://github.com/purplecod/jogo-de-decorar-numeros-BETA-/discussions')
        
        input('\nAperte ENTER para continuar. ')

    elif modo == 4:
        os.system('cls')
        sim=False
        titulo('COMO JOGAR?')
        print("""A cada rodada, seu computador irár gerar um numero de uma 1 á 5 e adicionar-lo em uma lista de numeros, depois, o jogador tera que responder o primeiro numero ate o ultimo da lista na ordem.\na cada rodada a lista de numeros vai ficando maior e mais difícil de decorar\n\nse você for derrotado no modo solo o jogo irá guardar sua pontuação e fazer um Ranking de colocados com mais pontuação (ranking de colocados sera adicionados nas proximas versões)\n\nse um dos jogadores for derrotado no modo multiplayer, ele sera eliminado e não tera mais vez, a lista vai continuar crecendo e os jogadores restantes continuara jogando. O jogo só vai acabar quando sobrar um jogador, que sera o vitorioso.\n""")
        input('Aperte ENTER para continuar. ')
        os.system('cls')


    elif modo == 5:
        os.system('cls')
        print('Saindo...')
        sleep(2)
        break


    if sim:
        while True: 
            try:
                continuar=int(input('Deseja ir para o menu principal? [1 sim/ 2 não]  '))
            except ValueError:
                print(menu.vermelho('Por favor, digite um numero.'))
                sleep(1)
                os.system('cls')
            else:
                if continuar == 1 or continuar == 2:
                    break
                else:
                    print(menu.vermelho('Por favor, digite numero valido'))
                    sleep(1)
                    os.system('cls')
        if continuar== 2:
            break