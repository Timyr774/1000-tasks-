N = int(input())
a = 0
for i in range(N):
    x = float(input())
    if x % 2 == 0:
        print(x)
        a += 1
print(a)