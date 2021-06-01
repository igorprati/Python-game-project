from os import system
from tempo import Tempo
from time import sleep
import random as rd
tempo = Tempo()


class Personagem():
    def __init__(self):
        self.__energia = 100  # energia atual
        self.__energiaMax = 100  # energia máxima possível
        self.__dinheiro = 100  # dinheiro atual
        self.__salario = 0  # salário atual
        self.__expHtml = 0  # exp HTML atual
        self.__expJava = 0  # exp Java atual
        self.__trabalhoDia = 0  # se o usuário trabalhou no dia de hoje
        self.nivel = "Sem experiência"  # nível de experiência no trabalho
        self.trabalho = False
        self.__contaBanco = 0  # valor atual no banco
        self.carregamento = "[-----------------]"

    def __str__(self):
        return f'\nStatus do personagem:\n\nExperiência HTML: {self.expHtml}\nExperiência Java: {self.expJava}\nNível: {self.nivel}'

    # ENCAPSULAMENTO
    @property
    def energia(self):
        return self.__energia

    @property
    def energiaMax(self):
        return self.__energiaMax

    @property
    def dinheiro(self):
        return self.__dinheiro

    @property
    def salario(self):
        return self.__salario

    @property
    def contaBanco(self):
        return self.__contaBanco

    @property
    def expJava(self):
        return self.__expJava

    @property
    def expHtml(self):
        return self.__expHtml

    @property
    def trabalhoDia(self):
        return self.__trabalhoDia

    def status(self):
        system('cls')
        print(f'⚡ {self.__energia}/{self.energiaMax}                    💵 R${self.dinheiro}\n\n{tempo}\n______________________________________')

    def menuPrincipal(self):
        system('cls')
        self.status()
        print('')
        print(
            '---------- Menu Principal ----------\n\n[ 1 ] Estudar\n[ 2 ] Trabalhar\n[ 3 ] Aumentar energia\n[ 4 ] Banco\n[ 5 ] Ir dormir\n\n[ 0 ] Tutorial\n')

    # TRABALHAR
    def trabalhar(self):
        num1 = rd.randint(1, 5)  # gera número aleatório para evento
        num2 = rd.randint(1, 5)  # gera número aleatório para evento
        tempo.avancarTempo(60*8)  # avança o tempo
        self.__dinheiro += self.__salario  # soma o dinheiro com o salário atual
        self.trabalho = True  # define salário para TRUE
        self.__trabalhoDia = 1  # define 1. Ou seja, o usuário trabalhou hoje.
        self.__energia -= 25  # diminui energia
        frase1 = f'\n\nVocê trabalhou como {self.nivel} e recebeu R${self.salario}.\n'
        frase2 = f'Sua energia diminuiu para {self.__energia}\n'
        print(f'\n\nCodando...')
        for i in self.carregamento:  # animação utilizando for + sleep
            print(i, end="")
            sleep(0.2)
        for i in frase1:  # animação utilizando for + sleep
            print(i, end="")
            sleep(0.05)
        for i in frase2:  # animação utilizando for + sleep
            print(i, end="")
            sleep(0.05)
        if num1 == num2:  # verifica se os números gerados são iguais. Se sim, dispara o evento aleatório
            system('cls')
            print(
                f'\n-------- Evento aleatório --------\n\nOh meu Deus!! Você sofreu um assalto voltando do trabalho e o ladrão levou R${self.dinheiro}.')
            self.__dinheiro = 0  # dinheiro setado para ZERO

    # ESTUDAR
    def menuEstudar(self):
        print(
            '\n---------- Menu Estudar ----------\n\n[ 1 ] HTML\nExperiência: + 0.5\nDuração: 3 horas\nEnergia: - 15\n\n[ 2 ] Java\nExperiência: + 0.5\nDuração: 3 horas\nEnergia: - 15\n\n[ 0 ] Sair\n')

    def estudar(self, opcao):
        system('cls')
        print(
            '\n---------- Menu Estudar ----------\n\n[ 1 ] HTML\nExperiência: + 0.5\nDuração: 3 horas\nEnergia: - 15\n\n[ 2 ] Java\nExperiência: + 0.5\nDuração: 3 horas\nEnergia: - 15\n\n[ 0 ] Sair\n')
        # ESTUDAR HTML
        if opcao == 1:
            system('cls')
            tempo.avancarTempo(60*3)  # avança o tempo
            self.status()
            self.__expHtml += 0.5  # adiciona experiência
            self.__energia -= 15  # diminui energia
            frase1 = f'\n\nVocê estudou HTML e sua experiência atual é {self.__expHtml}\n'
            frase2 = f'Sua energia diminuiu para {self.__energia}\n'
            if self.expJava >= 10 and self.__expHtml >= 10:  # caso corresponda aos requisitos, sobe de nível
                self.nivel = "Programador Senior FullStack"
                self.__salario = 1000  # aumenta o salário
            elif self.__expHtml >= 10:  # caso corresponda aos requisitos, sobe de nível
                self.nivel = "Programador Senior"
                self.__salario = 500  # aumenta o salário
            elif self.__expHtml >= 5:  # caso corresponda aos requisitos, sobe de nível
                self.nivel = "Programador Pleno"
                self.salario = 300  # aumenta o salário
            elif self.__expHtml >= 2:  # caso corresponda aos requisitos, sobe de nível
                self.nivel = "Programador Junior"
                self.__salario = 100  # aumenta o salário
            print('\nEstudando...')
            for i in self.carregamento:
                print(i, end='')
                sleep(0.2)
            for i in frase1:
                print(i, end='')
                sleep(0.05)
            for i in frase2:
                print(i, end="")
                sleep(0.05)
            if self.expHtml == 10 and self.expJava == 10:
                print(
                    f'\n-=-=-=-=-=-=-=-=-\nParabéns!!!\nVocê agora é um {self.nivel}, seu salário aumentou para R${self.salario}\n-=-=-=-=-=-=-=-=-\n')
            if self.__expHtml == 10:
                print(
                    f'\n-=-=-=-=-=-=-=-=-\nParabéns!!!\nVocê agora é um {self.nivel}, seu salário aumentou para R${self.salario}\n-=-=-=-=-=-=-=-=-\n')
            if self.__expHtml == 5:
                print(
                    f'\n-=-=-=-=-=-=-=-=-\nParabéns!!!\nVocê agora é um {self.nivel}, seu salário aumentou para R${self.salario}\n-=-=-=-=-=-=-=-=-\n')
            if self.__expHtml == 2:
                print(
                    f'\n-=-=-=-=-=-=-=-=-\nParabéns!!!\nVocê agora é um {self.nivel} e pode começar a trabalhar!\n-=-=-=-=-=-=-=-=-\n')
            input('Tecle ENTER para continuar ...')
        # ESTUDAR JAVA
        if opcao == 2:
            system('cls')
            tempo.avancarTempo(60*3)  # avança o tempo
            self.status()
            self.__expJava += 0.5  # adiciona experiência
            self.__energia -= 15  # diminui energia
            frase1 = f'\n\nVocê estudou Java e sua experiência atual é {self.expJava}\n'
            frase2 = f'Sua energia diminuiu para {self.__energia}\n'
            if self.expJava >= 10 and self.expHtml >= 10:  # caso corresponda aos requisitos, sobe de nível
                self.nivel = "Programador Senior FullStack"
                self.__salario = 1000  # aumenta o salário
            elif self.expJava >= 10:  # caso corresponda aos requisitos, sobe de nível
                self.nivel = "Programador Senior"
                self.__salario = 650  # aumenta o salário
            elif self.expJava >= 5:  # caso corresponda aos requisitos, sobe de nível
                self.nivel = "Programador Pleno"
                self.__salario = 250  # aumenta o salário
            elif self.expJava >= 2:  # caso corresponda aos requisitos, sobe de nível
                self.nivel = "Programador Junior"
                self.__salario = 130  # aumenta o salário
            print('\nEstudando...')
            for i in self.carregamento:
                print(i, end="")
                sleep(0.2)
            for i in frase1:
                print(i, end="")
                sleep(0.05)
            for i in frase2:
                print(i, end="")
                sleep(0.05)
            if self.expHtml == 10 and self.expJava == 10:
                print(
                    f'\n-=-=-=-=-=-=-=-=-\nParabéns!!!\nVocê agora é um {self.nivel}, seu salário aumentou para R${self.salario}\n-=-=-=-=-=-=-=-=-\n')
            if self.expJava == 10:
                print(
                    f'\n-=-=-=-=-=-=-=-=-\nParabéns!!!\nVocê agora é um {self.nivel}, seu salário aumentou para R${self.salario}\n-=-=-=-=-=-=-=-=-\n')
            if self.expJava == 5:
                print(
                    f'\n-=-=-=-=-=-=-=-=-\nParabéns!!!\nVocê agora é um {self.nivel}, seu salário aumentou para R${self.salario}\n-=-=-=-=-=-=-=-=-\n')
            if self.expJava == 2:
                print(
                    f'\n-=-=-=-=-=-=-=-=-\nParabéns!!!\nVocê agora é um {self.nivel} e pode começar a trabalhar!\n-=-=-=-=-=-=-=-=-\n')
            input('Tecle ENTER para continuar ...')

    # AUMENTAR ENERGIA
    def menuEnergia(self):
        print('\n--------- Menu Aumentar Energia ---------\n\n[ 1 ] Comprar energético\nCusto: R$25 reais\nEnergia: + 15\nDuração: 5 minutos\n\n[ 2 ] Tomar café\nCusto: R$10 reais\nEnergia: + 10\nDuração: 30 minutos\n\n[ 3 ] Tirar uma soneca\nCusto: 0\nEnergia: + 15\nDuração: 2 horas\n\n[ 0 ] Sair\n')

    def aumentarEnergia(self, opcao):
        # [ 1 ] ENERGÉTICO
        if opcao == 1:
            system('cls')
            self.status()
            tempo.avancarTempo(5)  # avança o tempo
            self.__energia += 15  # aumenta enegia
            if self.__energia > 100:  # se a energia estiver maior que 100:
                self.__energia = 100  # define energia para 100
            self.__dinheiro -= 50  # diminui o dinheiro
            print('\n\nIndo ao mercado...\n')
            sleep(2)
            print(f'Você foi ao mercado e comprou um energético. Sua energia aumentou!')
        # [ 2 ] CAFÉ
        elif opcao == 2:
            self.status()
            tempo.avancarTempo(60)  # avança o tempo
            self.__energia += 10  # aumenta enegia
            if self.__energia > 100:  # se a energia estiver maior que 100:
                self.__energia = 100  # define energia para 100
            self.__dinheiro -= 10  # diminui o dinheiro
            print('\n\nPreparando cafezinho...\n')
            sleep(2)
            print(f'O café estava delicioso. Sua energia aumentou!')
        # [ 3 ] SONECA
        elif opcao == 3:
            self.status()
            tempo.avancarTempo(60*2)  # avança o tempo
            self.__energia += 15  # aumenta enegia
            if self.__energia > 100:  # se a energia estiver maior que 100:
                self.__energia = 100  # define energia para 100
            print('\n\nFechando os olhos...\n')
            sleep(2)
            print(f'Você até babou! A soneca rendeu. Sua energia aumentou!\n')
        else:
            system('cls')
            print('\n** Escolha apenas entre as opções disponíveis! **')

    # BANCO
    def irAobanco(self, opcao):
        # [ 1 ] DEPOSITAR
        if opcao == 1:
            deposito = float(input('\nDigite quanto você quer depositar: '))
            # se o valor do depósito for maior que o dinheiro do usuário:
            if deposito > self.__dinheiro:
                tempo.avancarTempo(60*2)
                deposito = self.__dinheiro  # o depósito será toda a quantia de dinheiro do usuário
                print(f'Você depositou R${self.dinheiro}.')
                self.__contaBanco = deposito  # o valor da quantia depositada será o valor de depósito
                self.__dinheiro -= deposito  # dinheiro atual será subtraído pelo valor do depósito
            else:  # se o valor do depósito não for maior que o dinheiro do usuário:
                tempo.avancarTempo(60*2)
                # a quantia  depositada no banco será igual ao valor do depósito
                self.__contaBanco = deposito
                # o dinheiro do usuário será subtraído pelo valor do depósito
                self.__dinheiro -= deposito
                print(f'Você depositou R${deposito}.')
        # [ 2 ] SACAR
        elif opcao == 2:
            saque = float(input('Digite quanto você quer sacar: '))
            # se o valor do saque for maior que o valor presente na conta:
            if saque > self.contaBanco:
                tempo.avancarTempo(60*2)
                print(f'Você sacou R${self.contaBanco}')
                # o saque será toda a quantia presente na conta
                self.__dinheiro += self.__contaBanco
                self.__contaBanco = 0  # a quantia na conta ficará zerada
            else:  # se não:
                tempo.avancarTempo(60*2)
                self.__contaBanco -= saque  # a quantida na conta será debitada pelo valor do saque
                self.__dinheiro += saque  # o dinheiro na carteira será somado ao valor do saque
                print(f'Você sacou R${saque}')
        # [ 3 ] EXTRATO
        elif opcao == 3:
            tempo.avancarTempo(60*2)
            # mostra o valor presente na variável __contaBanco
            print(f'Você possui R${self.contaBanco}')
            input('Aperte ENTER para continuar...')
        else:
            system('cls')
            print('Escolha apenas valores entre as opções!')
            input('\nAperte ENTER para voltar...')

    def dormir(self):
        system('cls')
        self.status()
        # reseta a variável que armazena a informação de que o usuário já trabalhou
        self.__trabalhoDia = 0
        self.__energia = 100  # energia restaurada
        tempo.minutos = 0  # tempo resetado
        tempo.horas = 6
        tempo.dia += 1  # dia aumentado em + 1
        frase1 = '\nzzzZZZzzZZ Dormindo...  ZzzzZzzZZZz\n\n'
        for i in frase1:
            print(i, end="")
            sleep(0.1)
        sleep(3)
        print('Você dormiu como um neném!')
