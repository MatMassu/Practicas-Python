# c = open('ejemplo.txt', 'w')

# c.write('\nAgregaremos una nueva linea')

# c.close()

# x = open('ejemplo.txt')

# print(x.read())

import os 

if os.path.exists('ejemplo.txt'):
    os.remove('ejemplo.txt')
else:
    print('El archivo no existe')

os.rmdir('carpeta')