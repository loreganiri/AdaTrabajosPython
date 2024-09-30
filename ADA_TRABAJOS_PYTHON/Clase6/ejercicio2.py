nums = []
x = 0
while True:
    print("Dame un numero")
    pide = int(input("Introduce un numero 0 o negativo para terminar: "))
    nums.append(pide)
    if pide <= 0:
        break
    print(nums)

for i in nums:  
    x += i

print (f"El total de los numeros sumados es {x}")




