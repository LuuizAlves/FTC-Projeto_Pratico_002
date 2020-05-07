import ast

#---------------------------- FUNÇÃO DA MULTIPLICAÇÃO ----------------------#
def multiplicacao(x, y):
    lin_x = len(x)
    col_x = len(x[0])
    lin_y = len(y)
    col_y = len(y[0])

    res = []
    for linha in range(lin_x):
        res.append([])
        for coluna in range(col_y):
            res[linha].append(0)
            for k in range(col_x):
                res[linha][coluna] += x[linha][k] * y[k][coluna]

    return res

#------------------------- FUNÇÃO QUE CRIA PI TRANPOSTO -----------------------#
def criandoPit(qtd_est, est_ini):

    vetorPi = []
    for i in range(qtd_est):
        vetorPi2 = []
        for j in range(1):
            if i == est_ini:
                vetorPi2.append(1)
            else:
                vetorPi2.append(0)
        vetorPi.append(vetorPi2)

    matriz_T = []
    for i in range(1):
        linha = []
        for j in range(qtd_est):
            linha.append(0)
        matriz_T.append(linha)

    for i in range(1):
        for j in range(qtd_est):
            matriz_T[i][j] = vetorPi[j][i]

    #print('MATRIZ PI TRANSPOSTA: ')
    return matriz_T

#-------------------------- FUNÇÃO QUE CRIA A MATRIZ N ---------------------#
def criandoN(qte_est, ests_finais):
    matriz_n = []

    for i in range(qtd_est):
        linha = []
        for j in range(1):
            if i in ests_finais:
                linha.append(1)
            else:
                linha.append(0)
        matriz_n.append(linha)

    #print('MATRIZ N: ')
    return matriz_n

#------------------------- FUNÇÃO QUE CRIA Xa ------------------------------#
def criandoXa(delta):
    criandoxa = []
    k = 0
    for i in range(qtd_est):
        ad = delta[i][k]
        criandoxa.append(ad)

    xa = []
    for i in range(qtd_est):
        linha = []
        for j in range(qtd_est):
            linha.append(0)
        xa.append(linha)

    for i in range(qtd_est):
        a = criandoxa[i]
        xa[i][a] = 1

    #print('MATRIZ Xa: ')
    return xa

#------------------------- FUNÇÃO QUE CRIA Xb -------------------------------#
def criandoXb(delta):
    criandoxb = []
    k = 1
    for i in range(qtd_est):
        ad = delta[i][k]
        criandoxb.append(ad)

    xb = []
    for i in range(qtd_est):
        linha = []
        for j in range(qtd_est):
            linha.append(0)
        xb.append(linha)

    for i in range(qtd_est):
        a = criandoxb[i]
        xb[i][a] = 1

    #print('MATRIZ Xb: ')
    return xb

#--------------------------- RESULTADOS DAS PALAVRAS ----------------------#
def resultadosFinais(palavra, pit, mn, mxa, mxb):
    tamanho_palavra = len(palavra)
    resultado = []
    for i in range(tamanho_palavra):
        if i == 0:
            if palavra[i] == 'a':
                resultado = multiplicacao(pit, mxa)

            elif palavra[i] == 'b':
                resultado = multiplicacao(pit, mxb)
        else:
            if palavra[i] == 'a':
                resultado = multiplicacao(resultado, mxa)

            elif palavra[i] == 'b':
                resultado = multiplicacao(resultado, mxb)


    resultadof = multiplicacao(resultado, mn)

    if (resultadof[0][0] == 1):
        print('ACEITA')
    else:
        print('REJEITA')

x = input()
y = ast.literal_eval(x)

qtd_est = y['estados']
est_ini = y['inicial']
ests_finais = y['final']
delta = y['delta']

lind = len(delta)
for i in range(lind):
    delta[i].sort()

pit = criandoPit(qtd_est, est_ini)
mn = criandoN(qtd_est, ests_finais)
mxa = criandoXa(delta)
mxb = criandoXb(delta)

inteiro = input()
trans = int(inteiro)

for i in range(trans):
    palavra = input()
    resultadosFinais(palavra, pit, mn, mxa, mxb)