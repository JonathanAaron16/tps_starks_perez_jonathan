from random import *





def duplicar(numero):
    numero = numero *2

# numero =20

# duplicar()

def duplicar_valores(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2


def mostrarLista(lista:list)->None:
    for el in lista:
        print(el, end=" ")
    print()

def cargarListaEnterosRandom(lista:list, cant:int,desde:int,hasta:int):
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde,hasta))

def CrearListaEnterosRandom(cant:int,desde:int,hasta:int):
    # from random import randint
    lista = []
    # for _ in range(cant):# se usa el _ para no tener que usar esa variable
    #     lista.append(randint(desde,hasta))
    cargarListaEnterosRandom(lista,cant,desde,hasta)

    return lista

def totalizarLista(lista:list):
    total = 0
    for valor in lista:
        total += valor

    return  total

def CalcularPromedio(lista:list):
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError ("no esta definido el priomedio en una lista vacia")
        
        return totalizarLista(lista) / cant  
    raise ValueError ("no es una lista")


def calcularMayor(lista:list):
    if isinstance (lista, list):
        if len(lista)== 0:    
            raise ValueError ("la lista esta vacia") 
       
        mayor = lista[0]
        for i in range(1, len(lista)):
            if lista[i] > mayor:
                mayor = lista[i]
        return mayor
    
    

def calcular_menor(lista:list):
# calular normal

    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
        return menor
    # menor = lista[0]
    # for elemento in lista[1:]:
    #     if len(elemento) < len(menor):
    #         menor = elemento
    # return menor

#calcula por rango    
    # if isinstance (lista, list):
    #     if len(lista)== 0:    
    #         raise ValueError ("la lista esta vacia") 
       
    #     mayor = lista[0]
    #     for i in range(1, len(lista)):
    #         if len(lista[i]) < len(mayor):
    #             mayor = lista[i]
    #     return mayor


    

def enteroInLista(lista:list, target:int)->bool:
    if validar_lista(lista):
        return buscaInLista(lista,target) != -1
#---------------------------------------------------------------------------------------


def buscaInLista(lista:list,target:int)-> int:
    # está en la posicion tal
    posicion = -1
    if not isinstance(lista, list):
        raise TypeError("no es una lista")
    
    for i in range(len(lista)):
        if lista[i] == target:
            posicion = i
            break
    return posicion
        
  
        

def contarInLista(lista:list,target:any)-> int:
  #contar cuantas se repite
    if not isinstance(lista, list):
        raise TypeError("no es una lista")
    
    contador = 0
    for valor in lista:
        if valor == target:
            contador += 1
    return contador

def sorteador(lista:list)->None:
    import time
    if not isinstance(lista, list):
        raise TypeError("no es una lista")
    
    time.sleep(3)
    indice = randint(0, len(lista )- 1)
    print (f"el ganador es is {lista[indice]}")
    
def validar_lista(lista:list)->bool:
    if not isinstance(lista, list):
        raise TypeError("se esperaba una lista")
    return True
    

def ordenarListaAscedente(lista:list)->None:
    tam = len(lista)
    for i in range(tam -1):
        for j in range(i + 1, tam): 
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista    
        
def ordenarListaDescendente(lista:list)->None:
    tam = len(lista)
    for i in range(tam -1):
        for j in range(i + 1, tam): 
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def swap_lista(lista:list, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


# def ordenarLista(Lista:list,orden)->None:
#     if not isinstance(Lista, list):
#         raise TypeError("no es una lista")
    
#     if orden == 1:
#         validar = ordenarListaAscedente(Lista) 
#     elif orden == 2:
#         validar =ordenarListaDescendente(Lista)
#     return validar

def ordenarListaV2(lista:list,asc:bool= True)->None:
    tam = len(lista)
    for i in range (tam - 1):
        for j in range (i + 1, tam):
            if lista[i] > lista[j] if asc else lista[i] < lista[j]:
               swap_lista(lista,i,j)

def mapear_lista(procesadora, lista:list):
    lista_retorno= []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno


def mapear_campo(lista:list,campo:str):
    lista_retorno= []
    for el in lista:
        lista_retorno.append(el[campo])
    return lista_retorno

def filtrar_lists(lista, campo, valor):
    lista_retorno= []
    for el in lista:
        if el[campo] == valor:
            lista_retorno.append(el)
    return lista_retorno

def filtrar_lista(funcion, lista):
    lista_retorno= []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno