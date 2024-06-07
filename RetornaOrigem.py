import datetime
import os
import shutil
import time

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"[{current_time}]")

# Diretórios
pastas_origem = ['//192.168.2.7/Pastas_FTP/ems_23v08_go/Retornos', 
                '//192.168.2.7/Pastas_FTP/ems_23v08_to/Retornos', 
                '//192.168.2.7/Pastas_FTP/ems_23v08_ma/Retornos', 
                '//192.168.2.7/Pastas_FTP/ems_23v08_pa/Retornos', 
                '//192.168.2.7/Pastas_FTP/ems_23v08_pi/Retornos',
                '//192.168.2.7/Pastas_FTP/ems_23v08_am/Retornos',
                '//192.168.2.7/Pastas_FTP/ems_23v08_df/Retornos'] 
pastas_destino = ['//192.168.2.7/Pastas_FTP/teste/RetornoNotasNCFarma/Notas_GO', 
                '//192.168.2.7/Pastas_FTP/teste/RetornoNotasNCFarma/Notas_TO',
                '//192.168.2.7/Pastas_FTP/teste/RetornoNotasNCFarma/Notas_MA',
                '//192.168.2.7/Pastas_FTP/teste/RetornoNotasNCFarma/Notas_PA',
                '//192.168.2.7/Pastas_FTP/teste/RetornoNotasNCFarma/Notas_PI',
                '//192.168.2.7/Pastas_FTP/teste/RetornoNotasNCFarma/Notas_AM',
                '//192.168.2.7/Pastas_FTP/teste/RetornoNotasNCFarma/Notas_DF']

while True:
    for idx, pasta_destino in enumerate(pastas_destino):
        # Padrão de nome e diretório correspondente
        pasta_origem = pastas_origem[idx]
        
        try:
            # Lista os arquivos na pasta de destino
            arquivos_destino = os.listdir(pasta_destino)
            
            for arquivo in arquivos_destino:
                # Verifica se o arquivo existe há mais de 1 hora na pasta de destino
                caminho_arquivo_destino = os.path.join(pasta_destino, arquivo)
                if time.time() - os.path.getctime(caminho_arquivo_destino) >= 7200:  # 3600 segundos = 1 hora # 7200 segundos = 2 hora
                    # Verifica se o arquivo não existe na pasta de origem
                    caminho_arquivo_origem = os.path.join(pasta_origem, arquivo)
                    if not os.path.exists(caminho_arquivo_origem):
                        # Move o arquivo de volta para a pasta original
                        shutil.move(caminho_arquivo_destino, pasta_origem)
                        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(f"[{current_time}] Arquivo {arquivo} movido de volta {pasta_origem}.")
                    else:
                        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(f"[{current_time}] Arquivo {arquivo} já está em standby {pasta_origem}. Ignorando.")
        except Exception as e:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{current_time}] Erro ao acessar a pasta: {str(e)}")

    # Aguarda um curto período antes de verificar novamente
    time.sleep(60)  # Verifica a cada 60 segundos

# pyinstaller --onefile '.\RetornaOrigem.py'