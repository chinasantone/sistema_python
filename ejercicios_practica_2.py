# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open('stock.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    row = data[0]
    cantidad_filas = len(data)
    suma_stock = []
    for i in range(cantidad_filas):
        row = data[i]
        tornillos = int(row.get('tornillos'))
        suma_stock.append(tornillos)
    suma_total_stock = sum(suma_stock)
    print('el stock total de tornillos es igual a ', suma_total_stock)



        
    
         
        


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'
    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    row = data[0]
    cantidad_filas = len(data)
    departamentos_2amb = 0
    departamentos_3amb = 0

    for i in range(cantidad_filas):  # --> recorre la lista de departamentos 
        departamento = data[i]
        for k,v in departamento.items():    # --> recorre los departamentos
            if v == '2':
                departamentos_2amb += 1
            elif v == '3':
                departamentos_3amb += 1
    print('la cantidad de deperatamentos de dos ambientes es :', departamentos_2amb)            
    print('la cantidad de deperatamentos de tres ambientes es :', departamentos_3amb)   
            
    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
