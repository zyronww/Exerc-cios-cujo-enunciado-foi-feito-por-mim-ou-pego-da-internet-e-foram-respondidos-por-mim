#Fazer um programa que pergunte ao usuário infinitas vezes dias aleatórios da semana em ingles, sendo diferente do anterior, mostrando logo em seguida se ele errou ou acertou, caso ele erre, mostre o correto e sempre perguntando se ele quer continuar e caso ele nao queira, o programa pare e mostre quantas tentativas, quantos erros e quantos acertos o usuário teve.
from random import choice
errado = certo = tentativas = 0
escolha = ''
diasing = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
diasport = ['Domingo','Segunda','Terca','Quarta','Quinta','Sexta','Sabado']
while escolha != 'N':
    if tentativas == 0:
        aleatorio = choice(diasing)
        copia_aleatorio = aleatorio
    else:
        aleatorio = choice(diasing)
        while aleatorio == copia_aleatorio:
            aleatorio = choice(diasing)
        copia_aleatorio = aleatorio
    pergunta = input(f'Como se escreve \033[33m"{aleatorio}"\033[m em português\n(nao precisa colocar o "-feira")? ').capitalize().replace('ç','c').replace('á','a').replace(' ','')
    if pergunta in diasport:
        pergunta_index = diasport.index(pergunta)
    aleatorio_index = diasing.index(aleatorio)
    tentativas += 1
    if pergunta in diasport:
        if pergunta_index == aleatorio_index:
            print('\033[32mVocê acertou!\033[m')
            certo += 1
        else:
            print('\033[31mVocê errou!\033[m')
            if aleatorio_index == 6:
                print(f'O correto é \033[36mSábado\033[m')
            elif aleatorio_index == 2:
                print(f'O correto é \033[36mTerça\033[m')
            else:
                print(f'O correto é \033[36m{diasport[aleatorio_index]}\033[m')
            errado += 1
    else:
        print('\033[31mVocê errou!\033[m')
        if aleatorio_index == 6:
            print(f'O correto é \033[36mSábado\033[m')
        elif aleatorio_index == 2:
            print(f'O correto é \033[36mTerça\033[m')
        else:
            print(f'O correto é \033[36m{diasport[aleatorio_index]}\033[m')
        errado += 1
    escolha = input('Quer continuar [S/N]? ').upper().replace(' ','')
    while escolha not in 'SN' or escolha == '':
        escolha = input('Quer continuar [S/N]? ').upper().replace(' ','')
    print('=' * 21)
print(f'Você tentou um total de \033[36m{tentativas} vezes\033[m, \033[32macertou {certo} vezes\033[m e \033[31merrou {errado} vezes\033[m.') #Perdoe-me, mas se eu fosse colocar concordância, isso precisaria de muitas linhas, com o raciocínio que pensei
