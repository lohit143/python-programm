n = int(input("enter a number\n"))
prime = True

for i in range(2, n):
    if (n % i == 0):
        prime = False
        break

if prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
