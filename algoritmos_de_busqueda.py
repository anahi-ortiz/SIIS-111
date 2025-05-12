precios = [400, 250, 310, 280]
menor = precios[0]

for precio in precios:
    if precio < menor:
        menor = precio

#print(menor)

def precio_menor(precios):
    menor = precios[0]

    for precio in precios:
        if precio < menor:
            menor = precio
    return menor

precios = [400, 250, 310, 280]
print(precio_menor(precios))






#busqueda binaria
def busqueda_binaria(lista, objetivos):
    izquierda = 0
    derecha = len(lista) -1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivos:
            return medio
        elif lista[medio] < objetivos:
            izquierda = medio +1
        else:
            derecha = medio -1
    return -1

datos = [12, 23, 34, 45, 67]
buscado = 45
posicion = busqueda_binaria(datos, buscado)

if posicion != -1:
    print(f"ELEMENTO ENCONTRADO EN LA POSICION: {posicion}")
else:
    print("ELEMENTO NO ENCONTRADO")

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

#---------------------------------------------------
datos = [23, 45, 12, 67, 34]
buscado = 67

posicion = busqueda_lineal(datos, buscado)

if posicion != -1:
    print(f"elemento encontrado en la posicion: {posicion}")
else:
    print("elemento no encontrado")

