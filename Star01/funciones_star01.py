from funcionesListas01 import *

# def mostrar_hero(hero:dict):
#     print(f'{hero["nombre"]:20}  \t {hero["identidad"]:30} {hero["empresa"]:20} {hero["altura"]:0.5}\t {hero["peso"]:0.5}\t {hero["genero"]:5} {hero["color_ojos"]:30} {hero["color_pelo"]:20} {hero["fuerza"]:10}  {hero["inteligencia"]:10}')

# def mostrar_todos_hero(heros:list):
#     print("       ***lista de SuperHeroes**")
#     print(" nombre                          Identidad                   Empresa         Altura     Peso  Genero   color_ojos                   color_pelo         Fuerza         inteligencia      ")
#     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#     for i in range(len(heros)):
#         mostrar_hero(heros[i])


# def mostar_super_mayor(lista: list,campo_uno,campo_dos,keys):
#     mayor_lista = []
#     for dato in lista:
#         if dato[campo_dos] == keys:    
#             aux = float(dato[campo_uno])
#             mayor_lista.append(aux)
#             mayor = calcularMayor(mayor_lista)

#     for dato in lista:
#         if float(dato[campo_uno]) == mayor and dato[campo_dos] == keys:
#             print(f"\nEl personaje mas alto es : {dato['nombre']} con  :{mayor}  ")       
    
# def mostar_super_menor(lista: list,campo_uno,campo_dos,keys):
#     menor_lista = []
#     for dato in lista:
#         if dato[campo_dos] == keys:    
#             aux = float(dato[campo_uno])
#             menor_lista.append(aux)
#             menor = calcular_menor(menor_lista)

#     for dato in lista:
#         if float(dato[campo_uno]) == menor and dato[campo_dos] == keys:
#             print(f"\nEl personaje mas bajo es : {dato['nombre']:15} con :{menor} ")  


def Mostrar_nombre_campo(lista, campo, keys):
    """
    Muestra los nombres de los héroes cuyo campo específico coincide con el valor proporcionado.

    Parámetros:
    lista (list): La lista de datos que contiene los héroes.
    campo (str): El campo específico que se utilizará para la comparación.
    keys: El valor que se utilizará para comparar el campo especificado.

    """
    if not isinstance(lista, list):
        raise TypeError("El argumento 'lista' debe ser una lista.")
    for dato in lista:
        if dato[campo] == keys:
            print(f'hero: {dato["nombre"]:10} \t  {campo} : {dato[campo]}')


def mostrar_maximo_minimo_super(lista, campo_uno, campo_dos, keys, valor: bool = True):
    """
    Muestra el héroe más alto o más bajo según el campo especificado.

    Parámetros:
    lista (list): La lista de datos que contiene los héroes.
    campo_uno (str): El campo específico que se utilizará para determinar la altura.
    campo_dos (str): El campo específico que se utilizará para filtrar los héroes.
    keys: El valor que se utilizará para comparar el campo_dos.
    valor (bool): Un valor booleano que indica si se busca el máximo (True) o el mínimo (False).


    """
    if not isinstance(lista, list):
        raise TypeError("El argumento 'lista' debe ser una lista.")
    aux_lista = []
    for dato in lista:
        if dato[campo_dos] == keys:    
            aux = float(dato[campo_uno])
            aux_lista.append(aux)
            if valor:
                maxmin = calcular_menor(aux_lista)
            else:
                maxmin = calcularMayor(aux_lista)

    for dato in lista:
        if float(dato[campo_uno]) == maxmin and dato[campo_dos] == keys:
            print(f"\nEl personaje {'más bajo' if valor else 'más alto'} es: {dato['nombre']:15} con: {maxmin} ")  


def promediar_hero(lista: list, campo_uno, campo_dos, genero):
    """
    Calcula el promedio de la altura de los héroes de un género específico.

    Parámetros:
    lista (list): La lista de datos que contiene los héroes.
    campo_uno (str): El campo específico que se utilizará para determinar la altura.
    campo_dos (str): El campo específico que se utilizará para filtrar los héroes.
    genero: El género de los héroes para el cual se calculará el promedio de la altura.

    """
    if not isinstance(lista, list):
        raise TypeError("El argumento 'lista' debe ser una lista.")
    prom_lista = []
    for dato in lista:
        if dato[campo_dos] == genero:        
            altura = float(dato[campo_uno])
            prom_lista.append(altura)
    
    print(f"El promedio de altura de {genero} es: {CalcularPromedio(prom_lista):00.4}")


def mostar_mas_menos_pesado(lista, campo):
    """
    Muestra el héroe más pesado y el menos pesado.

    Parámetros:
    lista (list): La lista de datos que contiene los héroes.
    campo (str): El campo específico que se utilizará para determinar el peso.

    """
    if not isinstance(lista, list):
        raise TypeError("El argumento 'lista' debe ser una lista.")
    peso_lista = []
    for dato in lista:
        peso = float(dato[campo])
        peso_lista.append(peso)
        mayor = calcularMayor(peso_lista)
        menor = calcular_menor(peso_lista) 

    for dato in lista:
        if float(dato["peso"]) == menor:
            print(f"El menos pesado es {dato['nombre']} con: {menor}")
        elif float(dato["peso"]) == mayor:
            print(f"El más pesado es {dato['nombre']} con: {mayor}")
            

def Mostrar_tipo(lista: list, campo):
    """
    Muestra la cantidad de héroes según el tipo especificado en un campo.

    Parámetros:
    lista (list): La lista de datos que contiene los héroes.
    campo (str): El campo específico que se utilizará para determinar el tipo.

    """
    if not isinstance(lista, list):
        raise TypeError("El argumento 'lista' debe ser una lista.")
    datos = set([dato[campo] if dato[campo] else "no tiene" for dato in lista])

    for valor in datos:
        contador = 0
        for dato in lista:
            if (dato[campo] == valor) or (dato[campo] == "" and valor == "no tiene"):  
                contador += 1         

        print(f'{contador} elementos con {campo} {valor}')


def ordenar_campos(lista, campo):
    """
    Ordena una lista de datos según un campo específico.

    Parámetros:
    lista (list): La lista de datos que se ordenará.
    campo (str): El campo específico según el cual se realizará el ordenamiento.

    """
    if not isinstance(lista, list):
        raise TypeError("El argumento 'lista' debe ser una lista.")
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][campo] > lista[j][campo]:
                swap_lista(lista, i, j)


def listar_super(lista: list, campo):
    """
    Lista los héroes agrupados por el campo especificado.

    Parámetros:
    lista (list): La lista de datos que contiene los héroes.
    campo (str): El campo específico que se utilizará para agrupar los héroes.
    """
    if not isinstance(lista, list):
        raise TypeError("El argumento 'lista' debe ser una lista.")    
    aux = filtrar_lista(lambda auxs: auxs[campo], lista)
    ordenar_campos(aux, campo)

    datos_unicos = set([datos[campo].strip().lower() for datos in aux if datos[campo].strip()])
 
    for valor in datos_unicos:
        print(f"-{valor}") 

        for dato in aux:
            if dato[campo].strip().lower() == valor:
                print(f"     {dato['nombre']}")



# -----------------------------------------------------------
def obtener_path_actual(nombre_archivo):
    """
    Obtiene la ruta del archivo actual.

    Parámetros:
    nombre_archivo (str): El nombre del archivo al que se le desea obtener la ruta.

    Retorna:
    str
    """
    import os
    path = os.path.dirname(__file__)
    return os.path.join(path, nombre_archivo)
# -----------------------------------------------------------