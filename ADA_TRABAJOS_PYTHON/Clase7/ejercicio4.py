fibo=0
a=0
b=1

while fibo < 100:
    fibo = a+b
    a=b
    b=fibo
    print(fibo)
