import os
import re
import shutil

def organizar_documentos(diretorio_origem):
    # Iterar sobre os arquivos no diretório de origem
    for arquivo in os.listdir(diretorio_origem):
        caminho_completo = os.path.join(diretorio_origem, arquivo)

        # Verificar se é um arquivo e se começa com CPF ou CNPJ
        if os.path.isfile(caminho_completo) and re.match(r'^\d{11,14}', arquivo):
            # Extrair o CPF ou CNPJ do nome do arquivo
            cnpj_cpf = re.match(r'^(\d{11,14})', arquivo).group(1)

            # Criar o diretório com base no CPF ou CNPJ
            diretorio_empresa = os.path.join(diretorio_origem, cnpj_cpf)
            if not os.path.exists(diretorio_empresa):
                os.makedirs(diretorio_empresa)

            # Mover o arquivo para o diretório da empresa
            shutil.move(caminho_completo, os.path.join(diretorio_empresa, arquivo))

if __name__ == "__main__":
    # Definir o diretório de origem
    diretorio_origem = r"C:\Users\danie\Documents\###CND"

    # Chamar a função para organizar os documentos
    organizar_documentos(diretorio_origem)