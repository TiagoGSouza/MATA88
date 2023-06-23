from jogo import Jogo
from jogador import Jogador

VERMELHO = 1
PRETO = 2
CORES = [VERMELHO, PRETO]

jogo = Jogo()
jogador1 = Jogador("Tiago")
jogador2 = Jogador("Bia")
jogador3 = Jogador("Teste")
jogador4 = Jogador("Teste2")

jogador1.entrar_jogo(jogo)
jogador2.entrar_jogo(jogo)
jogador3.entrar_jogo(jogo)
jogador4.entrar_jogo(jogo)

jogador1.fazer_aposta(jogo, VERMELHO, 1)
jogador2.fazer_aposta(jogo, PRETO, 0)
jogador3.fazer_aposta(jogo, VERMELHO, 0)
jogador4.fazer_aposta(jogo, PRETO, 1)

jogo.iniciar_jogo()