import random

def dados(): 
    dado1 = random.randint(1, 6) 
    dado2 = random.randint(1, 6)
    resultado = dado1 + dado2 
    return dado1, dado2, resultado



contador = 3

while True:
    

   menu = input(""""
    1- Jogar
    2- Ver chances
    0- sair
   
   """)
   match menu:
      case '1':
        
         print('Você está jogando.')
         sorte = int(input('Digite qual o primeiro número que  você acha que irá vir?(entre 1 e 6)'))
         sorte2 = int(input('Digite qual o segundo número que você acha que irá vir?(entre 1 e 6)'))
         sorte3= int(input('Digite qual a soma desses números:'))


         
         dado1, dado2, resultado = dados()
         if dado1 == sorte and dado2 == sorte2 and resultado == sorte3:
            print('Voce acertou')
         else:
            contador -= 1
            print('Você errou')
            print(f'Os números que sairam nessa vez foi {dado1}, {dado2} e a soma foi {resultado}')
         if contador == 0:
            print('Você excedeu as tentativas')
            break
         
         
      case '2':
         print(contador)

      

      case '3':
         print('Você encerrou o jogo')
         break
   
      case _:
         print('Opção inválida')
       

    