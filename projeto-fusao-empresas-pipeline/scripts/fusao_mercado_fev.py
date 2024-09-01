from processamento_dados import Dados


pathA = 'data_raw/dados_empresaA.json'
pathB = 'data_raw/dados_empresaB.csv'


# Extract

dados_empresaA = Dados.read_data(pathA, 'json')
print(f"Colunas da empresa A: {dados_empresaA.nomes_colunas}, base com {dados_empresaA.qtd_linhas} linhas")
dados_empresaB = Dados.read_data(pathB, 'csv')
print(f"Colunas da empresa B: {dados_empresaB.nomes_colunas}, base com {dados_empresaB.qtd_linhas} linhas")


# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',                      #DE PARA de nome das colunas
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}


dados_empresaB.rename_columns(key_mapping)
print(f'Nome das colunas da empresa B atualizado: {dados_empresaB.nomes_colunas}')

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f'Colunas dos dados da fusão: {dados_fusao.nomes_colunas}')
print(f'Tamanho dos dados de fusão: {dados_fusao.qtd_linhas}')


# Load

path_dados_fusao = 'data_processed/dados_fusao.csv'
dados_fusao.write_data(path_dados_fusao)
print(f'Arquivo de fusao salvo em: {path_dados_fusao}')


