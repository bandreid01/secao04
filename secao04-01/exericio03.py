"""
Usuário digitar 3 números e retornar sua soma.
"""
soma = 0
for numero in range(3):
    n = input('Digite um número: ')
    soma += int(n)
print(soma)
