"""
A. Analizar detenidamente el set de datos
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
la altura del mismo
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F. Recorrer la lista y determinar la altura promedio de los superhéroes
(PROMEDIO)
G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
I. Ordenar el código implementando una función para cada uno de los valores
informados.
J. Construir un menú que permita elegir qué dato obtener
"""
from data_stark import *
from funciones_star import *

while True:
    respuesta = int(input("1.Datos de los super\n2.nombres de los personajes \n3.super con su altura\n4.super mas alto\n5.super mas bajo\n6.promedio de altura de los super\n7.super mas y menos alto\n8.salir\n elija una opcion:"))
    print("---------------------------------------------")
    
    match respuesta:
        case 1:
            print("A")
            mostrar_todos_hero(lista_personajes)
            print("---------------------------------------------")
        case 2:
            print("B")
            recorre_lista(lista_personajes)
            print("---------------------------------------------")
        case 3:
            print("C")
            Mostrar_nombre_altura(lista_personajes)
            print("---------------------------------------------")
        case 4:
            print("D")
            hero_mas_alto(lista_personajes)
            print("---------------------------------------------")
        case 5:
            print("E")
            hero_mas_bajo(lista_personajes)    
            print("---------------------------------------------")
        case 6:
            print("F")
            promediar_altura(lista_personajes)
            print("---------------------------------------------")
        case 7:
            print("H")
            mostar_mas_menos_pesado(lista_personajes)
            print("---------------------------------------------")
        case 8:
            break