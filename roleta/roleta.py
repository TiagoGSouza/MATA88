import random
VERMELHO = 1
PRETO = 2
CORES = [VERMELHO, PRETO]

class Roleta(object):
    def sortear_par_vencedor(self):
        cor_vencedora = random.choice(CORES)
        numero_vencedor = random.randint(0, 2)
        return cor_vencedora, numero_vencedor