class Tempo:
    def __init__(self):
        self.dia = 1 # jogo inicia no dia 1
        self.horas = 6 # hora de início do dia
        self.minutos = 0 # minutos de início do dia
        self.horaLimite = 24 # hora limite do dia
        
    # STATUS TEMPO
    def __str__(self):
        return f'📆 Dia {self.dia}                     ⌚ {self.horas:02d}:{self.minutos:02d}\n'

    # AVANÇAR O TEMPO
    def avancarTempo(self, valor): # método de avançar o tempo, com o parâmetro da quantidade de tempo que será avançada
        self.minutos += valor # os minutos aumentam de acordo com o valor do parâmetro
        while(self.minutos >= 60): # enquanto os minutos forem maior que 60:
            self.minutos -= 60 # diminui -60 minutos
            self.horas += 1 # aumenta 1 hora


    





