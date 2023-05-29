#Desafío 4: La inmobiliaria
#Requisitos técnicos:
#- Operadores.
#- Estructuras de datos.
#- Estructuras de control de flujo.
#- Funciones
# Integrantes: 
#               Agustín, Leiva
#               Joaquín  Meca
#               Nehemias Octavio  Ocampo Mitoire
#               Lucía  Morel
#               Marcelo Antonio, Murad
#               Luciano, Ertle
#               Alexis Matias, Calderon
#               Antonio, Flores
#               Lourdes Eliana, Baez
#               Nahuel, Sanchez
#               Ricardo Alexandro, Mena

import datetime
hora_actual = datetime.datetime.now().hour

def agregar_inmueble(lista):
    nuevo_registro = {}
    
    while True:
        anno = int(input("Ingrese el año (no puede ser anterior al 2000): "))
        if anno >= 2000:
            nuevo_registro['año'] = anno
            break
        else:
            print("No se opera con inmuebles anteriores al año 2000.")
    
    while True:
        metros = int(input("Ingrese la superficie en metros (no puede ser menor a 60m²): "))
        if metros >= 60:
            nuevo_registro['metros'] = metros
            break
        else:
            print("No se opera con inmuebles menores a 60m2.")
    
    while True:
        habitaciones = int(input("Ingrese el número de habitaciones (no puede ser menor a 2): "))
        if habitaciones >= 2:
            nuevo_registro['habitaciones'] = habitaciones
            break
        else:
            print("No se opera con inmuebles cuyo número de habitaciones sea menor a 2.")
    
    garage = input("Ingrese si incluye garage (True o False): ")
    nuevo_registro['garaje'] = bool(garage)
    
    while True:
        zona = input("Ingrese la zona (A, B o C): ")
        if zona in ['A', 'B', 'C']:
            nuevo_registro['zona'] = zona
            break
        else:
            print("Solo se permite ingresar las zonas A, B o C.")
    
    while True:
        estado = input("Ingrese el estado (Disponible, Reservado o Vendido): ")
        if estado in ['Disponible', 'Reservado', 'Vendido']:
            nuevo_registro['estado'] = estado
            break
        else:
            print("Solo se permite los siguientes estados: Disponible, Reservado o Vendido.")
    
    lista.append(nuevo_registro)
    print("Se agregó el inmueble a la lista.")

def editar_inmueble(lista, indice):
    if indice >= 0 and indice < len(lista):
        inmueble = lista[indice]
        print("Ingrese los nuevos datos del inmueble:")
        agregar_inmueble(lista)
        lista[indice] = inmueble
        print("El inmueble se actualizó")
    else:
        print("El índice no es válido.")

def eliminar_inmueble(lista, indice):
    if indice >= 0 and indice < len(lista):
        del lista[indice]
        print("El inmueble se ha eliminado de la lista.")
    else:
        print("El índice no es válido.")

def cambiar_estado_inmueble(lista, indice, nuevo_estado):
    if indice >= 0 and indice < len(lista):
        lista[indice]['estado'] = nuevo_estado
        print("El estado del inmueble se actualizó.")
    else:
        print("El índice no es válido.")

def buscar_inmuebles_por_presupuesto(lista, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista:
        if (inmueble['estado'] == 'Disponible' or inmueble['estado'] == 'Reservado') and calcular_precio_inmueble(inmueble) <= presupuesto:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = calcular_precio_inmueble(inmueble)
            inmuebles_encontrados.append(inmueble_con_precio)
    return inmuebles_encontrados

def calcular_precio_inmueble(inmueble):
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    antiguedad = 2023 - inmueble['año']
    zona = inmueble['zona']

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2
    
    return precio

# ESTRUCTURA PRINCIPAL DEL PROGRAMA

inmobiliaria = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]

salir = False

while not salir:
    print("MENÚ PRINCIPAL DEL PROGRAMA")
    print("1. Agregar, editar y eliminar inmuebles a la lista")
    print("2. Cambiar el estado de un inmueble")
    print("3. Hacer búsqueda de inmuebles en función de un presupuesto")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    print()
    
    if opcion == '1':
        print("SUBMENÚ AGREGAR/EDITAR/ELIMINAR INMUEBLE")
        print("¿Qué desea hacer?")
        print("1. Agregar un inmueble a la lista")
        print("2. Editar un inmueble existente en la lista")
        print("3. Eliminar un inmueble de la lista")
        print("4. Volver al Menú principal")
        print()
        subopcion = input("Elige una opción: ")
        print()
        
        if subopcion == '1':
            agregar_inmueble(inmobiliaria)
        elif subopcion == '2':
            indice = int(input("Ingrese el índice del inmueble a editar: "))
            editar_inmueble(inmobiliaria, indice)
        elif subopcion == '3':
            indice = int(input("Ingrese el índice del inmueble a eliminar: "))
            eliminar_inmueble(inmobiliaria, indice)
        elif subopcion == '4':
            salir
        else:
            print("Opción inválida")
    
    elif opcion == '2':
        print("CAMBIAR ESTADO DE UN INMUEBLE")
        print("Lista de inmuebles:")
        for i, inmueble in enumerate(inmobiliaria):
            print(f"Índice: {i}, Inmueble: {inmueble}")
        indice = int(input("Ingrese el índice del inmueble a modificar: "))
        nuevo_estado = input("Ingrese el nuevo estado del inmueble: ")
        cambiar_estado_inmueble(inmobiliaria, indice, nuevo_estado)
        for i, inmueble in enumerate(inmobiliaria):
            print(f"Índice: {i}, Inmueble: {inmueble}")
    
    elif opcion == '3':
        presupuesto = float(input("Ingrese su presupuesto: "))
        inmuebles_encontrados = buscar_inmuebles_por_presupuesto(inmobiliaria, presupuesto)
        if inmuebles_encontrados:
           print("Inmuebles encontrados:")
           for inmueble in inmuebles_encontrados:
            print(inmueble)
        else:
            print("No se encontraron inmuebles para el rpesupuesto ingresado")
    
    elif opcion == '4':
        salir = True
    
    else:
        print("Opción inválida")
    
    print()


if 6 <= hora_actual < 12:
    print("Gracias por usar nuestros servicios, Que tenga buenos días")
elif 12 <= hora_actual < 19:
    print("Gracias por usar nuestros servicios, Que tenga buenas tardes")
else:
    print("Gracias por usar nuestros servicios, Que tenga buenas noches")