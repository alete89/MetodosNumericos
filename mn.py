# -*- coding: utf-8 -*-

import numpy

print 'Ingrese los coeficientes de forma decreciente, separados con ENTER. Cuando haya terminado presione ENTER sin ingresar nada'
coeficientes = list(iter(raw_input, ''))
coeficientes = map(float, coeficientes)
print (coeficientes)

funcion = numpy.poly1d(coeficientes)
print (funcion)

print funcion(4)


neg = float(raw_input("ingrese un valor del dominio donde la función sea negativa"))
while (funcion(neg) >= 0):
    print "en el valor ingresado, la función es cero o positiva"
    neg = float(raw_input("ingrese un valor del dominio donde la función sea negativa"))

pos = float(raw_input("ingrese un valor del dominio donde la función sea positiva"))
while (funcion(pos) <= 0):
    print "en el valor ingresado, la función es cero o negativa"
    pos = float(raw_input("ingrese un valor del dominio donde la función sea positiva"))

# aux = [pos, neg]
# izquierda = aux[0]
# derecha = aux[1]

for _ in range(20):
    promedio = (neg + pos) / 2.0
    if (funcion(promedio) == 0):
        print promedio + "es la raiz"
    elif (funcion(promedio) > 0):
        pos = promedio
    else:
        neg = promedio
    print ("x= " + str(promedio) + " eval= " + str(funcion(promedio)))
