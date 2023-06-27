

class Jogador(object):
    def __init__(self, nome):
        self.nome = nome

    def entrar_jogo(self, jogo):
        jogo.adicionar_participante(self.nome)

    def fazer_aposta(self, jogo, cor, numero):
        jogo.adicionar_aposta(self.nome, cor, numero)
