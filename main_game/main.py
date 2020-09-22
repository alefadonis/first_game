import trisse_choices
import creditos

input('Pressione enter para continuar ')
print('Bem-Vindo(a) ao  Life is Hard Hack Trisse \nEsse jogo possui restrições de idade,portanto informe sua idade.')
idade = int(input('Qual a sua idade: '))

import os 

if idade < 15:
    print('Infelizmente você não pode jogar, volte em alguns anos') 
    os.system('pause')

elif idade >= 15:
    print('Ótimo, agora podemos continuar: \n')
    
    print('-' * 20)
    print('\nREGRAS DO JOGO: \n§ As respostas devem sempre ser apenas com o número da escolha, após a escolha apenas aperte ENTER.\n§Infelizmente você só pode escolher uma vez, afinal estamos tratando de uma vida aqui, então escolha sabiamente! \n§Alguns caminhos serão curtos e outros serão longos para saber todos eles, é só voltar a jogar. \n§ Se divirta!\n')
    print('-' * 20)

    personagem = input('Agora nos diga quem você quer ser?\n\nTrinity{1} ou Jesse{2}: ')
    
    if personagem == '1':
        trisse_choices()

    elif personagem == '2':
        print('\n--- ESTE PERSONAGEM SÓ ESTARÁ DISPONÍVEL A PARTIR DE 10/06/2020, POR FAVOR AGUARDE ATÉ O LANÇAMENTO --- \n')
			
    credits()
