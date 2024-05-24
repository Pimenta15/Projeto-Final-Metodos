import pandas as pd
from Lagrange import resolver

# Caminho para o arquivo Excel
arquivo_excel = 'Base de Dados.xlsx'

# Leitura da tabela Excel
df = pd.read_excel(arquivo_excel)

# Ajustar os nomes das colunas
df.columns = df.columns.str.strip().str.lower()

# Extrair dados das colunas
x = df['ano'].values
y = df['fecundidade'].values

# Criar lista de pontos conhecidos
pontos_conhecidos = list(zip(x, y))

print("Pontos conhecidos:")
for xi, yi in pontos_conhecidos:
    print(f"xi = {xi}, yi = {yi}")

# Instanciar a interpolação de Lagrange
interpolacao_lagrange = resolver(pontos_conhecidos)

# Solicitar o ano ao usuário
ano_usuario = int(input("Digite o ano para o qual deseja interpolar a população (ex: 2020): "))

# Interpolar taxa de fecundidade para o ano solicitado
previsao_fecundidade, tempo_execucao = interpolacao_lagrange.interpolar(ano_usuario)

# Exibir o resultado
print(f"Para o ano {ano_usuario}:")
print(f"Taxa de fecundidade estimada: {previsao_fecundidade:.2f}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

