x = int(input('Введите Х: '))
y = int(input('Введите Y: '))
text = 4

if x and y > 0:
    text = 1
elif x < 0 and y > 0:
    text = 2
elif x < 0 and y < 0:
    text = 3
print(f'Точка находится в {text} плоскости')
