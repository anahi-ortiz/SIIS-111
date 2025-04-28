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