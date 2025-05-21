#1
from os.path import split

py = "python"
print(py.title())

#2
slowo = "ananas"
print(slowo.count('a'))

#3
kot = "kot"
tok = kot[::-1]
print(tok)

#4
input = "kajak"
palindrom = input[::-1]
print(input == palindrom)

#5
zdanie = "Ala ma kota"
print(zdanie.replace(" ","-"))

#6
input = 1234
txt = str(input)
print(txt.split(","))