import csv

def leitor_csv(nome_arquivo):
    # Inicializa uma lista para armazenar os dicionários
    pacientes = []

    # Abrir e ler o arquivo CSV
    with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
        # Cria um leitor de CSV
        reader = csv.DictReader(csvfile)
        
        # Itera sobre cada linha no arquivo CSV
        for row in reader:
            # Cria um dicionário com apenas as colunas desejadas
            paciente = {
                'idade': int(row['idade']),
                'imc': int(row['imc']),
                'glicose': int(row['glicose']),
                'atividade': int(row['atividade'])
            }
            # Adiciona o dicionário à lista
            pacientes.append(paciente)

    return pacientes
