import numpy as np

N = int(input("Informe o tamanho: "))

M1 = np.zeros((N, N))
M2 = np.zeros((N, N))
M3 = np.zeros((N, N))

for l in range(N):
    for c in range(N):
        M1[l][c] = int(input(f"Informe valor para lin {l}, col {c}:"))

for l in range(N):
    for c in range(N):
        M2[l][c] = int(input(f"Informe valor para lin {l}, col {c}:"))

for l in range(N):
    for c in range(N):
        M3[l][c] = M1[l][c] + M2[l][c]

print(M3)
