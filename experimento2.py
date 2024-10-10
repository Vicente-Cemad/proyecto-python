factores = []
n = 10
divisor = 2
while n > 1:
    print (n)
    print (divisor)
    while n % divisor == 0:
        factores.append(divisor)
        n //= divisor
        divisor += 1
print (factores)
