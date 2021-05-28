from os import system
from tempo import Tempo
from personagem import Personagem


if __name__ == "__main__": ## FORÇA O PROGRAMA A RODAR APENAS NA MAIN
    tempo = Tempo()
    personagem = Personagem()

    # MENU PRINCIPAL
    while True:
        system('cls')
        print(tempo)
        print('')
        print('Escolha o que você quer fazer hoje:\n\n[ 1 ] Estudar\n[ 2 ] Trabalhar\n[ 3 ] Aumentar saúde\n[ 0 ] Ir dormir\n')
        opcao = int(input('Escolha uma opção -> '))
    
        # LAÇO DE REPETIÇÃO DOS MENUS SECUNDARIOS
        while True:
            # [ 1 ] ESTUDAR
            if opcao == 1:
                system('cls')
                print('O que você quer estudar?\n\n[ 1 ] HTML\n[ 2 ] Java\n[ 0 ] Menu principal\n')
                escolha = int(input('Escolha uma opção -> '))
                # [ 1 ] HTML
                if escolha == 1:
                    system('cls')
                    if tempo.horas < 21:
                        tempo.avancarTempo(60*3)
                        print(tempo)
                        personagem.estudarHtml()
                    else:
                        print(f'São {tempo.horas}:{tempo.minutos} horas.\n\nVocê não possui tempo suficiente para fazer esta atividade. Você precisa ir dormir.')
                        input('\nPressione ENTER para continuar ...')
                        break
                    input('\nPressione ENTER para continuar ...')
                # [ 2 ] JAVA
                elif escolha == 2:
                    system('cls')
                    if tempo.horas < 21:
                        personagem.estudarJava()
                        tempo.avancarTempo(60*3)
                        print(tempo)
                    else:
                        print(f'São {tempo.horas}:{tempo.minutos} horas.\n\nVocê não possui tempo suficiente para fazer esta atividade. Você precisa ir dormir.')
                        input('\nPressione ENTER para continuar ...')
                        break
                    input('\nPressione ENTER para continuar ...')
                elif escolha == 0:
                    system('cls')
                    break
                else:
                    print('** Escolha apenas entre as opções disponíveis **')
                    input('\nAperte ENTER para continuar...')
                    

            # [ 2 ] TRABALHAR
            elif opcao == 2:
                system('cls')
                if tempo.horas < 16:
                    personagem.trabalhar()
                    if personagem.trabalho == True:
                        tempo.avancarTempo(60*8)
                        print(tempo)
                        print(personagem)
                    else:
                        input('\nPressione ENTER para continuar ... ')
                        break
                else:
                    print(f'São {tempo.horas}:{tempo.minutos} horas.\n\nVocê não possui tempo suficiente para fazer esta atividade. Você precisa ir dormir.')
                    input('\nPressione ENTER para continuar ...')
                    break
                input('\nPressione ENTER para continuar ... ')
                break
            
            # AUMENTAR SAÚDE
            elif opcao == 3:
                system('cls')
                print('Escolha uma opção:\n\n[ 1 ] Comida saudável\n[ 2 ] Academia\n[ 3 ] Corrida ao ar livre\n[ 0 ] Menu Principal\n')
                escolha = int(input('Escolha uma opção acima -> '))
                # COMIDA SAUDÁVEL
                if escolha == 1:
                    personagem.comidaSaudavel()
                    tempo.avancarTempo(30)
                    print(tempo)
                    print(personagem)
                    input('\nDigite ENTER para continuar...')
                # ACADEMIA
                elif escolha == 2:
                    personagem.academia()
                    tempo.avancarTempo(60*2)
                    print(tempo)
                    print(personagem)
                    input('\nDigite ENTER para continuar...')
                # CORRIDA AO AR LIVRE
                elif escolha == 3:
                    personagem.corrida()
                    tempo.avancarTempo(60*2)
                    print(tempo)
                    print(personagem)
                    input('\nDigite ENTER para continuar...')
                # MENU PRINCIPAL
                elif escolha == 0:
                    break
                else:
                    system('cls')
                    print('\n** Escolha apenas entre as opções disponíveis! **')
                    input('\nDigite ENTER para continuar...')
            
            # IR DORMIR
            elif opcao == 0:
                tempo.dormir()
                print('')
                print(personagem)
                input('\nPressione ENTER para ACORDAR...')
                break
                
            else:
                system('cls')
                print('Digite apenas números das opções')
                input('\nDigite ENTER para continuar...')
                break
            


                    







        
    

    


