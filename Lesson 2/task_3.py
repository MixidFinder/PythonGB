str1 = str(input("Insert first string: "))
str2 = str(input("Insert second string: "))
count = 0
for i in range(len(str1)):
    if str1[i] == str2[i]:
        count += 1
print(count)

