print("Програма порахує кількість рядків які завершуються заданим символом")
print("Файл повинен розташовуватися в папці з програмою та називатися line.txt")
print("Файл не повинен містити порожніх рядків")
print("Текст повинен бути написаний латиницею")
f = open('line.txt')
line = f.readline()
if line == "":
   print("Файл порожній")
   quit()
while True:
    c = str(input("Введіть символ "))
    if len(c) != 1:
        print("Потрібно ввести лише один символ")
    else: break
s = 0
while line:
    if line[-2] == c:
        s += 1
    line = f.readline()
print(s)
f.close()
