from random import shuffle
girias_abreviacoes_escrita_normal = [['U', '4U', 'U2', 'OMG', 'LOL', 'LMAO', 'LMFAO', 'OOO', 'ASAP', 'IMO', 'FYI', 'TTYL', 'POV', 'TBH', 'WTF', 'G2G', 'FB', 'MSG', 'YNK', 'JK', 'IDC', 'BFF', 'SRSLY', 'TL;DR', 'SOML', 'J4F', 'WUZUP', 'NSFW', 'PPL', 'DIY', 'OMW', 'IDK', 'BRB', 'W8', 'RUOK', 'CU'], ['you', 'for you', 'you too', 'oh, my god', 'laughing out loud', 'laughing my ass off', 'laughing my fucking ass off', 'out of office', 'as soon as possible', 'in my oppinion', 'for your information', 'talk to you later', 'point of view', 'to be honest', 'what the fuck', 'got to go', 'facebook', 'message', 'you never know', 'just kidding', 'i dont care', 'best friends forever', 'seriously', 'too long didnt read', 'story of my life', 'just for fun', 'whats up', 'not safe for work', 'people', 'do it yourself', 'on my way', 'i dont know', 'be right back', 'wait', 'are you ok', 'see you']]
lista_save = girias_abreviacoes_escrita_normal[0][:]
shuffle(girias_abreviacoes_escrita_normal[0])
print('\033[33mEsse é um teste de seus conhecimentos!\nDesabrevie corretamente e ganhe um ponto. Boa sorte!\033[m')
tot = acertos = 0
for c in girias_abreviacoes_escrita_normal[0]:
    pos = lista_save.index(c)
    print(c, '🠒', end=' ')
    resposta = input().strip().replace("'", '').lower().replace(';', ' ').replace('?', '').replace('!', '')
    if resposta == girias_abreviacoes_escrita_normal[1][pos]:
        acertos += 1
        print('\033[32mVocê acertou!\033[m\n\033[36m+1 Ponto\033[m')
    else:
        print(f'\033[31mVocê errou.\033[m \033[33mA resposta correta é "{girias_abreviacoes_escrita_normal[1][pos]}"\n+0 Pontos \033[m')
    print('-' * 15)
    tot += 1
if acertos <= 15:
    print(f'\033[31mVocê acertou {acertos}/{tot}\033[m')
elif 15 < acertos <= 25:
    print(f'\033[33mVocê acertou {acertos}/{tot}\033[m')
else:
    print(f'\033[32mVocê acertou {acertos}/{tot}\033[m')