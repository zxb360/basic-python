def list_string(listas):
    convert_string = ', '.join(listas[:-1]) 
# tira o ultimo elemento da lista e joga na variavel 
    convert_string += ' e ' + listas[-1]
# junta a variavel com o ultimo elemento da lista
    return convert_string + ' são saborosas!'


print(list_string(['banana', 'maça', 'coco']))


# exercicio numero 2
# Seu grid
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

# tamanho da coluna e linha
num_coluna = len(grid[0])
num_linha = len(grid)

linha_result = []

for linha in range(num_linha):
    str_result = ''

    for coluna in range(num_coluna):
        str_result += grid[linha][coluna]

    linha_result.append(str_result)

for linha in linha_result:
    print(linha)
