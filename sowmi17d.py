print("Sum Of N Numbers")
print("---------------------------")
sn = int(input("Enter The Starting Number: "))
en = int(input("Enter The Ending Number: "))
print("Result")
print("Series:", end=" ")

sum = 0
count = 0

for i in range(sn, en + 1):
    if (i % 5 == 0) and (i % 3 == 0):
        print(i, end=" ")
        sum += i
        count += 1
        print("\n\nSum Value  :", sum)
        print("Count Values  :", count)

