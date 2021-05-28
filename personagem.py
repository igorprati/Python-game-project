from os import system
from time import sleep


class Personagem:
    def __init__(self):
        self.saude = 100
        self.dinheiro = 100
        self.salario = 0
        self.expHtml = 0
        self.expJava = 0
        self.nivel = "Sem experiência"
        self.trabalho = False
        
    def __str__(self):
        return f'Status do personagem:\n\nSaúde: {self.saude}\nDinheiro: R${self.dinheiro}\nExperiência HTML: {self.expHtml}\nExperiência Java: {self.expJava}\nNível: {self.nivel}'

    # TRABALHAR
    def trabalhar(self):
        if self.expHtml >= 2 or self.expJava >= 2:
            self.dinheiro += self.salario
            self.trabalho = True
            self.saude -= 10
            print(f'Você trabalhou como {self.nivel} e recebeu R${self.salario}.')
            print(f'Sua saúde diminuiu para {self.saude}')
        else:
            self.trabalho = False
            print(f'Você precisa de nível 02 em Java ou HTML para trabalhar!\n')
    
    # ESTUDAR HTML
    def estudarHtml(self):
        self.expHtml += 0.5
        self.saude -= 5
        if self.expJava >= 10 and self.expHtml >= 10:
            self.nivel = "Programador Senior FullStack"
            self.salario = 1000

        elif self.expHtml >= 10:
            self.nivel = "Programador Senior HTML"
            self.salario = 500

        elif self.expHtml >= 5:
            self.nivel = "Programador Pleno HTML"
            self.salario = 300

        elif self.expHtml >= 2:
            self.nivel = "Programador Junior HTML"
            self.salario = 100

        print(f'Você estudou HTML e sua experiência atual é {self.expHtml}\n')
        print(f'Sua saúde diminuiu para {self.saude}')

    # ESTUDAR JAVA
    def estudarJava(self):
        self.expJava += 0.5
        self.saude -= 5
        if self.expJava >= 10 and self.expHtml >= 10:
            self.nivel = "Programador Senior FullStack"
            self.salario = 1000

        elif self.expJava >= 10:
            self.nivel = "Programador Senior Java"
            self.salario = 650

        elif self.expJava >= 5:
            self.nivel = "Programador Pleno Java"
            self.salario = 250

        elif self.expJava >= 2:
            self.nivel = "Programador Junior Java"
            self.salario = 130
        print(f'Você estudou Java e sua experiência atual é {self.expJava}\n')
        print(f'Sua saúde diminuiu para {self.saude}')


    # AUMENTAR SAÚDE
    def comidaSaudavel(self):
        system('cls')
        self.saude += 4
        self.dinheiro -= 15
        print('Comendo...\n')
        sleep(2)
        print(f'Você comprou uma deliciosa marmita fitness por R$15.\n')
    
    def academia(self):
        system('cls')
        self.saude += 15
        self.dinheiro -= 50
        print('Malhando pesado...\n')
        sleep(2)
        print(f'Você malhou pesado hoje. Continue assim!\n')
    
    def corrida(self):
        system('cls')
        self.saude += 5
        print('Você saiu para correr um pouco...\n')
        sleep(2)
        print(f'A corrida foi muito boa!\n')

