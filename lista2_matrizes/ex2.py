import numpy as np

N = 10

M1 = np.zeros((N, N))

for l in range(N):
    for c in range(N):
        M1[l][c] = int(input(f"Informe valor para lin {l}, col {c}:"))


for i in range(N):
    aux = M1[2][i]
    M1[2][i] = M1[8][i]
    M1[8][i] = aux
    
for i in range(N):
    aux = M1[5][i]
    M1[5][i] = M1[i][9]
    M1[i][9] = aux

print(M1)