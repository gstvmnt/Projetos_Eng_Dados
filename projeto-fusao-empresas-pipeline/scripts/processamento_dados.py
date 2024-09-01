import json
import csv

class Dados:
    
    def __init__(self, dados):
        self.dados = dados
        self.nomes_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()
        
        
    def __read_json(path):
        dados_json = []
        with open(path, 'r') as file:
            dados_json = json.load(file)
            return dados_json


    def __read_csv(path):
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
            return dados_csv


    @classmethod
    def read_data(cls, path, tipo_dados):
        file_data = []
        
        if tipo_dados == 'csv':
            file_data = cls.__read_csv(path)
        elif tipo_dados == 'json':
            file_data = cls.__read_json(path)

        return cls(file_data)
    
    
    def __get_columns(self):
        return list(self.dados[-1].keys())
    
    
    def rename_columns(self, key_mapping):
        new_data = []
        
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_data.append(dict_temp)
            
        self.dados = new_data
        self.nomes_colunas = self.__get_columns()
        
        
    def __size_data(self):
        return len(self.dados)
    
    
    def join(dadosA, dadosB):
        dados_combinados = []
        dados_combinados.extend(dadosA.dados)
        dados_combinados.extend(dadosB.dados)
        
        return Dados(dados_combinados)
    
    
    def __data_to_table(self):
        dados_tabela = [self.nomes_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nomes_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_tabela.append(linha)
        return dados_tabela
    
    
    def write_data(self, path):
        dados_tabela = self.__data_to_table()
        
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_tabela)