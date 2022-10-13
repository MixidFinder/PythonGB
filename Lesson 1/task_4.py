first = float(input('Введите первое число: '))
op = str(input('Введите операцию: '))
second = float(input('Введите второе число: '))

if (op=="/" or op=="mod" or op=="div") and second==0:
    c = "Деление на 0!"
elif op=="+": c = first + second
elif op=="-": c = first - second
elif op=="/": c = first / second
elif op=="*": c = first * second
elif op=="mod": c = first % second
elif op=="pow": c = first ** second
elif op=="div": c = first // second

print (c)
