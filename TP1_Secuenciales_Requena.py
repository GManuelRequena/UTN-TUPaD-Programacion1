# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
print("Hola Mundo!")

# 2)  Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#  el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#  por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#  realizar la impresión por pantalla. 
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#  imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#  “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#  años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#  la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#  su perímetro.
radio = float(input("Ingrese el radio del circulo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#  cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#  multiplicar de dicho número.  
numero = int(input("Ingrese un numero: "))
for i in range(0, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#  pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Ingrese el primer numero (distinto de 0): "))
numero2 = int(input("Ingrese el segundo numero (distinto de 0): "))
print(f"La suma es: {numero1 + numero2}")
print(f"La resta es: {numero1 - numero2}")
print(f"La multiplicacion es: {numero1 * numero2}")
print(f"La division es: {numero1 / numero2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#  de masa corporal.
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#  pantalla su equivalente en grados Fahrenheit.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#  dichos números.
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los números ingresados es: {promedio}")