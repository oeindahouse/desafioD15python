preguntas = { 
            "Cuál es el mamífero más grande?" : "ballena",
            "Cómo se llama el satélite terrestre?" : "luna",
            "Cómo se llama el medio de transporte donde se debe pedalear para avanzar?" : "bicicleta",
            "Cuál es el primer nombre del último presidente de Chile que falleció":"sebastian",
            "Cuál es el nombre del primer elemento de la tabla periodica" : "hidrogeno",
            "Cuál es el nombre del lenguaje de programación del actual curso Full Stack" : "python",
            "Cuál es el nombre del movimiento de la tierra que da origen día/noche" : "rotación",
            "Escriba con palabras el número de componentes del agua" : "dos",
            "Cúal es el nombre del año cuándo febrero tiene 29 días?" : "bisiesto",
            }

puntaje = 0

for pregunta,respuesta in preguntas.items():
    print(pregunta)
    respuesta_user = str(input("ingrese su respuesta:"))
    
    if respuesta_user.lower() == respuesta.lower():
        print("correcto")
        puntaje +=1
    else:
        print(f"error, la respuesta :")
print(f"fin de la trivia, tu puntaje es: {puntaje} puntos")