# дан списко a = [4, 3, -10, 1, 7, 12], изменить его а=[4, -10, 12, 3, 1, 7]
a = [4, 3, -10, 1, 7, 12]
print(a)
a[1:] = -10, 12, 3, 1, 7
# a.sort(key=lambda x:x%2)
# a[1] = 10
# a[2] = 12
# a[3] = 3
# a[4] = 1
# a[5] = 7
print(a)