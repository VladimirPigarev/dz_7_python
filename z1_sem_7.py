# 1.напечатать сторку в одну линию - C:\WINDOWS\System32\drivers\etc\nst
# РЕШЕНИЕ
with open('file_1.txt', 'r') as file:
    str = file.readline()
    file.close()
print(str)
