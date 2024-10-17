
'''class Grafo:
    def __init__(self):
        self.vertices = {}

    def add_vertice(self, vertice):
        self.vertices[vertice] = []

    def add_aresta(self, v1, v2):
        self.vertices[v1].append(v2)
        self.vertices[v2].append(v1)  # Para grafos não direcionados
    def printar(self):
        print(self.vertices)

# Criando um grafo
grafo = Grafo()
grafo.add_vertice('A')
grafo.add_vertice('B')
grafo.add_vertice('C')
grafo.add_aresta('A', 'B')
grafo.add_aresta('B', 'C')
grafo.printar()'''

import networkx as nx
import random

def gerar_grafo_isomorfo(G):
    """Gera um grafo isomorfo a G.

    Args:
        G: O grafo original.

    Returns:
        Um novo grafo isomorfo a G.
    """

    # Cria uma lista com os vértices de G
    vertices = list(G.nodes)

    # Gera uma permutação aleatória dos vértices
    random.shuffle(vertices)

    # Cria um novo grafo vazio
    H = nx.Graph()

    # Adiciona as arestas ao novo grafo, usando a nova ordem dos vértices
    for u, v in G.edges:
        i = vertices.index(u)
        j = vertices.index(v)
        H.add_edge(i, j)

    return H

# Criando um grafo exemplo
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Gerando um grafo isomorfo
H = gerar_grafo_isomorfo(G)

print(G.edges)
print(H.edges)

# Verificando o isomorfismo
if nx.is_isomorphic(G, H):
    print("Os grafos são isomorfos")
else:
    print("Os grafos não são isomorfos")