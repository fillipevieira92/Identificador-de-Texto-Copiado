import re

def le_assinatura():
    # A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    # A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    # A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    # A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    # A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
    return frase.split()

def n_palavras_unicas(lista_palavras):
    # A funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    # A funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_x, as_b):
    # A funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
    subtracao = [x1 - x2 for (x1, x2) in zip(as_x, as_b)]
    somadasub = 0
    for n in subtracao:
        n = abs(n)
        somadasub += n
    Sab = somadasub/6

    return Sab
    
def calcula_assinatura(texto):
    # A funcao recebe um texto e deve devolver a assinatura do texto.
    
    sentencas = separa_sentencas(texto)
    frases = separa_frases(sentencas)
    palavras = separa_palavras(frases)

    # walb =  Soma do tamanho medio das palavras dividido pelo numero total de palavras.
    qtddepalavras = len(palavras)
    somapalavras = 0
    for n in palavras:
        if len(n) >= 2:
            somapalavras += len(n)
            
    walb = somapalavras/qtddepalavras

    # ttrb =  Número de palavras diferentes dividido pelo número total de palavras.

    ttrb = n_palavras_diferentes(palavras)/qtddepalavras


    # hlrb =  Número de palavras que aparecem uma única vez dividido pelo total de palavras.

    hlrb = n_palavras_unicas(palavras)/qtddepalavras

    # salb =  Soma dos números de caracteres em todas as sentenças dividido pelo número de sentenças.

    qtdsentencas = len(sentencas)
    somasentencas = 0
    for n in sentencas:
        somasentencas += len(n)

    salb = somasentencas/qtdsentencas

    # sacb =  Número total de frases dividido pelo número de sentenças.

    qtdfrases = len(frases)
    
    sacb = qtdfrases/qtdsentencas    

    # palb =  Soma do número de caracteres em cada frase dividida pelo número de frases no texto.

    somacaracteres = 0
    for n in frases:
        somacaracteres += len(n)
    
    palb = somacaracteres/qtdfrases
    
    return [walb, ttrb, hlrb, salb, sacb, palb]

def avalia_textos(textos, ass_cp):
    # A funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    
    ass_cp = le_assinatura()
   
    
    textos = le_textos()
    x = len(textos)
    if x == 1:
        texto1 = textos[0] 

        assinaturatexto1 = calcula_assinatura(texto1) 
        Sab1 = compara_assinatura(assinaturatexto1, ass_cp) 
        if Sab1 <= 2:
            print("O autor do texto provavelmente sofre de COH-PIAH.")
    
    if x == 2:
        texto1 = textos[0]
        texto2 = textos[1]

        assinaturatexto1 = calcula_assinatura(texto1)
        assinaturatexto2 = calcula_assinatura(texto2)
        Sab1 = compara_assinatura(assinaturatexto1, ass_cp)
        Sab2 = compara_assinatura(assinaturatexto2, ass_cp)
        if Sab1 < Sab2:
            print("O autor do texto 1 provavelmente sofre de COH-PIAH.")
        else:
            print("O autor do texto 2 provavelmente sofre de COH-PIAH.")
                
    if x == 3:
        texto1 = textos[0]
        texto2 = textos[1]
        texto3 = textos[2]

        assinaturatexto1 = calcula_assinatura(texto1)
        assinaturatexto2 = calcula_assinatura(texto2)
        assinaturatexto3 = calcula_assinatura(texto3)
        Sab1 = compara_assinatura(assinaturatexto1, ass_cp)
        Sab2 = compara_assinatura(assinaturatexto2, ass_cp)
        Sab3 = compara_assinatura(assinaturatexto3, ass_cp)
        listSab = [Sab1,Sab2,Sab3]
        lista3 = sorted(listSab)
        
        print("O autor do texto",lista3 ,"provavelmente sofre de COH-PIAH.")

    if x == 4:
        texto1 = textos[0]
        texto2 = textos[1]
        texto3 = textos[2]
        texto4 = textos[3]

        assinaturatexto1 = calcula_assinatura(texto1)
        assinaturatexto2 = calcula_assinatura(texto2)
        assinaturatexto3 = calcula_assinatura(texto3)
        assinaturatexto4 = calcula_assinatura(texto4)
        Sab1 = compara_assinatura(assinaturatexto1, ass_cp)
        Sab2 = compara_assinatura(assinaturatexto2, ass_cp)
        Sab3 = compara_assinatura(assinaturatexto3, ass_cp)
        Sab4 = compara_assinatura(assinaturatexto4, ass_cp)
        listSab = [Sab1,Sab2,Sab3,Sab4]
        lista4 = sorted(listSab)
        print("O autor do texto",lista4 ,"provavelmente sofre de COH-PIAH.")
