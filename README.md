# 📚 Algoritmo de Ordenação por Intercalação Balanceada com Seleção Natural

Este projeto implementa um algoritmo de ordenação externo baseado em **intercalação balanceada de P-caminhos** e **seleção natural com heap mínimo**, ideal para situações em que os dados não cabem na memória principal e precisam ser organizados por meio de leitura e gravação em blocos.

---

## 📌 Objetivo

Simular o processo de ordenação de grandes volumes de dados com recursos de memória limitados, utilizando técnicas clássicas de organização por blocos:

- **Seleção Natural com Heap**: Pré-processamento dos dados para formar segmentos ordenados.
- **Intercalação Balanceada**: Etapas de fusão dos segmentos para obter a lista ordenada final.

---

## ⚙️ Como Funciona

### 1. **Seleção Natural (`selecao_natural`)**
Divide a lista original em segmentos ordenados utilizando um heap mínimo de tamanho fixo (3 elementos), aplicando uma variação do algoritmo de seleção natural para simular a limitação de memória.

### 2. **Alocação de Segmentos (`alocacao_segmentos`)**
Distribui os segmentos criados entre os arquivos simulados, para posterior intercalação balanceada.

### 3. **Intercalação Balanceada de P-Caminhos (`intercalacao_balanceada` e `ordenacao_multicaminhos`)**
Realiza múltiplas fases de intercalação entre os segmentos, reduzindo o número de blocos até que reste apenas um segmento ordenado final.

### 4. **Cálculo de Acessos (`calculo_beta`)**
Mede o custo da ordenação em termos de quantidade de acessos aos registros, simulando leituras/escritas em disco.

---

## 🧮 Parâmetros

- `m`: Quantidade de blocos disponíveis na memória principal.
- `k`: Número total de arquivos disponíveis para intercalação.
- `r`: Quantidade de segmentos que serão gerados.
- `n`: Tamanho total da lista a ser ordenada.
- `lista`: Dados a serem ordenados.

---

## 🖥️ Exemplo de Execução

No final do arquivo, a função `main()` executa o algoritmo com os seguintes valores:

```python
lista = [7, 1, 5, 6, 3, 8, 2, 10, 4, 9, 1, 3, 7, 4, 1, 2, 3]
m = 3
k = 4
r = 3
n = 17
ordenacao_multicaminhos(m, k, r, n, lista)
