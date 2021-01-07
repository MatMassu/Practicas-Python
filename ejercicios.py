#dato = input('Ingrese dato: ')
#
#lista = ['hola', 'mundo', 'prueba', 'prueba 2', 'prueba 3']
#
#if lista.count(dato) > 0:
#    print('El dato existe:', dato)
#else:
#    print('El dato no existe', dato)

#CALCULADORA CON VALIDACION

primero = input('Ingrese el primer numero: ')

try:
    primero = int(primero)
except:
    primero = 'texto'


if primero == 'texto':
    print('El valor ingresado no es valido')
    exit()


segundo = input('Ingrese el segundo numero: ')

try:
    segundo = int(segundo)
except:
    segundo = 'texto'

if segundo == 'texto':
    print('El valor ingresado no es valido')
    exit()


simbolo = input('Ingrese operacion: ')

if simbolo == '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('Resta:', primero - segundo)
elif simbolo == '*':
    print('Producto:', primero * segundo)
elif simbolo == '/':
    print('Division:', primero / segundo)
else:
    print('El simbolo ingresado no es valido')
