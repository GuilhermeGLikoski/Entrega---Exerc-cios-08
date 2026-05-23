matriz = [
    [5, 8, 2, 1],
    [7, 3, 9, 4],
    [6, 15, 0, 2],
    [11, 10, 14, 13]
]


maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0


for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j


print("Matriz:")

for linha in matriz:
    print(linha)
print("\nMaior valor:", maior)
print("Linha:", linha_maior)
print("Coluna:", coluna_maior)
