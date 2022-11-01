num = int(input("Insert number: "))

def prim_facs(num):
   i = 2
   primnum = []
   while i * i <= num:
       while num % i == 0:
           primnum.append(i)
           num = num / i
       i = i + 1
   if num > 1:
       primnum.append(num)
   return primnum

print(prim_facs(num))