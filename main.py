# defining the fibonacci numbers and getting the formula

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# giving the range of the numbers


for i in range(20):
    print(fibo(i), end= "        ")