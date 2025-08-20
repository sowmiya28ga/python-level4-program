print("Reverse Number")
print("--------------------------")
n = int(input("Enter the number: "))
print("Result")
rev = 0
temp = n 

while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

print("Reverse number:", rev)
