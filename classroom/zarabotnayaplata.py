o = 15000
dk = int(input('Количество календарных дней по производственному календарю:'))
df = int(input('Количество фактически отработанных дней:'))
p = 2200
n = 13
u = int(input('Удержания:'))
a = o * dk
b = a + p
c = 100 - n
d = c / 100
e = b * d
f = e - u 
print(f)
