from os import system
from tempo import Tempo
from time import sleep
import random as rd
tempo = Tempo()


class Personagem():
    def __init__(self):
        self.__energia = 100
        self.__energiaMax = 100
        self.__dinheiro = 100
        self.__salario = 0
        self.__expHtml = 0
        self.__expJava = 0
        self.__trabalhoDia = 0
        self.nivel = "Sem experiência"
        self.trabalho = False
        self.__contaBanco = 0
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
        num1 = rd.randint(1, 5)
        num2 = rd.randint(1, 5)
        tempo.avancarTempo(60*8)
        self.__dinheiro += self.__salario
        self.trabalho = True
        self.__trabalhoDia = 1
        self.__energia -= 25
        frase1 = f'\n\nVocê trabalhou como {self.nivel} e recebeu R${self.salario}.\n'
        frase2 = f'Sua energia diminuiu para {self.__energia}\n'
        print(f'\n\nCodando...')
        for i in self.carregamento:
            print(i, end="")
            sleep(0.2)
        for i in frase1:
            print(i, end="")
            sleep(0.05)
        for i in frase2:
            print(i, end="")
            sleep(0.05)
        if num1 == num2:
            system('cls')
            print(
                f'\n-------- Evento aleatório --------\n\nOh meu Deus!! Você sofreu um assalto voltando do trabalho e o ladrão levou R${self.dinheiro}.')
            self.__dinheiro = 0

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
            tempo.avancarTempo(60*3)
            self.status()
            self.__expHtml += 0.5
            self.__energia -= 15
            frase1 = f'\n\nVocê estudou HTML e sua experiência atual é {self.__expHtml}\n'
            frase2 = f'Sua energia diminuiu para {self.__energia}\n'
            if self.expJava >= 10 and self.__expHtml >= 10:
                self.nivel = "Programador Senior FullStack"
                self.__salario = 1000
            elif self.__expHtml >= 10:
                self.nivel = "Programador Senior"
                self.__salario = 500
            elif self.__expHtml >= 5:
                self.nivel = "Programador Pleno"
                self.salario = 300
            elif self.__expHtml >= 2:
                self.nivel = "Programador Junior"
                self.__salario = 100
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
            tempo.avancarTempo(60*3)
            self.status()
            self.__expJava += 0.5
            self.__energia -= 15
            frase1 = f'\n\nVocê estudou Java e sua experiência atual é {self.expJava}\n'
            frase2 = f'Sua energia diminuiu para {self.__energia}\n'
            if self.expJava >= 10 and self.expHtml >= 10:
                self.nivel = "Programador Senior FullStack"
                self.__salario = 1000
            elif self.expJava >= 10:
                self.nivel = "Programador Senior"
                self.__salario = 650
            elif self.expJava >= 5:
                self.nivel = "Programador Pleno"
                self.__salario = 250
            elif self.expJava >= 2:
                self.nivel = "Programador Junior"
                self.__salario = 130
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
            tempo.avancarTempo(5)
            self.__energia += 15
            if self.__energia > 100:
                self.__energia = 100
            self.__dinheiro -= 50
            print('\n\nIndo ao mercado...\n')
            sleep(2)
            print(f'Você foi ao mercado e comprou um energético. Sua energia aumentou!')
        # [ 2 ] CAFÉ
        elif opcao == 2:
            self.status()
            tempo.avancarTempo(60)
            self.__energia += 10
            if self.__energia > 100:
                self.__energia = 100
            self.__dinheiro -= 10
            print('\n\nPreparando cafezinho...\n')
            sleep(2)
            print(f'O café estava delicioso. Sua energia aumentou!')
        # [ 3 ] SONECA
        elif opcao == 3:
            self.status()
            tempo.avancarTempo(60*2)
            self.__energia += 15
            if self.__energia > 100:
                self.__energia = 100
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
            if deposito > self.__salario:
                deposito = self.__salario
                print(f'Você depositou R${self.dinheiro}.')
                self.__contaBanco = deposito
                self.__dinheiro -= deposito
            else:
                self.__contaBanco = deposito
                self.__dinheiro -= deposito
                print(f'Você depositou R${deposito}.')
        # [ 2 ] SACAR
        elif opcao == 2:
            saque = float(input('Digite quanto você quer sacar: '))
            if saque > self.contaBanco:
                print(f'Você sacou R${self.contaBanco}')
                self.__dinheiro += self.__contaBanco
                self.__contaBanco = 0
            else:
                self.__contaBanco -= saque
                self.__dinheiro += saque
                print(f'Você sacou R${saque}')
        # [ 3 ] EXTRATO
        elif opcao == 3:
            print(f'Você possui R${self.contaBanco}')
            input('Aperte ENTER para continuar...')
        else:
            system('cls')
            print('Escolha apenas valores entre as opções!')
            input('\nAperte ENTER para voltar...')

    def dormir(self):
        system('cls')
        self.status()
        self.__trabalhoDia = 0
        self.__energia = 100
        tempo.minutos = 0
        tempo.horas = 6
        tempo.dia += 1
        frase1 = '\nzzzZZZzzZZ Dormindo...  ZzzzZzzZZZz\n\n'
        for i in frase1:
            print(i, end="")
            sleep(0.1)
        sleep(3)
        print('Você dormiu como um neném!')
