print("Prime Number Generation")
print("-------------------------------")
sn = int(input("Enter The Starting Number: "))
en = int(input("Enter The Ending Number: "))
print("Result:")

for n in range(sn, en + 1):
    if n > 1:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n, "Prime", end=" ")
