n1 = 367
n2 = 590
n3 = 333

if n1 > n2:
    n1, n2 = n2, n1
if n1 > n3:
    n1, n3 = n3, n1
if n2 > n3:
    n2, n3 = n3, n2

print(n1, n2, n3)
print(n3, n2, n1)