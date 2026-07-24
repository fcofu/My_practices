#Crea una lista con 5 nombres de animales. Agrega uno más al final, elimina el primero y muestra la lista ordenada alfabéticamente.

animales = ['perro', 'gato', 'raton', 'iguana', 'caballo']
animales.append('jirafa')
print(animales)

#Dada numeros = [4, 8, 15, 16, 23, 42], encuentra el índice del número 16 y elimínalo usando pop().

numerosejercicio = [4,8,15,16,23,42]
paraeliminar = numerosejercicio.index(16)
numerosejercicio.pop(paraeliminar)
#basicamente elimino la variable que tiene el index del 16 adentro de la lista numeros ejercicio
print(numerosejercicio)

#Crea una lista vacía y usa un for para llenarla con los cuadrados de los números del 1 al 10 (numero ** 2).

listavacia = []
for cadanumero in range(1,11):
    listavacia.append(cadanumero**2)
    
print(listavacia)

#Usa un for con range(1, 21) para imprimir solo los números pares.

for xl in range(1,21):
    if xl % 2 == 0:
        print(xl)

#Usa un while para simular una cuenta regresiva desde 10 hasta 0.


numcuenta = 10
while numcuenta >= 0:
    print(numcuenta)
    numcuenta = numcuenta - 1
print('Terminado')

#Con for y range, calcula la suma de todos los números del 1 al 100.

resultado = 0

for op in range(1,101):
    resultado = resultado + op
print(resultado)


#Usa range con step para imprimir los múltiplos de 3 entre 0 y 30.

for cadauno in range(0,31,1):
    if cadauno % 3 == 0 and cadauno != 0:
        print(cadauno)

#Usa range en reversa para imprimir del 20 al 1.

for estenumero in range(20,0,-1):
        print(estenumero)


#Crea un diccionario con 3 productos y sus precios. Usa un for con .items() para imprimir "producto: $precio".


#Dado edades = {"Luis": 20, "Marta": 35, "Ana": 28}, usa un loop para encontrar quién es la persona de mayor edad.


#Crea un diccionario vacío y ve agregando pares clave-valor dentro de un for que recorra una lista de nombres, asignando a cada uno la longitud de su nombre como valor.