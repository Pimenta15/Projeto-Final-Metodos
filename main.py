import pandas as pd
import numpy as np
from interpolacao import InterpolacaoLagrange
# Caminho para o arquivo Excel (com barras normais para compatibilidade)
arquivo_excel = 'Base de Dados.xlsx'

# Leitura da tabela Excel
df = pd.read_excel(arquivo_excel)

# Imprimir os nomes das colunas para verificação
print("Colunas no DataFrame:", df.columns)

# Remover espaços e converter para minúsculas (opcional)
df.columns = df.columns.str.strip().str.lower()

print("Colunas no DataFrame (ajustadas):", df.columns)

# colunas ajustadas são 'ano' e 'população'
x = df['ano'].values
y = df['população'].values

pontos_conhecidos = list(zip(x, y))

# Exibir a matriz
interpolacao_lagrange = InterpolacaoLagrange(pontos_conhecidos)
# Estimar a população nos próximos 10 anos
ano_atual = max(x)
previsoes = {}
tempos_execucao = {}
for i in range(1, 11):
    ano_futuro = ano_atual + i
    previsao_populacao, tempo_execucao = interpolacao_lagrange.interpolar(ano_futuro)
    previsoes[ano_futuro] = previsao_populacao
    tempos_execucao[ano_futuro] = tempo_execucao

# Exibir os resultados
print("Previsões de população para os próximos 10 anos:")
for ano, populacao in previsoes.items():
    print(f"Ano {ano}: População estimada = {populacao:.2f}, Tempo de execução = {tempos_execucao[ano]:.6f} segundos")
