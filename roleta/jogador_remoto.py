import Pyro4

class Jogador(object):
    def __init__(self, nome):
        self.nome = nome

    def entrar_jogo(self, jogo):
        jogo.adicionar_participante(self.nome)

    def fazer_aposta(self, jogo, cor, numero):
        jogo.adicionar_aposta(self.nome, cor, numero)

def main():
    jogo = Pyro4.Proxy('PYRONAME:jogo.roleta')
    nome = str(input("Digite seu nome: "))
    jogador = Jogador(nome)
    jogador.entrar_jogo(jogo)
    print("Para escolher a cor VERMELHO digite 1")
    print("Para escolher a cor PRETO digite 2")
    cor = int(input("Escolha a cor da sua aposta: "))
    numero = int(input("Escolha o numero da sua aposta: "))
    jogador.fazer_aposta(jogo, cor, numero)


if __name__ == "__main__":
    main()