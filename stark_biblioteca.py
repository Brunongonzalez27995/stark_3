from data_stark import * 

def stark_normalizar_datos(lista:list) -> bool:

    modificado = False

    for heroe in lista:

        for clave in heroe:

            valor = heroe[clave]

            if clave == "altura" and type(valor) != float:
                heroe[clave] = float(valor)
                modificado = True
                
            elif clave == "peso" and type(valor) != float:
                heroe[clave] = float(valor)
                modificado = True

            elif clave == "fuerza" and type(valor) != int:
                heroe[clave] = int(valor)
                modificado = True

    return modificado

def obtener_dato(diccionario:dict, clave:str) -> bool or str or bool:

    retorno = False

    if diccionario != {} and clave in diccionario:

        dato = diccionario[clave]
        retorno = dato

    return retorno

def obtener_nombre(diccionario:dict) -> str or bool:

    retorno = False

    if diccionario != {} and "nombre" in diccionario:
        
        nombre = obtener_dato(diccionario, "nombre")
        nombre_formateado = ("Nombre: {0}".format(nombre))
        retorno = nombre_formateado
    
    return retorno
    
def obtener_nombre_y_dato(diccionario:dict, clave:str) -> str or bool:

    if diccionario != {}:

        dato = obtener_dato(diccionario, clave)
        nombre = obtener_nombre(diccionario)
        nombre_dato = "{0}|{1}: {2}".format(nombre, clave.capitalize(), dato)
        retorno = nombre_dato
    
    else:
        retorno = False
    
    return retorno

def obtener_maximo(lista:list, clave: str) -> int or float or bool:

    retorno = False

    if lista != []:

        maximo = lista[0][clave]
        
        for elemento in lista:  

            valor = elemento[clave]         

            if type(valor) == int or type(valor) == float:

                if valor > maximo:

                    maximo = valor

        retorno = maximo
                
    return retorno

def obtener_minimo(lista:list, clave: str) -> int or float or bool:

    retorno = False

    if lista != []:

        minimo = lista[0][clave]
        
        for elemento in lista:  

            valor = elemento[clave]         

            if type(valor) == int or type(valor) == float:

                if valor < minimo:
                    
                    minimo = valor

        retorno = minimo
                
    return retorno

def obtener_dato_cantidad(lista:list, numero:int or float, clave:str ) -> list or bool: 

    retorno = False

    if lista != []:

        lista_solicitada = []

        for elemento in lista:

            if clave in elemento:

                valor = elemento[clave]

                if valor == numero:
                    lista_solicitada.append(elemento)

        retorno = lista_solicitada
            
    return retorno

def stark_imprimir_heroes(lista:list) -> None or bool:

    retorno = False

    if lista != []:

        for diccionario in lista:

            if diccionario != {}:

                for clave in diccionario:

                    valor = diccionario[clave]

                    if type(valor) == str:

                        print("{0}: {1}".format(clave.capitalize(), valor.title()))

                    else:
                        
                        print("{0}: {1:.2f}".format(clave.capitalize(), valor))
        
        return retorno
                    
def sumar_dato_heroe(lista:list, clave:str) -> int or float:

    retorno = False
    suma_total = 0

    for elemento in lista:

        if elemento != {}:

            valor = elemento[clave]
            suma_total += valor
    
    retorno = suma_total

    return retorno

def dividir(dividendo:int or float, divisor:int or float) -> int or float or bool:

    retorno = False

    if divisor != 0:

            resultado = dividendo / divisor
            retorno = resultado

    return retorno

def calcular_promedio(lista:list, clave:str) -> int or float or bool:

    retorno = False

    if lista != []:

        suma_datos = sumar_dato_heroe(lista, clave)
        cantidad_elementos = len(lista)
        
        if cantidad_elementos > 0:

            resultado = dividir(suma_datos, cantidad_elementos)
            retorno = resultado

    return retorno

def mostrar_promedio_dato(lista:list, clave:str) -> bool or None:

    retorno = False
    datos_validados = False

    if lista != []:

        for elemento in lista:

            valor_clave = elemento[clave]

            if type(valor_clave) == int or type(valor_clave) == float:
                
                datos_validados = True
    
    if datos_validados == True:

        promedio = calcular_promedio(lista, clave)
        mensaje = print("El promedio de {0} es: {1:.2f}".format(clave, promedio))
        retorno = mensaje

    return retorno

def obtener_superheroes_por_genero(lista:list, clave:str) -> list or bool:

    retorno = False
    lista_masculinos = []
    lista_femeninos = []
    lista_nb = []

    if clave == "F" or clave == "M" or clave == "NB":

        for elemento in lista:

            genero = elemento["genero"]

            if genero == "F":
                
                lista_femeninos.append(elemento)
                
            elif genero == "M":

                lista_masculinos.append(elemento)
                
            elif genero == "NB":

                lista_nb.append(elemento)
               
    if clave == "F":

        retorno = lista_femeninos
        
    elif clave == "M":

        retorno = lista_masculinos

    elif clave == "NB":

        retorno = lista_nb

    return retorno

def imprimir_menu() -> str: 

    print('''
1. Mostrar heroes de género no binario.
2. Mostrar superhéroe más alto de género F
3. Mostrar superhéroe más alto de género M
4. Mostrar superhéroe más débil de género M
5. Mostrar superhéroe más débil de género NB
6. Mostrar fuerza promedio de los superhéroes de
género NB.
7. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
8. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
9. Listar todos los superhéroes agrupados por color de ojos.
10. Listar todos los superhéroes agrupados por tipo de inteligencia.
11. Salir de S.T.A.R.K III.          
''')
    
def validar_entero(cadena_a_validar:str):

    retorno = False

    if cadena_a_validar.isdigit() == True:

        retorno = True

    return retorno

def stark_menu_principal() -> bool or int:

    imprimir_menu()
    opcion = input("Ingrese una opción: ")

    if validar_entero(opcion) == True:

        opcion = int(opcion)
        retorno = opcion

    else:
        
        retorno = False

    return retorno

def contador_dato(lista:list, clave:str) -> dict or bool:

    dict_contador = {}
    retorno = False

    if lista != []:

        for elemento in lista:

            dato = obtener_dato(elemento, clave)
    
            if dato in dict_contador:

                dict_contador[dato] += 1

            else:

                dict_contador[dato] = 1

        retorno = dict_contador
    
    return retorno

def agrupar_por_clave(lista:list, clave:str, clave_a_guardar:str) -> dict:

    retorno = False
    diccionario_retorno = {}
    
    for elemento in lista:

        dato = obtener_dato(elemento, clave)
        
        if dato not in diccionario_retorno:
            diccionario_retorno[dato] = []
        
        diccionario_retorno[dato].append(elemento[clave_a_guardar])

    if diccionario_retorno != {}:

        retorno = diccionario_retorno
    
    return retorno

def stark_marvel_app(lista:list):

    normalizar = False

    while normalizar == False:

        opcion_normalizar = int(input("1. Normalizar datos.\n2. Salir de S.T.A.R.K III\nIntroduce una opción: "))

        if opcion_normalizar == 1:

            normalizar = stark_normalizar_datos(lista)

            if normalizar == True:
                print("Datos normalizados con éxito.\nBienvenido a S.T.A.R.K III")
            else:
                print("Ocurrió un error al normalizar los datos.")

        if opcion_normalizar == 2:
            print("Gracias por utilizar S.T.A.R.K III")
            break

    while normalizar == True:
            
        opcion = stark_menu_principal()

        if opcion == 1:

            lista_nb = obtener_superheroes_por_genero(lista_personajes, "NB")
            print("Heroes de género no binario: ")

            for heroe in lista_nb:

                nombre = obtener_nombre(heroe)
                print(nombre)

        elif opcion == 2:

            lista_mujeres = obtener_superheroes_por_genero(lista_personajes, "F")
            mayor_altura = obtener_maximo(lista_mujeres, "altura")
            lista_mas_altas = obtener_dato_cantidad(lista_mujeres, mayor_altura, "altura")
            stark_imprimir_heroes(lista_mas_altas)

        elif opcion == 3:

            lista_hombres = obtener_superheroes_por_genero(lista_personajes, "M")
            mayor_altura = obtener_maximo(lista_hombres, "altura")
            lista_mas_altos = obtener_dato_cantidad(lista_hombres, mayor_altura, "altura")
            stark_imprimir_heroes(lista_mas_altos)

        elif opcion == 4:

            lista_hombres = obtener_superheroes_por_genero(lista_personajes, "M")
            menor_fuerza = obtener_minimo(lista_hombres, "fuerza")
            lista_mas_debiles = obtener_dato_cantidad(lista_hombres, menor_fuerza, "fuerza")
            stark_imprimir_heroes(lista_mas_debiles)

        elif opcion == 5:

            lista_nb = obtener_superheroes_por_genero(lista_personajes, "NB")
            menor_fuerza = obtener_minimo(lista_nb, "fuerza")
            lista_mas_debiles = obtener_dato_cantidad(lista_nb, menor_fuerza, "fuerza")
            stark_imprimir_heroes(lista_mas_debiles)

        elif opcion == 6:

            lista_nb = obtener_superheroes_por_genero(lista_personajes, "NB")
            mostrar_promedio_dato(lista_nb, "fuerza")

        elif opcion == 7:

            colores = contador_dato(lista_personajes, "color_ojos")

            for color in colores: 
                print("Color de ojos: {0} Cantidad de heroes que lo tienen: {1}".format(color, colores[color]))

        elif opcion == 8:

            colores = contador_dato(lista_personajes, "color_pelo")

            for color in colores: 
                
                print("Color de pelo: {0} Cantidad de heroes que lo tienen: {1}".format(color, colores[color]))

        elif opcion == 9:

            diccionario = agrupar_por_clave(lista_personajes, "color_ojos", "nombre")

            for clave in diccionario:

                print("Color de ojos: {0}".format(clave))

                for nombre in diccionario[clave]:

                    print("-{0}".format(nombre))

        elif opcion == 10:

            diccionario = agrupar_por_clave(lista_personajes, "inteligencia", "nombre")

            for clave in diccionario:

                print("Tipo de inteligencia: {0}".format(clave))

                for nombre in diccionario[clave]:

                    print("-{0}".format(nombre))

        elif opcion == 11:

            print("Gracias por utilizar S.T.A.R.K. III")
            break

        else:

            print("Debe introducir una opción valida (1-10).")