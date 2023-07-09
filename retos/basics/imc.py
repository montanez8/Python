"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es 
<imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""

weight = int(input('enter your weight (kilograms): '))
height = float(input('enter your height (meters): '))
imc = weight / height**2
print('your body mass index is {:,.2f}'.format(imc))
