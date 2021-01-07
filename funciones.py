def miFuncion():
    print('Mi primera funcion')

# miFuncion()

def imprimeDato(*nombre):
    print('El nombre completo es:', nombre[1])

# imprimeDato('Nombre', 'Apellido', 'Nombre 2', 'Apellido 2') 

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

# nombreCompleto(nombre='Nombre1', apellido='Apellido1')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

# nombreCompleto2(nombre='Nombre', apellido='Apellido')

def miFuncion2(argumento = 'Nombre'):
    print(argumento)

# miFuncion2('Batman')
# miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)

# miFuncionLista(['Nombre','Apellido'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

# nombres = concatenaNombres(['Nombre', 'Apellido'])
# print(nombres)

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)

