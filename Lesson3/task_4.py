num = int(input("Insert number: "))

b = ''
while num > 0:
    b = str(num % 2) + b
    num //= 2
 
print(b)