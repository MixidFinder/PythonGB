numbers = list(float(i) for i in input("Input nambers: ").split())

div = []
for i in numbers:
    if i % 1 != 0:
        div.append(round(i % 1, 6))

res = max(div) - min(div)

print(res)