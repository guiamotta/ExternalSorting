import heapq

#utilizando um algoritmo de selecao natural, o codigo pre-ordena
#os segmentos a serem intercalados utilizando um heap minimo de tamanho 3
def selecao_natural(m, k, r, n, lista):
    tamanho_max_segmento = n//m
    segmentos = []
    segmento = []
    heap = []
    indice = 3
    indice_heap = 0
    for i in range(n):
        if len(heap) <3:
            heap.append(lista[i])
        else:
            break
    heap = sorted(heap)

    for _ in range(r):
        while (len(segmento) < tamanho_max_segmento) and heap:
            segmento.append(heap.pop(indice_heap))
            if indice<len(lista):
                heap.append(lista[indice])
            heap = sorted(heap)
            indice = indice + 1

            if heap:
                if len(segmento)>0 and heap[indice_heap]<segmento[-1]:
                    indice_heap = indice_heap + 1

                if len(segmento) == tamanho_max_segmento:
                    indice_heap = 0

                if indice_heap == 2 and indice==len(lista):
                    segmento.append(heap.pop(indice_heap))

                if indice_heap == 3 or indice == len(lista):
                    indice_heap = 0
                    break

        segmentos.append(segmento)
        segmento = [] 
    return segmentos

def alocacao_segmentos(k, segmentos):
    num_listas = k // 2
    listas = [[] for _ in range(num_listas)] 

    for i, segmento in enumerate(segmentos):
        listas[i % num_listas].append(segmento) 
    return listas

#Formata o print para ficar mais legível
def formatar_print(listas, y):
    resultado_formatado = ""
    if len(listas) == 1:
        resultado_formatado += "{" + " ".join(map(str, listas[0])) + "}" 
        return print(resultado_formatado.strip())

    for i in range(len(listas)):
        resultado_formatado += f"{i+1+y}: " 
        for segmento in listas[i]:
            resultado_formatado += "{" + " ".join(map(str, segmento)) + "}" 
        resultado_formatado += "\n"
    return print(resultado_formatado.strip())

#Calcula o número de acessos aos registros
def calculo_beta(m, lista, alfa):
    somatorio_tamanho = 0
    for sequencia in lista:
        somatorio_tamanho = somatorio_tamanho + len(sequencia)
    if alfa ==1:
        return somatorio_tamanho
    return ((1/(m*len(lista)))*somatorio_tamanho)

#Algoritmo de um passo da intercalação balanceada de P-caminhos
def intercalacao_balanceada(lista):
    n = len(lista)
    ind = 0
    for i in range(0, n, 2):
        if i==n-1:
            break
        if ind%2 == 1:
            lista[i] = list(heapq.merge(lista[i], lista[i+1]))
            lista.remove(lista[i+1])
            break
        else:
            lista[i+1] = list(heapq.merge(lista[i], lista[i+1]))
            lista.remove(lista[i])
            break
    return lista

#Algoritmo de toda a intercalacao balanceada de P-caminhos
def ordenacao_multicaminhos(m, k, r, n, lista):
    #Fase 0
    segmentos_ordenados = sorted(selecao_natural(m, k, r, n, lista), key=len, reverse=True)
    beta = calculo_beta(m, segmentos_ordenados, 0)
    num_registros = calculo_beta(m, segmentos_ordenados, 1)
    operacoes = 0
    print(f"fase 0 {beta:.2f}")
    segmentos_print = alocacao_segmentos(k, segmentos_ordenados)    
    formatar_print(segmentos_print, 0)

    #Intercalaçao Balanceada P-Caminhos
    fase = 1
    while len(segmentos_ordenados)>1:
        segmentos_ordenados = intercalacao_balanceada(segmentos_ordenados)
        beta = calculo_beta(m, segmentos_ordenados, 0) 
        operacoes = operacoes + calculo_beta(m, segmentos_ordenados, 1) 
        print(f"fase {fase} {beta:.2f}")
        if len(segmentos_ordenados)>1:
            segmentos_print = alocacao_segmentos(k, segmentos_ordenados)
            formatar_print(segmentos_print, k//2)
        else:
            print("1:", end=" ")
            formatar_print(segmentos_ordenados, k//2)
        fase = fase + 1
    alfa = operacoes//num_registros
    print(f"final {alfa:.2f}")

#executa o programa
def main():
    lista = [7, 1, 5, 6, 3, 8, 2, 10, 4, 9, 1, 3, 7, 4, 1, 2, 3]
    m = 3
    k = 4
    r = 3
    n = 17
    ordenacao_multicaminhos(m, k, r, n, lista)

if __name__ == '__main__':
    main()
