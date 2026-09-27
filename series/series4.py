N = int(input())
a = 0
b = 1.0
for i in range(N):
    x = float(input())
    a += x
    b *= x
print(a)
print(b)