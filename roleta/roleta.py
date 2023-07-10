import random
import Pyro4

VERMELHO = 1
PRETO = 2
CORES = [VERMELHO, PRETO]

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Roleta(object):
    def __init__(self, daemon):
        self.daemon = daemon

    def sortear_par_vencedor(self):
        cor_vencedora = random.choice(CORES)
        numero_vencedor = random.randint(0, 36)
        print(f"Par sorteado: cor - {cor_vencedora} numero - {numero_vencedor}")
        return cor_vencedora, numero_vencedor
    
    @Pyro4.oneway
    def encerrar_roleta(self):
        try:
            self.daemon.shutdown()
        except:
            print("Nao foi possivel encerrar a roleta")
    
if __name__=="__main__":
    daemon = Pyro4.Daemon()
    roleta_server = Roleta(daemon)
    uri = daemon.register(roleta_server, objectId='Roleta')
    ns = Pyro4.locateNS()
    ns.register("roleta", uri)
    print("Roleta pronta para sortear")
    daemon.requestLoop()