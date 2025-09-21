#  Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
    
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”.
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
#  Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#  Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Nino")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto joven")
else:
    print("Adulto")
    
#  Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.
contrasena = input("Ingrese una contrasena entre 8 y 14 caracteres: ")
if len(contrasena) < 8 or len(contrasena) > 14:
    print("Por favor ingrese una contrase de entre 8 y 14 caracteres")
else:
    print("Ha ingresado una contrasena correcta")

# En la documentación oficial se puede encontrar más información sobre este paquete: 
# https://docs.python.org/es/3.8/library/statistics.html.  
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
# mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
# la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# Definir la lista numeros_aleatorios de la siguiente forma: 
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
# forma aleatoria. 
import random
from statistics import mode, median, mean 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)

if (media > mediana) and (mediana > moda):
    print("Sesgo positivo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("Sesgo negativo")
    
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla. 
frase = input("Ingrese una frase o palabra: ")
ultima_letra = frase[len(frase) -1].lower()
if ultima_letra in 'aeiou':
    frase += '!'
print(frase)

# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Ingrese una opcion: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
else:
    print(nombre.title())

# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa danos)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar danos en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar danos significativos)")
else:
    print("Extremo (puede causar graves danos a gran escala)")
    
    
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().upper()
mes = input("Ingrese el mes (ejemplo: marzo): ").strip().lower()
dia = int(input("Ingrese el día: "))

meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}
num_mes = meses.get(mes, 0)

if num_mes == 0 or hemisferio not in ("N", "S"):
    print("Datos incorrectos")
else:
    estacion = ""
    if hemisferio == "N":
        if (num_mes == 12 and dia >= 21) or (num_mes == 1) or (num_mes == 2) or (num_mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (num_mes == 3 and dia >= 21) or (num_mes == 4) or (num_mes == 5) or (num_mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (num_mes == 6 and dia >= 21) or (num_mes == 7) or (num_mes == 8) or (num_mes == 9 and dia <= 20):
            estacion = "Verano"
        elif (num_mes == 9 and dia >= 21) or (num_mes == 10) or (num_mes == 11) or (num_mes == 12 and dia <= 20):
            estacion = "Otoño"
    elif hemisferio == "S":
        if (num_mes == 12 and dia >= 21) or (num_mes == 1) or (num_mes == 2) or (num_mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (num_mes == 3 and dia >= 21) or (num_mes == 4) or (num_mes == 5) or (num_mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (num_mes == 6 and dia >= 21) or (num_mes == 7) or (num_mes == 8) or (num_mes == 9 and dia <= 20):
            estacion = "Invierno"
        elif (num_mes == 9 and dia >= 21) or (num_mes == 10) or (num_mes == 11) or (num_mes == 12 and dia <= 20):
            estacion = "Primavera"
    if estacion:
        print("Estación:", estacion)
    else:
        print("Datos incorrectos")