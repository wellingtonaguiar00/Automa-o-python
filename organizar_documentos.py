import os
import re
import shutil

def organizar_documentos(diretorio_origem):
    for arquivo in os.listdir(diretorio_origem):
        caminho_completo = os.path.join(diretorio_origem, arquivo)
        
        if os.path.isfile(caminho_completo) and re.match(r'^\d{11,14}', arquivo):
            # Extrair o CPF ou CNPJ do nome do arquivo
            cnpj_cpf = re.match(r'^(\d{11,14})', arquivo).group(1)
            
            diretorio_empresa = os.path.join(diretorio_origem, cnpj_cpf)
            if not os.path.exists(diretorio_empresa):
                os.makedirs(diretorio_empresa)

            shutil.move(caminho_completo, os.path.join(diretorio_empresa, arquivo))

if __name__ == "__main__":
    # Definir o diretório de origem
    diretorio_origem = r"C:\Users\danie\Documents\###CND"
    
    organizar_documentos(diretorio_origem)
