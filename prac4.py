#PROGRAMA PARA GANANCIAS DE “UIOTOVINO”

tipo_uva= input("ingres el tipo de uva (A/B): ").upper()
tipo_tamaño= int(input("ingrese el tipode tamaño (1/2): "))
kilos = float(input("ingrese la cantidad de kilos: "))
precio_kilo= float(input("ingrese el valor por kilo: "))

if tipo_uva== "A":
    if tipo_tamaño ==1:
        precio_final = (precio_kilo*kilos)+0.20
    elif tipo_tamaño ==2:
        precio_final = (precio_kilo*kilos)+0.30
elif tipo_uva =="B":
    if tipo_tamaño ==1:
        precio_final = (precio_kilo*kilos)-0.30
    elif tipo_tamaño == 2:
        precio_final = (precio_kilo*kilos)-0.50
else: 
    raise ValueError("tipo de uva no válida. intente de nuevo")

print(f"ganancia total para agricultor es de: {precio_final}")


