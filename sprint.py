import random
import time
import sys
import matplotlib.pyplot as plt
import gc
sys.setrecursionlimit(10000000)
 
# Classe para o nó da árvore AVL
class NoAVL:
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao
        self.esquerda = None
        self.direita = None
        self.altura = 1  # Altura do nó
 
# Classe para a árvore AVL
class ArvoreAVL:
    def __init__(self):
        self.raiz = None
 
    def inserir(self, nome, pontuacao):
        self.raiz = self._inserir(self.raiz, nome, pontuacao)
 
    def _inserir(self, raiz, nome, pontuacao):
        # Inserção normal de árvore binária de busca
        if not raiz:
            return NoAVL(nome, pontuacao)
        elif pontuacao < raiz.pontuacao:
            raiz.esquerda = self._inserir(raiz.esquerda, nome, pontuacao)
        else:
            raiz.direita = self._inserir(raiz.direita, nome, pontuacao)
 
        # Atualizar altura do nó pai
        raiz.altura = 1 + max(self.get_altura(raiz.esquerda),
                              self.get_altura(raiz.direita))
 
        # Obter o fator de balanceamento
        fator_balanceamento = self.get_balanceamento(raiz)
 
        # Rotação LL
        if fator_balanceamento > 1 and pontuacao < raiz.esquerda.pontuacao:
            return self.rotacao_direita(raiz)
 
        # Rotação RR
        if fator_balanceamento < -1 and pontuacao > raiz.direita.pontuacao:
            return self.rotacao_esquerda(raiz)
 
        # Rotação LR
        if fator_balanceamento > 1 and pontuacao > raiz.esquerda.pontuacao:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
 
        # Rotação RL
        if fator_balanceamento < -1 and pontuacao < raiz.direita.pontuacao:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)
 
        return raiz
 
    def rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
 
        # Rotação
        y.esquerda = z
        z.direita = T2
 
        # Atualizar alturas
        z.altura = 1 + max(self.get_altura(z.esquerda),
                           self.get_altura(z.direita))
        y.altura = 1 + max(self.get_altura(y.esquerda),
                           self.get_altura(y.direita))
 
        return y
 
    def rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
 
        # Rotação
        y.direita = z
        z.esquerda = T3
 
        # Atualizar alturas
        z.altura = 1 + max(self.get_altura(z.esquerda),
                           self.get_altura(z.direita))
        y.altura = 1 + max(self.get_altura(y.esquerda),
                           self.get_altura(y.direita))
 
        return y
 
    def get_altura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura
 
    def get_balanceamento(self, raiz):
        if not raiz:
            return 0
        return self.get_altura(raiz.esquerda) - self.get_altura(raiz.direita)
 
    def in_order_traversal(self, raiz, result):
        if raiz is not None:
            self.in_order_traversal(raiz.esquerda, result)
            result.append((raiz.nome, raiz.pontuacao))
            self.in_order_traversal(raiz.direita, result)
 
    def buscar_por_pontuacao(self, pontuacao, epsilon=1e-6):
        return self._buscar_por_pontuacao(self.raiz, pontuacao, epsilon)
 
    def _buscar_por_pontuacao(self, raiz, pontuacao, epsilon):
        if raiz is None:
            return None
        if abs(raiz.pontuacao - pontuacao) < epsilon:
            return (raiz.nome, raiz.pontuacao)
        elif pontuacao < raiz.pontuacao:
            return self._buscar_por_pontuacao(raiz.esquerda, pontuacao, epsilon)
        else:
            return self._buscar_por_pontuacao(raiz.direita, pontuacao, epsilon)
 
# Função para medir tempo de execução
def medir_tempo(funcao, *args, **kwargs):
    inicio = time.perf_counter()
    resultado = funcao(*args, **kwargs)
    fim = time.perf_counter()
    return fim - inicio, resultado
 
# Funções de busca sequencial
def buscar_por_pontuacao_dicionarios(dados, pontuacao_busca, epsilon=1e-6):
    for d in dados:
        if abs(d['pontuacao'] - pontuacao_busca) < epsilon:
            return d
    return None
 
def buscar_por_pontuacao_tuplas(dados_tuplas, pontuacao_busca, epsilon=1e-6):
    for nome, pontuacao in dados_tuplas:
        if abs(pontuacao - pontuacao_busca) < epsilon:
            return (nome, pontuacao)
    return None
 
# Função de busca binária em lista de tuplas
def busca_binaria_tuplas(lista, pontuacao_busca, epsilon=1e-6):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        pontuacao_meio = lista[meio][1]
        if abs(pontuacao_meio - pontuacao_busca) < epsilon:
            return lista[meio]
        elif pontuacao_busca < pontuacao_meio:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return None
 
# Função de busca binária em lista de dicionários
def busca_binaria_dicionarios(lista, pontuacao_busca, epsilon=1e-6):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        pontuacao_meio = lista[meio]['pontuacao']
        if abs(pontuacao_meio - pontuacao_busca) < epsilon:
            return lista[meio]
        elif pontuacao_busca < pontuacao_meio:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return None
 
# Funções de ordenação
def ordenar_dicionarios(dados):
    return sorted(dados, key=lambda x: x['pontuacao'])
 
def ordenar_tuplas(dados_tuplas):
    return sorted(dados_tuplas, key=lambda x: x[1])
 
# Função para executar testes de escalabilidade
def executar_testes_escalabilidade(tamanhos):
    resultados = {
        'n': [],
        'tempo_insercao_avl': [],
        'tempo_busca_avl': [],
        'tempo_busca_seq_dicionario': [],
        'tempo_busca_bin_dicionario': [],
        'tempo_ordenacao_dicionario': [],
    }
 
    for n in tamanhos:
        print(f"Executando testes para n = {n}")
        resultados['n'].append(n)
 
        # Limpar memória antes de cada teste
        gc.collect()
 
        # Gerar dados
        random.seed(42)
        dados = [{'nome': f'usuario_{i}', 'pontuacao': random.uniform(0, 100) + i * 1e-8} for i in range(n)]
        dados_tuplas = [(d['nome'], d['pontuacao']) for d in dados]
 
        # Selecionar uma pontuação aleatória para buscar
        id_aleatorio = random.randint(0, n - 1)
        pontuacao_busca = dados[id_aleatorio]['pontuacao']
 
        # Criar e preencher a árvore AVL
        arvore_avl = ArvoreAVL()
        tempo_insercao_avl_total = 0
        for d in dados:
            tempo_insercao, _ = medir_tempo(arvore_avl.inserir, d['nome'], d['pontuacao'])
            tempo_insercao_avl_total += tempo_insercao
        resultados['tempo_insercao_avl'].append(tempo_insercao_avl_total)
 
        # Medir tempo de busca na árvore AVL
        tempo_busca_avl, _ = medir_tempo(arvore_avl.buscar_por_pontuacao, pontuacao_busca)
        resultados['tempo_busca_avl'].append(tempo_busca_avl * 1000)  # Converter para ms
 
        # Medir tempo de busca sequencial em dicionários
        tempo_busca_seq_dicionario, _ = medir_tempo(buscar_por_pontuacao_dicionarios, dados, pontuacao_busca)
        resultados['tempo_busca_seq_dicionario'].append(tempo_busca_seq_dicionario * 1000)  # Converter para ms
 
        # Ordenar os dados
        tempo_ordenacao_dicionario, lista_dicionarios_ordenada = medir_tempo(ordenar_dicionarios, dados)
        resultados['tempo_ordenacao_dicionario'].append(tempo_ordenacao_dicionario)
 
        # Medir tempo de busca binária em dicionários ordenados
        tempo_busca_bin_dicionario, _ = medir_tempo(busca_binaria_dicionarios, lista_dicionarios_ordenada, pontuacao_busca)
        resultados['tempo_busca_bin_dicionario'].append(tempo_busca_bin_dicionario * 1000)  # Converter para ms
 
        # Exibir resultados para cada tamanho n
        print(f"Tempo de inserção na AVL: {tempo_insercao_avl_total:.4f} segundos")
        print(f"Tempo de busca AVL: {tempo_busca_avl*1000:.6f} ms")
        print(f"Tempo de busca sequencial Dicionário: {tempo_busca_seq_dicionario*1000:.6f} ms")
        print(f"Tempo de ordenação Dicionário: {tempo_ordenacao_dicionario:.4f} segundos")
        print(f"Tempo de busca binária Dicionário: {tempo_busca_bin_dicionario*1000:.6f} ms\n")
 
    return resultados
 
# Defina os tamanhos a serem testados
tamanhos = [10000, 50000, 100000, 500000]  # Você pode adicionar 1_000_000 se o seu ambiente suportar
 
# Executar os testes
resultados = executar_testes_escalabilidade(tamanhos)
 
# Plotar os resultados em um único gráfico
plt.figure(figsize=(12, 8))
plt.plot(resultados['n'], resultados['tempo_busca_seq_dicionario'], label='Busca Sequencial')
plt.plot(resultados['n'], resultados['tempo_busca_bin_dicionario'], label='Busca Binária')
plt.plot(resultados['n'], resultados['tempo_busca_avl'], label='Busca na Árvore AVL')
plt.xlabel('Tamanho do Conjunto de Dados (n)')
plt.ylabel('Tempo de Busca (ms)')
plt.title('Comparação dos Tempos de Busca: Sequencial, Binária e AVL')
plt.legend()
plt.grid(True)
plt.show()
 