produto = input('Digite um produto: ')
preço = float(input('Digite o preço do produto sem o desconto aplicado: '))
desconto = preço - (preço * 0.05)
print(f'O preço de {produto} com o desconto de 5% passa a valer R${desconto:.2f}')