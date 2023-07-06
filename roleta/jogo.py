from __future__ import print_function
import time
from roleta import Roleta
import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Jogo(object):
    def __init__(self, daemon):
        self.jogadores = []
        self.apostas = []
        self.roleta = Roleta()
        self.jogo_iniciado = False
        self.cor_vencedora = -1
        self.numero_vencedor = -1
        self.qt_jogadores = 0
        self.jogo_status = True
        self.daemon = daemon

    def define_quantidade_jogadores(self, qtd_jogadores):
        self.qt_jogadores = qtd_jogadores

    def adicionar_participante(self, nome):
        try:
            self.jogadores.append(nome)
            print("Jogador adicionado")
            print(f"Seja bem vindo(a), {nome}")
        except:
            print("Erro ao adicionar jogador")

    def adicionar_aposta(self, nome, cor, numero):
        try:
            aposta = (nome, cor, numero)
            self.apostas.append(aposta)
            print("Aposta adicionada")
        except:
            print('Aposta invalida')

    def iniciar_jogo(self):
        if not (self.jogo_iniciado):
            self.cor_vencedora, self.numero_vencedor = self.roleta.sortear_par_vencedor()
            self.jogo_iniciado = True
            print(f"Cor: {self.cor_vencedora}")
            print(f"Numero: {self.numero_vencedor}")
        i = 0
        while len(self.apostas) < self.qt_jogadores:
            if i == 0:
                print("Esperando mais jogadores")
                i = 1
            time.sleep(1)
        return self.notifica_jogadores()
    
    def notifica_jogadores(self):
        vencedores = [aposta for aposta in self.apostas
                      if aposta[1] == self.cor_vencedora and aposta[2] == self.numero_vencedor]
        if len(vencedores) > 0:
            for vencedor in range(len(vencedores)):
                s = (f"Vencedor: {vencedor+1} - {vencedores[vencedor][0]}")
                self.jogo_status = False
                return s
        else:
            self.jogo_status = False
            return "Ninguem venceu"
        
    def status_jogo(self):
        return self.jogo_status
    
    @Pyro4.oneway
    def encerrar_jogo(self):
        try:
            self.daemon.shutdown()
        except:
            print("Nao foi possivel encerrar o jogo")
    
if __name__=="__main__":
    daemon = Pyro4.Daemon()
    jogo_server = Jogo(daemon)
    uri = daemon.register(jogo_server, objectId='Jogo')
    ns = Pyro4.locateNS()
    ns.register("jogo.roleta", uri)
    print("Servidor do jogo iniciado")
    daemon.requestLoop()