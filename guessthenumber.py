import random

def adivinhe(x):
    numero_random = random.randint(1, x)
    adivinhe = 0
    while adivinhe != numero_random:
        adivinhe = int(input(f'Chute um número entre 1 e {x}: '))
        if adivinhe < numero_random:
            print('Tente novamente, o número é maior que esse')
        elif adivinhe > numero_random:
            print('Tente novamente, o número é menor que esse')
        else:
            print ('Meus Parabéns, você acertou o número!! :)')
                
    
adivinhe(10)

    