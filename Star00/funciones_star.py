from funcionesListas  import *
def mostrar_hero(hero: dict):
    """
    Muestra los detalles de un héroe.

    Parámetros:
    hero (dict): Un diccionario que contiene los detalles de un héroe.

    Retorna:
    None
    """
    print(f'{hero["nombre"]:20}  \t {hero["identidad"]:30} {hero["empresa"]:20} {hero["altura"]:0.5}\t {hero["peso"]:0.5}\t {hero["genero"]:5} {hero["color_ojos"]:30} {hero["color_pelo"]:20} {hero["fuerza"]:10}  {hero["inteligencia"]:10}')


def mostrar_todos_hero(heros: list):
    """
    Muestra todos los héroes en una lista.

    Parámetros:
    heros (list): Una lista que contiene diccionarios de héroes.

    Retorna:
    None
    """
    print("       ***Lista de SuperHéroes***")
    print(" nombre                          Identidad                   Empresa         Altura     Peso  Genero   color_ojos                   color_pelo         Fuerza         inteligencia      ")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(len(heros)):
        mostrar_hero(heros[i])


def recorre_lista(lista: list):
    """
    Recorre una lista de héroes e imprime solo sus nombres.

    Parámetros:
    lista (list): Una lista que contiene diccionarios de héroes.

    Retorna:
    None
    """
    for nombre in lista:
        print(f'hero: {nombre["nombre"]}')


def Mostrar_nombre_altura(lista: list):
    """
    Muestra el nombre y la altura de los héroes en una lista.

    Parámetros:
    lista (list): Una lista que contiene diccionarios de héroes.

    Retorna:
    None
    """
    for dato in lista:
        print(f'hero: {dato["nombre"]:10} \t  su altura : {dato["altura"]:0.5}')


def hero_mas_alto(lista: list):
    """
    Muestra el héroe más alto de una lista.

    Parámetros:
    lista (list): Una lista que contiene diccionarios de héroes.

    Retorna:
    None
    """
    mayor_altura = []
    for dato in lista:
        altura = float(dato["altura"])
        mayor_altura.append(altura)
        mayor = calcularmayorV4(mayor_altura)

    for dato in lista:
        if float(dato["altura"]) == mayor:
            print(f"\nEl personaje más alto es : {dato['nombre']} con  :{mayor}  ")


def hero_mas_bajo(lista: list):
    """
    Muestra el héroe más bajo de una lista.

    Parámetros:
    lista (list): Una lista que contiene diccionarios de héroes.

    Retorna:
    None
    """
    altura_lista = []
    for dato in lista:
        altura = float(dato["altura"])
        altura_lista.append(altura)
        menor = calcular_menor(altura_lista)

    for dato in lista:
        if float(dato["altura"]) == menor:
            print(f"\nEl personaje más bajo es : {dato['nombre']:15} con :{menor} ")


def promediar_altura(lista: list):
    """
    Calcula y muestra el promedio de la altura de los héroes en una lista.

    Parámetros:
    lista (list): Una lista que contiene diccionarios de héroes.

    Retorna:
    None
    """
    prom_lista = []
    for dato in lista:
        altura = float(dato["altura"])
        prom_lista.append(altura)
    
    print(f"El promedio de las alturas es: {CalcularPromedio(prom_lista):00.4}")


def mostar_mas_menos_pesado(lista: list):
    """
    Muestra el héroe más pesado y el más ligero de una lista.

    Parámetros:
    lista (list): Una lista que contiene diccionarios de héroes.

    Retorna:
    None
    """
    peso_lista = []
    for dato in lista:
        peso = float(dato["peso"])
        peso_lista.append(peso)
        mayor = calcularmayorV4(peso_lista)
        menor = calcular_menor(peso_lista) 

    for dato in lista:
        if float(dato["peso"]) == menor:
            print(f"El menos pesado es {dato['nombre']} con: {menor}")
        elif float(dato["peso"]) == mayor:
            print(f"El más pesado es {dato['nombre']} con: {mayor}")
