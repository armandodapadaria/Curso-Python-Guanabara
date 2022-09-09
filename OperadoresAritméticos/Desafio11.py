largura = float(input('Insira o valor em metros da largura: '))
altura = float(input('Insira o valor em metros da altura: '))
area = largura * altura
litro = area / 2
print(f'A quantidade de tinta necessária para pintar a área de {area}m² são {litro:.2f}litros')