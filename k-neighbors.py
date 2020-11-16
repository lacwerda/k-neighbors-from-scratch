import math

K = int(input())

N = input()
Ntrain, Ntest = N.split()
Ntrain = int(Ntrain)
Ntest = int(Ntest)

matrix_ntrain = []

for i in range(Ntrain):
    f = input()
    f = f.split()
    matrix_ntrain.append(f)

y_ntrain = []

for i in range(Ntrain):
    y = input()
    y_ntrain.append(y)

matrix_ntest = []

for i in range(Ntest):
    g = input()
    g = g.split()
    matrix_ntest.append(g)

def matrix_converter(matrix):
    for i in range(len(matrix)):
        for o in range(22):
            if o == 0:
                if matrix[i][o] == 'b':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'c':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'x':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'f':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'k':
                    matrix[i][o] = 4
                elif matrix[i][o] == 's':
                    matrix[i][o] = 5
            elif o == 1:
                if matrix[i][o] == 'f':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'g':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 2
                elif matrix[i][o] == 's':
                    matrix[i][o] = 3
            elif o == 2:
                if matrix[i][o] == 'n':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'b':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'c':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'g':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'r':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'p':
                    matrix[i][o] = 5
                elif matrix[i][o] == 'u':
                    matrix[i][o] = 6
                elif matrix[i][o] == 'e':
                    matrix[i][o] = 7
                elif matrix[i][o] == 'w':
                    matrix[i][o] = 8
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 9
            elif o == 3:
                if matrix[i][o] == 't':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'f':
                    matrix[i][o] = 1
            elif o == 4:
                if matrix[i][o] == 'a':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'l':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'c':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'f':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'm':
                    matrix[i][o] = 5
                elif matrix[i][o] == 'n':
                    matrix[i][o] = 6
                elif matrix[i][o] == 'p':
                    matrix[i][o] = 7
                elif matrix[i][o] == 's':
                    matrix[i][o] = 8
            elif o == 5:
                if matrix[i][o] == 'a':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'd':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'f':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'n':
                    matrix[i][o] = 3
            elif o == 6:
                if matrix[i][o] == 'c':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'w':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'd':
                    matrix[i][o] = 2
            elif o == 7:
                if matrix[i][o] == 'b':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'n':
                    matrix[i][o] = 1
            elif o == 8:
                if matrix[i][o] == 'k':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'n':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'b':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'h':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'g':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'r':
                    matrix[i][o] = 5
                elif matrix[i][o] == 'o':
                    matrix[i][o] = 6
                elif matrix[i][o] == 'p':
                    matrix[i][o] = 7
                elif matrix[i][o] == 'u':
                    matrix[i][o] = 8
                elif matrix[i][o] == 'e':
                    matrix[i][o] = 9
                elif matrix[i][o] == 'w':
                    matrix[i][o] = 10
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 11
            elif o == 9:
                if matrix[i][o] == 'e':
                    matrix[i][o] = 0
                elif matrix[i][o] == 't':
                    matrix[i][o] = 1
            elif o == 10:
                if matrix[i][o] == 'b':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'c':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'u':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'e':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'z':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'r':
                    matrix[i][o] = 5
                elif matrix[i][o] == '?':
                    matrix[i][o] = 6
            elif o == 11:
                if matrix[i][o] == 'f':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'k':
                    matrix[i][o] = 2
                elif matrix[i][o] == 's':
                    matrix[i][o] = 3
            elif o == 12:
                if matrix[i][o] == 'f':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'k':
                    matrix[i][o] = 2
                elif matrix[i][o] == 's':
                    matrix[i][o] = 3
            elif o == 13:
                if matrix[i][o] == 'n':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'b':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'c':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'g':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'o':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'p':
                    matrix[i][o] = 5
                elif matrix[i][o] == 'e':
                    matrix[i][o] = 6
                elif matrix[i][o] == 'w':
                    matrix[i][o] = 7
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 8
            elif o == 14:
                if matrix[i][o] == 'n':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'b':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'c':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'g':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'o':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'p':
                    matrix[i][o] = 5
                elif matrix[i][o] == 'e':
                    matrix[i][o] = 6
                elif matrix[i][o] == 'w':
                    matrix[i][o] = 7
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 8
            elif o == 15:
                if matrix[i][o] == 'p':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'u':
                    matrix[i][o] = 1
            elif o == 16:
                if matrix[i][o] == 'n':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'o':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'w':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 3
            elif o == 17:
                if matrix[i][o] == 'n':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'o':
                    matrix[i][o] = 1
                elif matrix[i][o] == 't':
                    matrix[i][o] = 2
            elif o == 18:
                if matrix[i][o] == 'c':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'e':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'f':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'l':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'n':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'p':
                    matrix[i][o] = 5
                elif matrix[i][o] == 's':
                    matrix[i][o] = 6
                elif matrix[i][o] == 'z':
                    matrix[i][o] = 7
            elif o == 19:
                if matrix[i][o] == 'k':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'n':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'b':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'h':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'r':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'o':
                    matrix[i][o] = 5
                elif matrix[i][o] == 'u':
                    matrix[i][o] = 6
                elif matrix[i][o] == 'w':
                    matrix[i][o] = 7
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 8
            elif o == 20:
                if matrix[i][o] == 'a':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'c':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'n':
                    matrix[i][o] = 2
                elif matrix[i][o] == 's':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'v':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'y':
                    matrix[i][o] = 5
            elif o == 21:
                if matrix[i][o] == 'g':
                    matrix[i][o] = 0
                elif matrix[i][o] == 'l':
                    matrix[i][o] = 1
                elif matrix[i][o] == 'm':
                    matrix[i][o] = 2
                elif matrix[i][o] == 'p':
                    matrix[i][o] = 3
                elif matrix[i][o] == 'u':
                    matrix[i][o] = 4
                elif matrix[i][o] == 'w':
                    matrix[i][o] = 5
                elif matrix[i][o] == 'd':
                    matrix[i][o] = 6
    
    return matrix

matrix_ntrain = matrix_converter(matrix_ntrain)
matrix_ntest = matrix_converter(matrix_ntest)

vetor_medias = []

for o in range(len(matrix_ntrain[0])):
    soma_dos_atributos = 0
    for i in range(len(matrix_ntrain)):
        soma_dos_atributos = soma_dos_atributos + matrix_ntrain[i][o]
    media = soma_dos_atributos/len(matrix_ntrain)
    vetor_medias.append(media)

vetor_desvio_padrao = []

for o in range(len(matrix_ntrain[0])):
    somatorio = 0
    for i in range(Ntrain):
        somatorio = somatorio + (pow(matrix_ntrain[i][o]-vetor_medias[o], 2))
    desvio_padrao = math.sqrt((somatorio)/len(matrix_ntrain))
    vetor_desvio_padrao.append(desvio_padrao)

def padronizacao(matrix, v_m, v_dp):
    matriz_padronizada = []
    for i in range(len(matrix)):
        linha = []
        for j in range(len(matrix[0])):
            if v_dp[j] == 0:
                linha.append(0)
            else:
                g = (matrix[i][j]-v_m[j])/v_dp[j]
                linha.append(g)
        matriz_padronizada.append(linha)
    return matriz_padronizada

ntrain_padronizada = padronizacao(matrix_ntrain, vetor_medias, vetor_desvio_padrao)
ntest_padronizada = padronizacao(matrix_ntest, vetor_medias, vetor_desvio_padrao)

output = []

for i in range(len(ntest_padronizada)):
    distancias = []
    distancias2 = []
    p_e = []
    for o in range(len(ntrain_padronizada)):
        soma = 0
        for j in range(22):
            soma = soma + ((ntest_padronizada[i][j] - ntrain_padronizada[o][j])**2)
        decl = math.sqrt(soma)
        distancias.append(decl)
        distancias2.append(decl)
    distancias2.sort()
    for l in range(K):
        f = distancias2[l]
        h = distancias.index(f)
        p_e.append(y_ntrain[h])
    if p_e.count('p') > p_e.count('e'):
        output.append('p')
    elif p_e.count('p') < p_e.count('e'):
        output.append('e')

for i in range(len(output)):
    print(output[i])