def list_string(listas):
    convert_string = ', '.join(listas[:-1]) 
# tira o ultimo elemento da lista e joga na variavel 
    convert_string += ' e ' + listas[-1]
# junta a variavel com o ultimo elemento da lista
    return convert_string + ' são saborosas!'


print(list_string(['banana', 'maça', 'coco']))
