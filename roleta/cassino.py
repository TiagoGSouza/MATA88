import sys
from jogo import Jogo
from jogador import Jogador
import Pyro4
import Pyro4.util

sys.excepthook = Pyro4.util.excepthook

VERMELHO = 1
PRETO = 2
CORES = [VERMELHO, PRETO]

jogo = Pyro4.Proxy('PYRONAME:jogo.roleta')
jogo.reiniciar_jogo()

qt_jogadores = int(input("Quantos jogadores vao participar? ").strip())

for i in range(qt_jogadores):
    nome = str(input(f"Digite o nome do jogador {i+1}: "))
    jogador = Jogador(nome)
    jogador.entrar_jogo(jogo)
    print(f"Seja bem vindo(a), {nome}")
    print("Faça sua aposta")
    print("Para escolher a cor VERMELHO digite 1")
    print("Para escolher a cor PRETO digite 2")
    cor = int(input("Escolha a cor da sua aposta: "))
    numero = int(input("Escolha o numero da sua aposta: "))
    jogador.fazer_aposta(jogo, cor, numero)

print("\nJogadores registrados e apostas encerradas")
print("-----------------------------------------")

cor_vencedora, numero_vencedor, vencedores = jogo.iniciar_jogo()
print(f"\nCor sorteada: {cor_vencedora}")
print(f"Numero vencedor: {numero_vencedor}")
print("\nE os vencedores são:")
if len(vencedores) > 0:
    for vencedor in range(len(vencedores)):
        print(f"Vencedor: {vencedor+1} - {vencedores[vencedor][0]}")
else:
    print("Ninguem venceu")