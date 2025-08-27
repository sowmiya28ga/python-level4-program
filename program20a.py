print("Prime Number Checking")
print("-----------------------------")
n = int(input("Enter The Number: "))
print("Result")

count = 0
for i in range(2, n):
    if n % i == 0:
        count += 1
        break

if count == 0 and n > 1:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
