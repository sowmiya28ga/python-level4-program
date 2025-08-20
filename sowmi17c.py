print("Sum Of N Numbers")
print("---------------------------")
sn = int(input("Enter The Starting Number: "))
en = int(input("Enter The Ending Number: "))
d = int(input("Enter The Difference: "))
print("Result")
print("Series:", end=" ")

sum = 0
count = 0

for i in range(sn, en + 1, d):
    print(i, end=" ")
    sum += i
    count += 1

print("\nSum Value:", sum)
print("Count Values:", count)
