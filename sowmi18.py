print("Fibonacci Series")
print("--------------------------------")
n=int(input("Enter The Number:"))
print("Fibonacci Series:")
a = -1
b = 1
for i in range(n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
