#Se ingresan los valores por teclado y se convierten a enteros
num1=int(input("Ingrese primer valor: "))
num2=int(input("ingrese segundo valor: "))
#Se utiliza la esturctura if-else, si num1 es mayor a num2 se ejecuta el if
#De no cumplirse esta condicio
if num1>num2:
    print(f"El valor mayor es: {num1}")
else:
    print(f"El valor mayor es: {num2}")