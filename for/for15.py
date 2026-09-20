A = int(input())
N = int(input())
H = A
for i in range(N - 1):
    A *= H

print(A)