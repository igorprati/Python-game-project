from os import system
from time import sleep


class Tempo:
    def __init__(self):
        self.dia = 1
        self.horas = 6 
        self.minutos = 0
        self.horaLimite = 24

    def __str__(self):
        return f'=-=-=-=-=-=-=\nAgora são {self.horas} horas e {self.minutos} minutos do dia {self.dia}.\n=-=-=-=-=-=-='

    # AVANÇAR O TEMPO
    def avancarTempo(self, valor):
        self.minutos += valor
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
        
    # DORMIR
    def dormir(self):
        system('cls')
        self.horas = 6
        self.minutos = 0
        self.dia += 1
        print('zzzZZZzzZZ Dormindo...  ZzzzZzzZZZz\n')
        sleep(3)
        print('Você dormiu como um neném!\n')

    





