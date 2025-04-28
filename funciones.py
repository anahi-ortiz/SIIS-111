def nombre_funcion1():
    print("salida de funcion 1")


def nombre_funcion2():
    print("salida de funcion 2")

def funcion_retorno():
    variable = 456
    return 123


def otener_edad ():
    edad = int(input("indique su edad: "))
    if (edad > 0):
        return edad
    else:
        return 0
    
def habilitado_brevet(hedad):
    if(hedad ==0): return "solo positivos"

    if(hedad >= 18):
        return "verdadero"
    else:
        return "falso"

def cualcular_descuento_producto():
    precio_original =100
    descuento = 20
    precio_descuento = (precio_original * descuento)/100
    precio_final = precio_original - precio_original
    return precio_final
def calcular_descuento_producto_mejorado(precio_original, descuento):
    precio_descuento = (precio_original * descuento)/100
    precio_final = precio_original - precio_descuento
    return precio_final
def calcular_descuento_producto_mejorado_x2(precio_original, descuento):
    return precio_original - (precio_original* descuento)/100

def calcular_descuento_producto_mejorado_x3(precio_original, descuento):
    return precio_original * (1 - descuento /100)

# 1 edad minima votar
def edad_minima_votar():
    print("la edad minima para votar es de 18 años")

# mayor entre dos numeros
def mayor_de_dos_numeros(numA, numB):
    if(numA == numB): "iguales"

    if (numA > numB):
        return numA
    else:
        return numB

def mayor_de_dos_numeros_mejorado(numA, numB):
    if(numA == numB): "iguales"

    return numA if (numA > numB) else numB

#algoritmo base
def recorrer_digitos(num):
    while(num > 0):
        dig = num % 10
        print(dig)
        num = num //10
#par/impar de los dig de un num
def par_impar_dig(num):
    while(num > 0):
        dig = num % 10
        print(dig)
        var_temp = "par" if(dig % 2 == 0) else "impar"
        print(var_temp)
        num = num //10
def suma_digitos_num(num):
    suma = 0
    while(num > 0):
        dig = num % 10
        suma = suma + dig
        num = num // 10
    return suma

#salida consula

#par_impar_dig(78234)

var_suma = suma_digitos_num(78234)
print(var_suma)










#edad_minima_votar()
#var_numA = int(input("ingrese el numero A: "))
#var_numB = int(input("ingrese el numero B: "))
#var_nummayor = mayor_de_dos_numeros_mejorado(var_numA, var_numB)
#print(var_nummayor)