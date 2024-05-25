import pandas as pd
from Lagrange import resolverL
from Quadratica import resolverQ

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
i = 0
print("Pontos conhecidos:")
for xi, yi in pontos_conhecidos:
    print(f"x{i} = {xi}, yi = {yi}")
    i = i+1

# Instanciar a interpolação de Lagrange
interpolacao_lagrange = resolverL(pontos_conhecidos)
# Solicitar o ano ao usuário
ano_usuario = int(input("Digite o ano para o qual deseja interpolar a população (ex: 2004): "))

# Interpolar taxa de fecundidade para o ano solicitado
previsao_fecundidade, tempo_execucao = interpolacao_lagrange.interpolar(ano_usuario)

# Exibir o resultado
print("Interpolação por Lagrange")
print(f"Para o ano {ano_usuario}:")
print(f"Taxa de fecundidade estimada: {previsao_fecundidade:.2f}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
print("-------------------------------------------------------------------")

# Solicitar ao usuário para digitar 3 anos
anos_usuario = []
for i in range(3):
    ano = int(input(f"Digite o ano {i+1}: "))
    anos_usuario.append(ano)

# Filtrar pontos conhecidos para incluir apenas os anos fornecidos pelo usuário
pontos_conhecidos_filtrados = []
for ponto in pontos_conhecidos:
    if ponto[0] in anos_usuario:
        pontos_conhecidos_filtrados.append(ponto)


interpolacao_quadratica = resolverQ(pontos_conhecidos_filtrados)
previsao_fecundidade, tempo_execucao = interpolacao_quadratica.interpolar(ano_usuario, "direto")

print("Interpolação por Quadratica de modo direto")
print(f"Para o ano {ano_usuario}:")
print(f"Taxa de fecundidade estimada: {previsao_fecundidade:.2f}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
print("-------------------------------------------------------------------")

interpolacao_quadratica = resolverQ(pontos_conhecidos_filtrados)
previsao_fecundidade, tempo_execucao = interpolacao_quadratica.interpolar(ano_usuario, "iterativo")

print("Interpolação por Quadratica de modo iterativo")
print(f"Para o ano {ano_usuario}:")
print(f"Taxa de fecundidade estimada: {previsao_fecundidade:.2f}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
print("-------------------------------------------------------------------")