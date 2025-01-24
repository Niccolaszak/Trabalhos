#tarefa 111 foi fazer a modularização
from utilidadesCeV import moeda
from utilidadesCeV import dado
g = dado.leia_dinheiro("Digite o valor para gerar um resumo: ")
moeda.resumo(g)