class Tempo:
    def __init__(self):
        self.dia = 1
        self.horas = 6
        self.minutos = 0
        self.horaLimite = 24
        
    # STATUS TEMPO
    def __str__(self):
        return f'📆 Dia {self.dia}                     ⌚ {self.horas:02d}:{self.minutos:02d}\n'

    # AVANÇAR O TEMPO
    def avancarTempo(self, valor):
        self.minutos += valor
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1


    





