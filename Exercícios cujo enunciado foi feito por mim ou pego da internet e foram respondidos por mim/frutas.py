frutas = ('Coco', 'Uva', 'Laranja', 'Goiaba', 'Abacaxi', 'Melancia', 'Morango', 'Pitaya')
print(f'A primeira fruta é "{frutas[0]}".')
print(f'A última fruta é "{frutas[-1]}".')
print(f'A tupla "frutas" possui um total de {len(frutas)} frutas.')
print(f'As frutas em ordem alfabética da tupla "frutas" são:\n{sorted(frutas)}')
print('-' * 45)
escolha = input('Digite uma fruta: ').strip().capitalize()
if escolha in frutas:
    print(f'A fruta {escolha} está na posição {frutas.index(escolha)}.')
else:
    print(f'A fruta {escolha} não está na tupla.')