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

# Função para obter os pontos para interpolação quadrática
def obter_pontos_quadraticos(ano, pontos_conhecidos):
    if 1940 <= ano <= 1960:
        pontos = [(1940, next(y for x, y in pontos_conhecidos if x == 1940)),
                  (1950, next(y for x, y in pontos_conhecidos if x == 1950)),
                  (1960, next(y for x, y in pontos_conhecidos if x == 1960))]
    elif 1961 <= ano <= 1980:
        pontos = [(1960, next(y for x, y in pontos_conhecidos if x == 1960)),
                  (1970, next(y for x, y in pontos_conhecidos if x == 1970)),
                  (1980, next(y for x, y in pontos_conhecidos if x == 1980))]
    elif 1981 <= ano <= 2000:
        pontos = [(1980, next(y for x, y in pontos_conhecidos if x == 1980)),
                  (1990, next(y for x, y in pontos_conhecidos if x == 1990)),
                  (2000, next(y for x, y in pontos_conhecidos if x == 2000))]
    elif 2001 <= ano <= 2020:
        pontos = [(2000, next(y for x, y in pontos_conhecidos if x == 2000)),
                  (2010, next(y for x, y in pontos_conhecidos if x == 2010)),
                  (2020, next(y for x, y in pontos_conhecidos if x == 2020))]
    else:
        raise ValueError(f"Não há pontos suficientes para interpolação quadrática para o ano {ano}")
    
    return pontos

# Interpolação para todos os anos de 1960 a 2010
anos_interpolacao = list(range(1940, 2021))
resultados = {
    'Método': [],
    'Ano': [],
    'Fecundidade Estimada': [],
    'Tempo de Execução (s)': []
}


for ano in anos_interpolacao:
    #Interpolação de Lagrange
    interpolacao_lagrange = resolverL(pontos_conhecidos)
    previsao_fecundidade_lagrange, tempo_execucao_lagrange = interpolacao_lagrange.interpolar(ano)
    
    resultados['Método'].append('Lagrange')
    resultados['Ano'].append(ano)
    resultados['Fecundidade Estimada'].append(previsao_fecundidade_lagrange)
    resultados['Tempo de Execução (s)'].append(tempo_execucao_lagrange-1)

    # Interpolação Quadrática (Direto)
    try:
        pontos_quadraticos = obter_pontos_quadraticos(ano, pontos_conhecidos)
        interpolacao_quadratica = resolverQ(pontos_quadraticos)
        previsao_fecundidade_quadratica, tempo_execucao_quadratica = interpolacao_quadratica.interpolar(ano, "direto")
        
        resultados['Método'].append('Quadrática (Direto)')
        resultados['Ano'].append(ano)
        resultados['Fecundidade Estimada'].append(previsao_fecundidade_quadratica)
        resultados['Tempo de Execução (s)'].append(tempo_execucao_quadratica-1)
    except ValueError as e:
        print(e)

    # Interpolação usando Diferenças Diretas
    interpolacao_DD = ResolverDD(pontos_conhecidos)
    previsao_fecundidade_DD, tempo_execucao_DD = interpolacao_DD.interpolar(ano)

    resultados['Método'].append('Diferenças Diretas')
    resultados['Ano'].append(ano)
    resultados['Fecundidade Estimada'].append(previsao_fecundidade_DD)
    resultados['Tempo de Execução (s)'].append(tempo_execucao_DD-1)

    # Interpolação usando Diferenças Finitas
    interpolacao_DF = ResolverDF(pontos_conhecidos)
    previsao_fecundidade_DF, tempo_execucao_DF = interpolacao_DF.interpolar(ano)

    resultados['Método'].append('Diferenças Finitas')
    resultados['Ano'].append(ano)
    resultados['Fecundidade Estimada'].append(previsao_fecundidade_DF)
    resultados['Tempo de Execução (s)'].append(tempo_execucao_DF-1)

# Converter resultados para DataFrame e salvar em Excel
df_resultados = pd.DataFrame(resultados)
df_resultados.to_excel('auxiliar.xlsx', index=False)

print("Resultados salvos no arquivo 'auxiliar.xlsx'")
