print("EJERCICIO 3")
#  3 count of even and old digit
num_var = int(input("ingresa un numero entero: "))
pares = 0
impares = 0
while(num_var > 0):
    dig = num_var % 10
    if dig % 2 == 0:
        pares += 1
    else:
        impares += 1
    num_var = num_var //10

print("numero pares:", pares, "numeros impares", impares)

print("EJERCICIO 1")
# 1 sequence of order verified
numeros = []
for i in range(5):
    numero = int(input(f"ingrese el numero {i + 1}: "))
    numeros.append(numero)

# Verificar el orden de los números
ascendente = True
descendente = True

for i in range(4):  # Hasta el penúltimo número
    if numeros[i] < numeros[i+1]:
        descendente = False
    elif numeros[i] > numeros[i+1]:
        ascendente = False

# Mostrar el resultado
if ascendente:
    print("Orden ascendente")
elif descendente:
    print("Orden descendente")
else:
    print("Orden aleatorio")    

print("EJERCICIO 2")  
# 2 element search 
nume = list(map(int, input("ingrese una lista de numeros (separadas por espacios): ").split()))
objetivo = int(input("ingrese el número que desea buscar: "))


encontrado = False
for num in nume:
    if num == objetivo:
        encontrado = True
        break
if encontrado:
    print("número encontrado")
else:
    print("número no encontrado")

print("EJERCICIO 4")
# 4 team performance comparation
equipo_A = list(map(int, input("ingrese los 5 resultados del equipo A en una lista (separadas por espacios): ").split()))
equipo_B = list(map(int, input("ingrese los 5 resultados del equipo B en una lista (separadas por espacios): ").split()))

promedio_A = sum(equipo_A) / len(equipo_A)
promedio_B = sum(equipo_B) / len(equipo_B)

if promedio_A > promedio_B:
    print("el equipo A tuvo mejor rendimiento")
elif promedio_B > promedio_A:
    print("el equipo B tuvo mejor rendimiento")
else:
    print("los dos equipos tienen rendimientos iguales")


#5 largest PRODUCT BETWEEN TWO NUMBERS
print("EJERCICIO 5")
numer = list(map(int, input("ingrese 4 números (separadas por espacios): ").split()))
producto_max = 0

for i in range(len(numer)):
    for j in range(i + 1, len(numer)):
        producto = numer[i] * numer[j]
        if producto > producto_max:
            producto_max = producto
print("produto mas grande:", producto_max)


# 6 days to reach a savings goal
print("EJERCICIO 6")
meta = int(input("ingresa tu meta de ahorro:"))
dia = 1
total = 0
while total < meta :
    total += dia
    dia += 1
print(f"meta alcanzada en{dia - 1} dias")

# 7 PALINDROMO
print("EJERCICIO 7")

palindromo = input("ingrese un numero entero: ")

if palindromo == palindromo[:: -1]:
    print("Es un numero palíndromo")
else:
    print("No es un número palíndromo")

# 8
print("EJERCICIO 8")
numm = list(map(int, input("ingrese 4 números (separadas por espacios): ").split()))
for e in range(len(numm)):
    for d in range(e + 1, len(numm)):
        print(f"({numm[e]}, {numm[d]})")


# 9 
print("EJERCICIO 9")

import math
numero = int(input("Ingresa un número entero: "))

if numero < 2:
    print("No es primo")
else:
    es_primo = True
    
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")

# 10
print("EJERCICIO 10")
# Solicitar una lista de números al usuario
numeros = input("Ingresa una lista de números separados por comas: ")
lista = [int(x) for x in numeros.split(',')]

# Calcular la suma de los números pares
suma_pares = sum(num for num in lista if num % 2 == 0)

# Mostrar el resultado
print(f"Suma de los números pares: {suma_pares}")
