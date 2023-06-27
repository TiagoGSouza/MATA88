from __future__ import print_function
from roleta import Roleta
import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Jogo(object):
    def __init__(self):
        self.jogadores = []
        self.apostas = []
        self.roleta = Roleta()

    def adicionar_participante(self, nome):
        if nome != None:
            self.jogadores.append(nome)
            print("Jogador adicionado")
        else:
            print("Erro ao adicionar jogador")

    def adicionar_aposta(self, nome, cor, numero):
        aposta = (nome, cor, numero)
        self.apostas.append(aposta)

    def iniciar_jogo(self):
        print("Vamos comecar o jogo")
        cor_vencedora, numero_vencedor = self.roleta.sortear_par_vencedor()
        print(f"Cor: {cor_vencedora}")
        print(f"Numero: {numero_vencedor}")
        vencedores = [aposta for aposta in self.apostas
                      if aposta[1] == cor_vencedora and aposta[2] == numero_vencedor]
        return cor_vencedora, numero_vencedor, vencedores
    
    def reiniciar_jogo(self):
        self.__init__()
        print("Jogadores e apostas redefinidas")

def main():
    Pyro4.Daemon.serveSimple(
        {
            Jogo: "example.jogo"
        },
        host="127.0.0.1",
        ns=True)
    
if __name__=="__main__":
    main()