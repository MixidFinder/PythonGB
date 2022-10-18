import math
number = float(input("Insert number: "))

w, f = math.modf(number)

w = round(w, 6)

while w != int(w):
    w *= 10

gen =[w, f]

x = len(gen) - 1
res = 0
for i, v in enumerate(gen):
    res += v * 10 ** (x - i)

sum = 0
while res > 0:
    sum += res % 10
    res //= 10

print(int(sum))