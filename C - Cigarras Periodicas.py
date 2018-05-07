#http://maratona.ime.usp.br/prim-fase17/maratona.pdf

N = 100000 #Quantidade limite de populacoes
L = 10000000 #Limite de quantidade de iteracoes que podem ser executadas
qtdPop = []
LIM = 0
POP = 0
i = 0
fam = 0

dic_anosSaida = {}



while POP > N or POP < 2:
    POP = input("Entre com a quantidade de populacao de cigarras: ")
    if (POP > N or POP < 2):
        print("Valor invalido! - Valores permitidos: Acima de 2 e menor que 100000")

while LIM > L or LIM < 1:
    LIM = input("Entre com a quantidade de limite de iteracoes: ")
    if (LIM > L or LIM < 1):
        print("Valor invalido! - Valores permitidos: Acima de 1 e menor que 10000000")

while i < POP:
    idadePop = input("Entre com a idade da populacao: %d - " %(i+1))
    qtdPop.append(idadePop)
    i += 1


while fam < POP:
    #print("- Familia: %d" %fam)
    j = 0
    listaAnosFamilia = []
    ANO = 0
    while j < LIM:
        ANO += qtdPop[fam]
        listaAnosFamilia.append(ANO)
        dic_anosSaida[fam] = listaAnosFamilia
        #print ("- Limite: %d" %j)
        j += 1
    fam += 1


print (dic_anosSaida.keys())

for i in dic_anosSaida.keys():
