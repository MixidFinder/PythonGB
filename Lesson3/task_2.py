numbers = list(int(i) for i in input("Input nambers: ").split())

minInd = 0
maxInd = -1
res = []
lenList = int(len(numbers) / 2)

while lenList != 0:
    res.append(numbers[minInd] * numbers[maxInd])
    minInd = minInd + 1
    maxInd = maxInd - 1
    lenList = lenList - 1

print(res)