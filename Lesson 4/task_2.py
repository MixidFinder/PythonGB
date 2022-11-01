numbers = list(int(i) for i in input("Input numbers: ").split())

def non_recuring(numbers):
    list_non_recuring = list(set(numbers))
    return list_non_recuring

print(non_recuring(numbers))