print("Dame un numero:")
x = int(input())
if x<1 or x>10:
    raise ValueError ("Solo se aceptan numeros entre 1 y 10")
else:
    print("Numero registrado correctamente")