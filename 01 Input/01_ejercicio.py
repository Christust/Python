#Ingresar el valor de un lado del cuadrado por medio de consola con la función input y calcular el area del cuadrado

#Para recibir un valor con la funcion input(mensaje_del_texto) se debe considerar que siempre es un string
#Si se desea recibir un entero o flotante se debe usar la funcion int() o float() respectivamente
lado=int(input("Ingrese la medida del lado del cuadrado: "))
#Realizar la multiplicación del valor por si mismo para obtener el cuadrado lo cual seria el area
superficie=lado*lado
#Imprimir el valor usando la función print con formato usando print(f"string{variable}")
print(f"La superficie del cuadrado es: {superficie}")