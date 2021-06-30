'''
def imprime_cosas():
    print("la clase esta genial")
    print("python es lo maximo")
imprime_cosas()

def repetir_funciones():
    imprime_cosas
    imprime_cosas

repetir_funciones()
'''

'''
def suma(a, b):
    return a+b

suma(30, 10)
'''
'''
def mi_funcion(nombre, apellido):
    nombre_completo = nombre, apellido
    print(nombre_completo)

mi_funcion('david', 'alvarez')
'''
'''
def saludar(nombre, mensaje='hoa'):
    print(mensaje, nombre)

saludar('pepe grillo')
'''
'''
def saludar(nombre, mensaje='hola)'):
    print(mensaje, nombre)

saludar(mensaje='buen dia', nombre='juancho')
'''
'''
def saludo(cadena):
    return "hola {}! ¿como estas?".format(cadena)

nombre = input("ingrese su nombre")
texto_saludo = saludo(nombre)
print(texto_saludo)
'''
'''
def sumayresta():
    numero1 = int(input("ingrese el numero 1"))
    numero2 = int(input("ingrese el numero 2"))
    suma = numero1 + numero2
    resta = numero1 - numero2
    print(suma)
    print(resta)

sumayresta()
'''

'''
#listas paralelas:
nombres =[]
edades = []

for i in range(0,2):
    nombre = input("ingresa el nombre")
    nombres.append(nombre)
    edad = int(input("ingrese la edad"))
    edades.append(edad)

print(nombres)
print(edades)

for i in range (0, len(nombres)):
    if edades [i]>= 18:
        print(nombres[i])

        #listas compuestas:
    '''
'''
listas = [[1,3,4], [7,9,0], [2,6,9]]
print(listas[0][1])

lista = [[1,3,4], [7,9,0], [2,6,9]]
for i in range(0,len(lista[0])):
    print(lista[0][i])
'''

'''
lista = [[1,3,4], [7,9,0], [2,6,9]]
for i in range(0,len(lista)):
    for j in range(0,len(lista[i])):
        print(lista[i][j]) '''
'''
lista1 = [[2,4,5,3], [3,9,7,8], [5,3,4,9]]
for i in range(0, len(lista1)):
    suma=0
    for j in range(0, len(lista1[i])):
        suma += lista1[i][j]
    print(suma) '''
    
''' 
lista = [[7], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]
suma = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        suma += lista[i][j]
print(suma)'''


padres = [["andres", "camila"], ["pedro", "manuela"], ["marcos", "sandra"]]
hijos = [["joshua"], ["manuela", "maicol", "sandra"], []]

for i in range(len(padres)):
    print("el padre {} y la madre {} tienen estos hijos:".format(padres))
    for j in range(len(hijos[i])):
        print("el hijo numero {} se llama {}". format(j+1,hijos[i][j]))



'''for in range(len(padres)):
    nombre_padre = padres[i][0]
    numero_hijos = len(hijos[i])
    print("el nombre del padre es {} y el numero de hijos es {}".format(nombre_padre, numero_hijos))
'''
