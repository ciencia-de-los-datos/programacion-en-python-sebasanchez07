"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def importar_datos(ruta_datos):
  with open(ruta_datos, "r") as archivo:
    datos_taller = archivo.readlines()
    datos_taller = [elemento.replace("\n", "") for elemento in datos_taller] 
    datos_taller = [elemento.split("\t") for elemento in datos_taller] 

  return datos_taller

datos = importar_datos(ruta_datos = "data.csv")

def variable(num):
    lista = []
    for i in range(len(datos)):
        lista.append(datos[i][num])
    return lista

def pregunta_01():
    lista = []
    for i in range(len(datos)):
      lista.append(int(datos[i][1]))
      resultado = sum(lista)

    return resultado


def pregunta_02():
    
    letras = ["A", "B", "C", "D", "E"]
    
    # Función 1: Seleccionar la columna 1
    def variable():
        lista = []
        for i in range(len(datos)):
            lista.append(datos[i][0])
        return lista

    # Función 2: Conteo para cada letra
    def suma_letra(letra):
        prueba = []
        for i in range(len(variable())):
            prueba.append(variable()[i] == letra)
        res = sum(prueba)
        
        return res

    # Función 3: Resultado final 
    def resultado(x):
        letra = []
        conteo = []
        
        for i in range(len(x)):
            letra.append(letras[i])
            conteo.append(suma_letra(letra = letras[i]))
            
        res = [
            (letra[0], conteo[0]),
            (letra[1], conteo[1]),
            (letra[2], conteo[2]),
            (letra[3], conteo[3]),
            (letra[4], conteo[4])
            ]
        return res
    
    return resultado(x = letras)


def pregunta_03():
    def variable(num):
        lista = []
        for i in range(len(datos)):
            lista.append(datos[i][num])
        return lista

    def sumacol2(letra):
        listaletras = []
        for i in range(len(variable(num = 0))):
            listaletras.append(variable(num = 0)[i] == letra)
        sumaletra = []
        for i in range(len(listaletras)):
            sumaletra.append(int(variable(num = 1)[i]) * listaletras[i])
        res = sum(sumaletra)
        return res 

    letras = ["A", "B", "C", "D", "E"]
    letra = []
    sumatoria = []
    for i in range(len(letras)):
        letra.append(letras[i])
        sumatoria.append(sumacol2(letra = letras[i]))
    
    resultado = [
        (letra[0], sumatoria[0]),
        (letra[1], sumatoria[1]),
        (letra[2], sumatoria[2]),
        (letra[3], sumatoria[3]),
        (letra[4], sumatoria[4])
    ]
    return resultado


def pregunta_04():
    def variable(num):
        lista = []
        for i in range(len(datos)):
            lista.append(datos[i][num])
        return lista

    mes = []
    for i in range(len(variable(num=2))):
        mes.append(variable(num=2)[i].split("-")[1])

    def suma_mes(x):
        prueba = []
        for i in range(len(mes)):
            prueba.append(mes[i] == x)
        res = sum(prueba)

        return res

    num_mes = []
    conteo = []
    meses = ["01", "02", "03", "04", "05", "06",
             "07", "08", "09", "10", "11", "12"]

    for i in range(len(meses)):
        num_mes.append(meses[i])
        conteo.append(suma_mes(x=meses[i]))

    res = [
        (num_mes[0], conteo[0]),
        (num_mes[1],  conteo[1]),
        (num_mes[2], conteo[2]),
        (num_mes[3], conteo[3]),
        (num_mes[4], conteo[4]),
        (num_mes[5], conteo[5]),
        (num_mes[6], conteo[6]),
        (num_mes[7], conteo[7]),
        (num_mes[8], conteo[8]),
        (num_mes[9], conteo[9]),
        (num_mes[10], conteo[10]),
        (num_mes[11], conteo[11])
    ]
    return res



def pregunta_05():
    from collections import Counter    
    with open( 'data.csv' , "r") as file:
        data = file.readlines()  
    data = [row.replace("\n", "") for row in data]
    data = [row.replace("\t", ",") for row in data]
    data = [row.split(",") for row in data]
    data = [row[0:2] for row in data]
    data = [(row[0], int(row[1])) for row in data] 
    respuesta =[(k, max([y for (x,y) in data if x == k]), min([y for (x,y) in data if x == k])) for k in dict(data).keys()]
    respuesta.sort(reverse = False) 

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return respuesta


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
