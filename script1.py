import os
import shutil
import time

# Padrão de nome inicial dos arquivos
padrao_inicio_nome = 'NOTEMS_'

# Diretórios
pasta_origem = 'Z:/ems_23v08_go/Retornos'
pasta_destino = 'Z:/teste/RetornoNotasNCFarma/Notas_GO'

while True:
    # Lista os arquivos na pasta de origem
    arquivos_origem = os.listdir(pasta_origem)
    
    for arquivo in arquivos_origem:
        # Verifica se o nome do arquivo começa com o padrão especificado
        if arquivo.startswith(padrao_inicio_nome):
            # Caminho completo do arquivo na pasta de origem
            caminho_arquivo_origem = os.path.join(pasta_origem, arquivo)
            # Caminho completo do arquivo na pasta de destino
            caminho_arquivo_destino = os.path.join(pasta_destino, arquivo)
            
            # Verifica se o arquivo foi criado nos últimos 20 minutos
            if time.time() - os.path.getctime(caminho_arquivo_origem) <= 600:  # 1200 segundos = 20 minutos # 900 segundos = 15 minutos
                # Verifica se o arquivo já existe na pasta de destino
                if not os.path.exists(caminho_arquivo_destino):
                    # Move o arquivo para a pasta de destino
                    shutil.move(caminho_arquivo_origem, pasta_destino)
                    print(f"Arquivo {arquivo} movido para a pasta de destino.")
                else:
                    print(f"Arquivo {arquivo} já existe na pasta de destino. Ignorando.")
            else:
                print(f"Arquivo {arquivo} não foi criado nos últimos 10 minutos. Ignorando.")
    
    # Aguarda um curto período antes de verificar novamente
    time.sleep(30)  # Verifica a cada 30 segundos
