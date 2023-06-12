

class Jogador(object):
    def __init__(self, nome):
        self.nome = nome

    def entrar_jogo(self, jogo):
        jogo.adicionar_participante(self)

    def fazer_aposta(self, jogo, cor, numero):
        jogo.adicionar_aposta(self, cor, numero)
