# Declrando listas
A = [10,40,65,90,16,19,16,80,67,54]
b = [77,90,55,44,30,80,97,16,13,10]
C = []

for i in range(len(A)):
    C.append(A[i] + b[i])
print(C)