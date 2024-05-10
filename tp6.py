#1. Escriba una función redondear() que permita redondear un número decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el entero siguiente (en este caso, 4), si no devolver el entero inmediatamente anterior (3).

"""def redondear(numero):
    if (numero - int(numero)) < 0.5:
        return int(numero)
    else:
        return int(numero) + 1

numero = input("Ingrese un número decimal: ")
numero = float(numero)

print(redondear(numero))"""

#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un módulo que esté fuera de ese paquete, cree una función de suma de decimales que redondee el resultado haciendo uso de la función redondear() del paquete recién creado.
"""import tp6_2

numero1= float(input("ingrese un numero: "))
numero2= float(input("ingrese otro numero: "))

resultado= numero1+numero2

print(tp6_2.redondear(resultado))"""

#3. Usando el módulo datetime, escribe un programa que muestre la fecha y hora actuales del sistema
"""import datetime

dia=datetime.datetime.now()

print(dia)"""

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10 (pista: para comprobar si se pueden generar todos los números, pruebe ejecutar el programa dentro de un ciclo infinito).

"""import random

while True:
    numeros=[2,3,4,5,6,7,8,9,10]
    devolver_numero=input("devolver un numero? si/no: ")
    if devolver_numero=="si":
        numero_azar=random.choice(numeros)
        print (numero_azar)
    else:
        print("saliendo")
        break"""


#5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado para la adivinación o para buscar consejo. Su mecanismo es muy simple: ante una pregunta del usuario, la bola responde con una de 8 posibles

"""import random
while True:
    pregunta=input("ingrese pregunta (si quiere salir, ingresar salir): ")
    respuestas=["Es seguro que si","Las chances son buenas", "Puedes contar con ello", "Pregúntame de nuevo más tarde", "Concéntrate y pregunta de nuevo", "No veo con claridad, intenta de nuevo", "Mi respuesta es no", "Mis fuentes me dicen que no"]
    if pregunta=="salir":
        break
    else:
    bola_magica=random.choice(respuestas)
    print(bola_magica)"""

#6. Encuentre el tiempo de ejecución de los programas de los ejercicios anteriores (pista: use el módulo time)
"""import time"""
 
 #punto 1:

"""inicio1=time.time() #guarda el timepo de incio 

#se ejecuta
def redondear(numero):
    if (numero - int(numero)) < 0.5:
        return int(numero)
    else:
        return int(numero) + 1

numero = input("Ingrese un número decimal: ")
numero = float(numero)

print(redondear(numero))
fin1=time.time() #guarda el tiempo cuando finaliza

tiempo1=fin1-inicio1 #calcula cuanto tardó
print("el tiempo de ejecucion fue de",tiempo1,"segundos en el primer punto")"""

#punto 2:
"""inicio2=time.time()
import tp6_2

numero1= float(input("ingrese un numero: "))
numero2= float(input("ingrese otro numero: "))

resultado= numero1+numero2

print(tp6_2.redondear(resultado))

fin2=time.time()
tiempo2= fin2-inicio2

print("el tiempo de ejecucion fue de", tiempo2, "segundos en el punto2")"""

#punto 3:
"""inicio3=time.time()
import datetime

dia=datetime.datetime.now()

print(dia)

fin3=time.time()
tiempo3=fin3-inicio3

print("el tiempo de ejecucion fue de", tiempo3, "segundos en el punto 3")"""

#punto 4:

"""inicio4=time.time()

import random

while True:
    numeros=[2,3,4,5,6,7,8,9,10]
    devolver_numero=input("devolver un numero? si/no: ")
    if devolver_numero=="si":
        numero_azar=random.choice(numeros)
        print (numero_azar)
    else:
        print("saliendo")
        break

fin4=time.time()
tiempo4=fin4-inicio4

print("el tiempo de ejecucion fue de", tiempo4,"segundos en el punto 4")"""

#punto 5:

"""inicio5= time.time()

import random
while True:
    pregunta=input("ingrese pregunta (si quiere salir, ingresar salir): ")
    respuestas=["Es seguro que si","Las chances son buenas", "Puedes contar con ello", "Pregúntame de nuevo más tarde", "Concéntrate y pregunta de nuevo", "No veo con claridad, intenta de nuevo", "Mi respuesta es no", "Mis fuentes me dicen que no"]
    if pregunta=="salir":
        break
    else:
    bola_magica=random.choice(respuestas)
    print(bola_magica)
    

fin5= time.time()
tiempo5= fin5-inicio5

print("el tiempo de ejecución fue de", tiempo5, "segundos en el punto 5")"""
#7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde toman uno o más papeles al azar de un pozo para elegir los ganadores
"""import random
while True:
    sorteo=[]
    participantes=input("ingrese nombre de un participante:")
    sorteo.append(participantes)
    seguir=input("faltan participantes? si/no: ")
    if seguir=="no":
        break

cantidad_ganadores=int(input("cuantos ganadores hay?: "))
posibilidades= 1% len(sorteo)
ganadores=random.choices(sorteo, k=cantidad_ganadores)

print(ganadores)"""




#8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de nacimiento y sea capaz de devolver la cantidad de días desde su nacimiento hasta hoy. 
from datetime import datetime
fecha_nacimiento= input("Ingrese su fecha de nacimiento (formato: dd/mm/yyyy): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%y")
fecha_hoy = datetime.now()
diferencia = fecha_hoy - fecha_nacimiento
print(diferencia.days)

#9. (Opcional) Implemente el programa del ejercicio 6 usando un diccionario.
