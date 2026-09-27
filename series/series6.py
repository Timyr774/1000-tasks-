N = int(input())
a = 1.0
for i in range(N):
    x = float(input())
    b = x-int(x)
    print(b)
    a *= b
print(a)