import os
import shutil
import time

# Diretórios
pasta_origem = 'Z:/ems_23v08_go/Retornos'
pasta_destino = 'Z:/teste/RetornoNotasNCFarma/Notas_GO'

while True:
    # Lista os arquivos na pasta de destino
    arquivos_destino = os.listdir(pasta_destino)
    
    for arquivo in arquivos_destino:
        # Obtém o caminho completo do arquivo na pasta de destino
        caminho_arquivo_destino = os.path.join(pasta_destino, arquivo)
        # Verifica se o arquivo existe há mais de uma hora
        if time.time() - os.path.getctime(caminho_arquivo_destino) >= 600:  # 1800 segundos = 30 min  # 1200 segundos = 20 min # 900 segundos = 15 min # 600 segundos = 10 min
            # Verifica se o arquivo não existe na pasta de origem
            caminho_arquivo_origem = os.path.join(pasta_origem, arquivo)
            if not os.path.exists(caminho_arquivo_origem):
                # Move o arquivo de volta para a pasta original
                shutil.move(caminho_arquivo_destino, pasta_origem)
                print(f"Arquivo {arquivo} movido de volta para a pasta de origem.")
            else:
                print(f"Arquivo {arquivo} já existe na pasta de origem. Ignorando.")
    
    # Aguarda um curto período antes de verificar novamente
    time.sleep(60)  # Verifica a cada 60 segundos