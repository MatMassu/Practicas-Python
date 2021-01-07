lista = ['hola', 'mundo', 'prueba']

lista2 = lista.copy()
lista.append('cuatro')

# lista.clear()

# print(lista, lista2.count(3))
# print(len(lista, lista2)

largoLista = len(lista)
largoLista2 = len(lista2)

# print(largoLista, largoLista2)
# print(lista[1])

# lista.pop() ~~ elimina ultimo elemento de la lista

# lista.remove('hola') ~~ elimina un elemento por su valor

lista.reverse()
lista.sort()
tupla = ('hola', 'mundo', 'somos', 'tupla')
# print(tupla.count('hola'))
# tupla.append() no existe a menos que se convierta a lista
# print(tupla.index('mundo)) devuelve el indice del valor indicado

# listaDeTupla = list(tupla)
# print(listaDeTupla)

rango = range(6)
# print(rango)




diccionario = {
        "nombre": "Pedro",
        "color": "Blanco",
        "edad": "52"
}

# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario.get('nombre'))

diccionario['nombre'] = 'Raul'

# print(len(diccionario))

diccionario['Pelo'] = 'Si'

# print(diccionario)

# diccionario.pop('Pelo') ~~Equiv. a del. Si es ultimo item, utilizar popitem
# diccionario.popitem()
# copiaDic = diccionario.copy() ~~Genera copia de ultima iteracion
copiaDic = dict(diccionario)
# del diccionario['Pelo']
diccionario.clear()
# print(diccionario)

Variables = {
        "A": {
            "prueba": "Si",
            "edad": 4
        },
        "B":{
            "prueba": "No",
            "edad": 12
        }
}

# print(Variables)

perritos = dict(nombre="asd", edad=6)
# print(perritos)

verdadero = True
falso = False

print(verdadero, falso)










