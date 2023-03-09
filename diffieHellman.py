print("Enter Two Large Prime Numbers")
p = int(input("Enter First Large Prime Number: -"))
q = int(input("Enter Second Large Prime Number: -"))
a = int(input("Enter Ramesh Secret Key: - "))
b = int(input("Enter Suresh Secret Key: - "))

R= ((q ** a)%p)
S= ((q ** b)%p)

RK = ((S**a)%p)
SK = ((R**b)%p)
print("Ramesh's Secret Key = ", RK)
print("Suresh's Secret Key = ", SK)

if RK == SK :
    print("Communication Can Continue")
else:
    print("Communication cannot continue")