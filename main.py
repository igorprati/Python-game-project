from os import system
from tempo import Tempo
from personagem import Personagem
from personagem import tempo # importa a variável tempo instanciada em Tempo()
from time import sleep

if __name__ == "__main__":  # FORÇA O PROGRAMA A RODAR APENAS NA MAIN
    personagem = Personagem()

    # DEFINE A FUNÇÃO TUTORIAL
    def tutorial():
        system('cls')
        print('------------- TUTORIAL DO PROGRAMA -------------')
        print('''
        Este é um simulador de rotina diária da vida de uma
        pessoa. Para começar, você poderá escolher seus atri-
        butos que mudarão o rumo da sua história.
        ''')
        input('Aperte ENTER para continuar o tutorial...\n')
        system('cls')
        print('------------- TUTORIAL DO PROGRAMA -------------\n')
        print(tempo)
        personagem.status()
        print('''
        Acima você encontra sua barra de status. Nela, você
        encontra o dia, hora atual, sua saúde e o dinheiro
        que você carrega na carteira.\n''')
        input('Aperte ENTER para continuar o tutorial...\n')
        system('cls')
        print('------------- TUTORIAL DO PROGRAMA -------------\n\n')
        print(
            '[ 1 ] Estudar\n[ 2 ] Trabalhar\n[ 3 ] Aumentar energia\n[ 4 ] Banco\n[ 0 ] Ir dormir')
        print('''
        Este é o menu principal. É nele que você poderá es-
        colher suas ações teclando o numero correspondente
        de cada item.''')
        input('\nAperte ENTER para continuar o tutorial...\n')
        system('cls')
        print('------------- TUTORIAL DO PROGRAMA -------------\n')
        print('''
        A cada ação tomada no jogo, existem consequências
        benéficas e maléficas para seu personagem. Por exem-
        plo: ao ir à ACADEMIA você recupera sua energia, po-
        rém perde dinheiro e tempo. Você precisa escolher
        suas ações com cuidado e inteligência.''')
        input('\nAperte ENTER para continuar o tutorial...\n')
        system('cls')
        input('Vamos começar?\n\nAperte ENTER para começar o jogo! ->')

    # MENU PRINCIPAL
    while True:
        personagem.menuPrincipal()
        opcao = int(input('Escolha uma opção -> '))

        # LAÇO DE REPETIÇÃO DOS MENUS SECUNDARIOS
        while True:
            # [ 1 ] ESTUDAR
            if opcao == 1:
                if tempo.horas <= 21:  ## Usuário só poderá estudar caso haja tempo necessário para a realização da tarefa
                    personagem.status()
                    personagem.menuEstudar() # Mostra o menu de opções "ESTUDAR"
                    opcao = int(input('Escolha uma opção -> '))
                    if opcao == 0: # Sair do menu
                        break
                    else:
                        personagem.estudar(opcao) # Executa o método "estudar" do personagem
                else:
                    print(f'São {tempo.horas}:{tempo.minutos}.\nVocê não possui tempo suficiente para esta tarefa. Tente amanhã!')
                    input('Pressione ENTER para continuar...')
                    break

            # [ 2 ] TRABALHAR
            elif opcao == 2:
                personagem.status()
                if personagem.trabalhoDia == 0: # Se o usuário ainda não trabalhou, o contador permanece em ZERO e ele poderá trabalhar. Caso contrário será bloqueado.
                    if tempo.horas < 16: # se houver tempo hábil para trabalhar, será executado o método
                        if personagem.expHtml >= 2 or personagem.expJava >= 2: # caso o jogador possua experiência necessária, será executado o método
                            personagem.trabalhar() # Executa o método "Trabalhar" do personagem
                            input('Aperte ENTER para continuar...')
                            break
                        else:
                            print(
                                f'\nVocê precisa de nível 02 em Java ou HTML para trabalhar!\n')
                            input('Aperte ENTER para continuar...')
                            break
                    else:
                        print(
                            '\nVocê não tem tempo suficiente para realizar esta tarefa.\n')
                        input('Aperte ENTER para continuar...')
                        break
                else:
                    print('\nVocê já trabalhou hoje! Tente dormir e voltar amanhã...\n')
                    input('Aperte ENTER para continuar...')
                    break

            # [ 3 ] AUMENTAR ENERGIA
            elif opcao == 3:
                if tempo.horas < 24: # caso ainda não seja 24 horas, o método será executado
                    personagem.status()
                    personagem.menuEnergia() # mostra o menu de Energia
                    opcao = int(input('Escolha uma opção acima -> '))
                    if opcao == 0: # sai do menu Energia
                        break
                    else:
                        personagem.aumentarEnergia(opcao) # executa o método baseado no INPUT do usuário
                    input('\nDigite ENTER para continuar...')
                    break
                else:
                    print('Você não possui tempo suficiente para estar tarefa. Volte amanhã.')
                    input('Pressione ENTER para continuar.')
                    break

            # [ 4 ] BANCO
            elif opcao == 4:
                personagem.status()
                print('[ 1 ] Depositar\n[ 2 ] Sacar\n[ 3 ] Extrato\n[ 0 ] Sair\n') # mostra o menu do BANCO
                opcao = int(input('Escolha uma opção -> '))
                if opcao == 0: # sai do menu BANCO
                    break
                else:
                    personagem.irAobanco(opcao) # Executa o método baseado no INPUT do usuário
                input('\nDigite ENTER para continuar...')

            # [ 0 ] TUTORIAL
            elif opcao == 0:
                tutorial() # executa a função TUTORIAL
                break

            # [ 5 ] IR DORMIR
            elif opcao == 5:
                personagem.dormir() # Executa a função dormir
                print('')
                input('\nPressione ENTER para ACORDAR...')
                break
            
            # CASO O USUÁRIO DIGITE OUTRO NÚMERO FORA DAS OPÇÕES
            else:
                system('cls')
                print('Digite apenas números das opções')
                input('\nDigite ENTER para continuar...')
                break
