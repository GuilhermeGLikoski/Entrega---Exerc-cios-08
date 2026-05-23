matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

maior = 0
matricula = 0

for i in range(5):

    matriz[i][0] = int(input("Matricula: "))
    matriz[i][1] = int(input("Media provas: "))
    matriz[i][2] = int(input("Media trabalhos: "))

    matriz[i][3] = matriz[i][1] + matriz[i][2]

    if matriz[i][3] > maior:
        maior = matriz[i][3]
        matricula = matriz[i][0]

print("\nMatriz:")

for i in range(5):
    print(matriz[i])

print("\nMatricula com maior nota final:", matricula)
