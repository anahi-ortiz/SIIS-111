def calcular_salario_neto():
    #1. ingresar salario bruto y porcentaje
    salario_bruto = float(input("ingrese el salario bruto: "))
    #impuesto al valor agregado
    iva_procentaje = 13
    # impuesto a la transferencia 
    it_porcentaje = 3

    #calcular las deducciones
    deduccion_iva = (salario_bruto * (iva_procentaje / 100))
    deduccion_it = (salario_bruto * (it_porcentaje))
    deducciones = deduccion_iva + deduccion_it

    #restar las deducciones al salario bruto
    salario_neto = salario_bruto - deducciones

    #mostrar el salario neto
    print(f"salario Bruto:{salario_bruto}")
    print(f"Total deducciones (IVA): {deduccion_iva}")
    print(f"total deducciones (IT): {deduccion_it}")
    