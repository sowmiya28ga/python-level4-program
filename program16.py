print("Factorial Program")
print("--------------------")
n = int(input("Enter The Number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i   
print("Factorial of", n, "is:", fact)  
