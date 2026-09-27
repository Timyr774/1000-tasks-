B = float(input())
N = int(input())
for i in range(N):
    x = float(input())
    if B < x:
        print(B)
        B = x
    print(x)
    if B > x:
        print(B)