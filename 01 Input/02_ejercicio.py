#Recibir dos valores por consola y volverlos enteros
num1=int(input("ingrese primer valor: "))
num2=int(input("ingrese segundo valor: "))
#Sumar los dos valores y depositarlos en una variable
suma=num1+num2
#Multiplicar los dos valores y depositarlos en una variable
producto=num1*num2
#Imprimir los dos valores con diferentes mensajes usando la funcion print y el metodo para string format()
#El orden de las variables se deposita como se agregen a las llaves
#print("string{}".format(variable))
print("La suma de los dos valores es: {}".format(suma))
print("El producto de los dos valores es: {}".format(producto))
