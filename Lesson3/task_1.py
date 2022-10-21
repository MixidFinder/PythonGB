numbers = list(int(i) for i in input("Input numbers: ").split())

numbersOdd = []
for i, num in enumerate(numbers):
    if i % 2 != 0:
        numbersOdd.append(num)

print(sum(numbersOdd))