from funciones_star01 import *

from data_stark import *







CampoA= "altura"
CampoG= "genero"

GeneroF = "F"
GeneroM = "M"

campoPelo = "color_pelo"
campoOjo = "color_ojos"
color = "Brown"

campoInt = "inteligencia"
inteligencia = "average"

# listar_super(lista_personajes,"color_pelo")




while True:
    respuesta = int(input("1.nombre de cada superhéroe de género M \
                          \n2.nombre de cada superhéroe de género F\
                          \n3.superhéroe más alto de género M\
                          \n4.superhéroe más alto de género F\
                          \n5.superhéroe más bajo de género M\
                          \n6.superhéroe más bajo de género F\
                          \n7.altura promedio de los superhéroes de género M\
                          \n8.altura promedio de los superhéroes de género F\
                          \n9. cuántos superhéroes tienen cada tipo de inteligencia\
                          \n10.cuántos superhéroes tienen cada tipo de color de ojos\
                          \n11.cuántos superhéroes tienen cada tipo de color de pelo\
                          \n12.cuántos superhéroes tienen cada tipo de inteligencia\
                          \n\
                          \nelija una opcion:"))
    print("---------------------------------------------------------------------------")
    
    match respuesta:
        case 1:
            
            print("A")
            Mostrar_nombre_campo(lista_personajes,CampoG,GeneroM)
            print("---------------------------------------------")
        case 2:
            print("B")
            Mostrar_nombre_campo(lista_personajes,CampoG,GeneroF)

            print("---------------------------------------------")
        case 3:
            print("C")
            mostrar_maximo_minimo_super(lista_personajes,CampoA,CampoG,GeneroM,False)
            print("---------------------------------------------")
        case 4:
            print("D")
            mostrar_maximo_minimo_super(lista_personajes,CampoA,CampoG,GeneroF,False)
            print("---------------------------------------------")
        case 5:
            print("E")
            mostrar_maximo_minimo_super(lista_personajes,CampoA,CampoG,GeneroM)   
            print("---------------------------------------------")
        case 6:
            print("F")
            mostrar_maximo_minimo_super(lista_personajes,CampoA,CampoG,GeneroF)
            print("---------------------------------------------")
        case 7:
            print("G")
            promediar_hero(lista_personajes,CampoA,CampoG,GeneroM)
            print("---------------------------------------------")
        case 8:
            print("H")
            promediar_hero(lista_personajes,CampoA,CampoG,GeneroF)
            print("---------------------------------------------")
        case 9:
            print("L")
            Mostrar_tipo(lista_personajes,"inteligencia")
            print("---------------------------------------------")

        case 10:
            print("M")
            listar_super(lista_personajes,"color_ojos")
            print("---------------------------------------------")

        case 11:
            print("N")
            listar_super(lista_personajes,"color_pelo")
            print("---------------------------------------------")

        case 12:
            print("O")
            listar_super(lista_personajes,"inteligencia")
            print("---------------------------------------------")

        case 13:
            break