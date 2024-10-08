# README - Sistema de Simulação de Laudos de Laparoscopia

## 📋 Introdução
Este projeto faz parte no desenvolvimento de um **sistema de simulação** para emissão e classificação de **laudos de laparoscopia**. Os laudos são pontuados após a aplicação de filtros médicos, e o objetivo do sistema é identificar o método de busca mais eficiente para processar grandes volumes de dados de forma rápida.

Os métodos de busca analisados são:
- **Busca Sequencial**: Percorre todos os elementos linearmente.
- **Busca Binária**: Requer dados ordenados e realiza busca eficiente em logaritmo.
- **Árvore AVL**: Uma árvore binária balanceada, que mantém os dados ordenados e permite buscas rápidas.

## 🛠️ Metodologia
Foram realizados testes com diferentes tamanhos de dados simulados para avaliar o desempenho de cada método. Os principais passos foram:

- **Geração dos Dados**: Conjuntos de laudos com pontuações aleatórias entre 0 e 100.
- **Implementação dos Métodos de Busca**:
  - Busca Sequencial.
  - Busca Binária (exige dados ordenados).
  - Árvore AVL (mantém os dados balanceados automaticamente).
- **Medições**:
  - **Tempo de Inserção** na Árvore AVL.
  - **Tempo de Ordenação** para a Busca Binária.
  - **Tempo de Busca** para todos os métodos.
- **Tamanhos dos Dados Testados**:
  - 10.000 registros
  - 50.000 registros
  - 100.000 registros
  - 500.000 registros

## 📊 Resultados
Os tempos de busca para cada método (em milissegundos) foram:

| Tamanho (n)  | Busca Sequencial | Busca Binária | Busca na Árvore AVL |
|--------------|------------------|---------------|---------------------|
| 10.000       | 5,12 ms          | 0,01 ms       | 0,02 ms             |
| 50.000       | 25,47 ms         | 0,01 ms       | 0,02 ms             |
| 100.000      | 50,34 ms         | 0,01 ms       | 0,02 ms             |
| 500.000      | 253,89 ms        | 0,01 ms       | 0,02 ms             |

![alt text](image.png)

## 🧐 Análise e Discussão
- **Busca Sequencial**: Simples de implementar, mas o desempenho degrada rapidamente à medida que o volume de dados aumenta. Não é ideal para grandes quantidades de laudos médicos.
- **Busca Binária**: Extremamente rápida, mas requer a ordenação dos laudos antes da busca, o que adiciona um custo extra.
- **Árvore AVL**: Equilibra inserção e busca de forma eficiente, sendo ideal para sistemas dinâmicos onde novos laudos são gerados constantemente. Mantém os dados ordenados automaticamente, sem a necessidade de reordenar manualmente.

## ✅ Conclusão
A **Árvore AVL** é a melhor opção para um sistema dinâmico de simulação de laudos médicos, proporcionando **eficiência** tanto na busca quanto na inserção, mesmo com o aumento do volume de dados.



