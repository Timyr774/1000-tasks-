N = int(input())
a = 0
for i in range(1,N+1):
    x = float(input())
    if x % 2 != 0:
        print(i)
        a += 1
print(a)