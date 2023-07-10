import sys
import time
import Pyro4
import Pyro4.util

sys.excepthook = Pyro4.util.excepthook

@Pyro4.expose
@Pyro4.callback
def main():
    print("Bem-vindo ao jogo de Roloeta!")
    jogo = Pyro4.Proxy('PYRONAME:jogo')
    roleta = Pyro4.Proxy('PYRONAME:roleta')
    qt_jogadores = int(input("Quantos jogadores vão participar? "))
    jogo.define_quantidade_jogadores(qt_jogadores)
    cor_vencedora, numero_vencedor = roleta.sortear_par_vencedor()
    jogo.define_par_vencedor(cor_vencedora, numero_vencedor)
    print("Vamos esperar os jogadores")
    while jogo.status_jogo():
        time.sleep(1)
    time.sleep(5)
    print("Jogo encerrado")
    roleta.encerrar_roleta()
    jogo.encerrar_jogo()

if __name__=="__main__":
    main()