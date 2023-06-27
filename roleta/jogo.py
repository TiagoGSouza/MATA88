from __future__ import print_function
from roleta import Roleta

class Jogo(object):
    def __init__(self):
        self.jogadores = []
        self.apostas = []
        self.roleta = Roleta()

    def adicionar_participante(self, jogador):
        print(f"{jogador.nome} entrou no jogo")
        self.jogadores.append(jogador)

    def adicionar_aposta(self, jogador, cor, numero):
        aposta = (jogador.nome, cor, numero)
        self.apostas.append(aposta)

    def iniciar_jogo(self):
        print("Vamos comecar o jogo")
        cor_vencedora, numero_vencedor = self.roleta.sortear_par_vencedor()
        print(f"Cor: {cor_vencedora}")
        print(f"Numero: {numero_vencedor}")
        vencedores = [aposta for aposta in self.apostas
                      if aposta[1] == cor_vencedora and aposta[2] == numero_vencedor]
        if len(vencedores) > 0:
            for vencedor in range(len(vencedores)):
                print(f"Vencedor: {vencedor+1} - {vencedores[vencedor][0]}")
        else:
            print("Ngm venceu")
