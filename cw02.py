#1
import datetime
import math

a = 5
b = 7
result_cw1 = (a+b) * 7
print(result_cw1)

#2
c = 5
d = 8
e = 2
max_num = max(c,d,e)
print(max_num)

#3
f = 5
g = 8
h = 3
numbers = [f,g,h]
avg = sum(numbers)/len(numbers)
print(round(avg,2))

#4
temp = 301.23
temp_c = temp - 273.15
print(temp_c)

#5
num = 25
pierwiastek = math.sqrt(num)
print(pierwiastek)

#6
a = input("Podaj liczbę A: ")
import time
t = time.localtime()
current_time = time.strftime("%H",t)
print(int(a) * int(current_time))
