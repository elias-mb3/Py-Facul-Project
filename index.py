from random import randint
print('#### Iniciando Jogo ####')
print('As regras são simples, escolha um número inteiro de 0 a 100
e você tem 10 chutes')
randomNum = randint(0, 100)
chances = 10
for _ in range(chances):
chute = input('Chute um número entre 0 a 100: ')
if chute.isnumeric(): #Falo que quero um número não string
chute = int(chute) #Falo que quero um número inteiro
chances -= 1 #Deixei implícito a subtração das chances
if chute == randomNum: #Prefiro começar com a mais fácil que
é a vitória
print('Parabéns, você venceu! O número era {} e você
ainda tinha {} chances.'.format(randomNum, chances))
break
else: #Senão ele vai tentar até acertar ou até as chances
acabarem
print('')
if chute > randomNum:
print('Você errou!!! Dica: É um número menor.')
else:
print('Você errou!!! Dica: É um número maior.')
print('Você ainda possui {} chances.'.format(chances))
if chances == 0:
print('Suas chances acabaram, você perdeu!')
print('#### Fim do Jogo ####')