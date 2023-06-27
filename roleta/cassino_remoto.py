import sys

import Pyro4
import Pyro4.util

sys.excepthook = Pyro4.util.excepthook

jogo = Pyro4.Proxy('PYRONAME:jogo.roleta')

cor_vencedora, numero_vencedor, vencedores = jogo.iniciar_jogo()
print(f"\nCor sorteada: {cor_vencedora}")
print(f"Numero vencedor: {numero_vencedor}")
print("\nE os vencedores são:")
if len(vencedores) > 0:
    for vencedor in range(len(vencedores)):
        print(f"Vencedor: {vencedor+1} - {vencedores[vencedor][0]}")
else:
    print("Ninguem venceu")