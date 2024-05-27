import pandas as pd
from Lagrange import resolverL
from Quadratica import resolverQ
from DiferencasDivididas import ResolverDD
from DiferencasFinitas import ResolverDF

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

# Função para obter os pontos para interpolação quadrática manualmente
def obter_pontos_quadraticos_manual():
    pontos = []
    for i in range(3):
        ano = int(input(f"Digite o ano do ponto {i + 1}: "))
        fecundidade = float(input(f"Digite a fecundidade do ponto {i + 1}: "))
        pontos.append((ano, fecundidade))
    return pontos

# Função para mostrar o menu e obter a escolha do usuário
def mostrar_menu():
    print("\nEscolha o método de interpolação:")
    print("1. Lagrange")
    print("2. Quadrática")
    print("3. Diferenças Divididas")
    print("4. Diferenças Finitas")
    return int(input("Digite o número do método escolhido: "))

# Solicitar método de interpolação e ano ao usuário
metodo = mostrar_menu()
ano_usuario = int(input("Digite o ano para interpolar: "))

# Inicializar variáveis para os resultados
resultados = {
    'Método': [],
    'Ano': [],
    'Fecundidade Estimada': [],
    'Tempo de Execução (s)': []
}

# Interpolação baseada no método escolhido
if metodo == 1:
    interpolacao = resolverL(pontos_conhecidos)
    previsao_fecundidade, tempo_execucao = interpolacao.interpolar(ano_usuario)
    resultados['Método'].append('Lagrange')
    resultados['Ano'].append(ano_usuario)
    resultados['Fecundidade Estimada'].append(previsao_fecundidade)
    resultados['Tempo de Execução (s)'].append(tempo_execucao-1)

elif metodo == 2:
    pontos_quadraticos = obter_pontos_quadraticos_manual()
    tipo_quadratica = input("Digite 'direto' para interpolação quadrática direta ou 'iterativo' para interpolação quadrática iterativa: ").strip().lower()
    interpolacao = resolverQ(pontos_quadraticos)
    previsao_fecundidade, tempo_execucao = interpolacao.interpolar(ano_usuario, tipo_quadratica)
    resultados['Método'].append(f'Quadrática ({tipo_quadratica.capitalize()})')
    resultados['Ano'].append(ano_usuario)
    resultados['Fecundidade Estimada'].append(previsao_fecundidade)
    resultados['Tempo de Execução (s)'].append(tempo_execucao-1)

elif metodo == 3:
    interpolacao = ResolverDD(pontos_conhecidos)
    previsao_fecundidade, tempo_execucao = interpolacao.interpolar(ano_usuario)
    resultados['Método'].append('Diferenças Divididas')
    resultados['Ano'].append(ano_usuario)
    resultados['Fecundidade Estimada'].append(previsao_fecundidade)
    resultados['Tempo de Execução (s)'].append(tempo_execucao-1)

elif metodo == 4:
    interpolacao = ResolverDF(pontos_conhecidos)
    previsao_fecundidade, tempo_execucao = interpolacao.interpolar(ano_usuario)
    resultados['Método'].append('Diferenças Finitas')
    resultados['Ano'].append(ano_usuario)
    resultados['Fecundidade Estimada'].append(previsao_fecundidade)
    resultados['Tempo de Execução (s)'].append(tempo_execucao-1)

else:
    print("Método de interpolação desconhecido.")

# Imprimir resultados no console
print("\nResultados:")
for i in range(len(resultados['Método'])):
    print(f"Método: {resultados['Método'][i]}")
    print(f"Ano: {resultados['Ano'][i]}")
    print(f"Fecundidade Estimada: {resultados['Fecundidade Estimada'][i]}")
    print(f"Tempo de Execução (s): {resultados['Tempo de Execução (s)'][i]}")
    print("-" * 30)

print("Processo de interpolação concluído.")
