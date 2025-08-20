print("Sum Of N Numbers")
print("------------------------")

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

sum = 0
print("Result:")
for i in range(start, end + 1):
    print(i, end=" ")
    sum += i

print("\nSum of values is:", sum)

