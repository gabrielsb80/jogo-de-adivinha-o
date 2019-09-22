from random import randint
from time import sleep
computador = randint(0 , 100) #aqui o computador vai "pensar" num número de 0 a 100
print('-=-' * 20)
print('Vou pensar em um número de 0 a 100, tente adivinhar')
print('-=-' * 20)
jogador= int(input('Digite um número de 0 a 100: ')) #aqui o usuário vai advinhar o número que o computador "pensou"
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS VOCÊ GANHOU!')
else:
    print('Que pena você perdeu, eu pensei em {} e não em {}'.format(computador , jogador))
    print('BOA SORTE NA PROXIMA VEZ')

