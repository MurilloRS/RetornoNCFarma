import datetime
import os
import shutil
import time

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"[{current_time}]")
# Padrões de nome inicial dos arquivos e diretórios
padrao_inicio_nome = 'NOTEMS_'
# padrao_inicio_nome_ret = 'RETEMS_'

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
    for idx, pasta_origem in enumerate(pastas_origem):
        # Padrão de nome e diretório correspondente
        # padrao_inicio_nome = padrao_inicio_nome
        pasta_destino = pastas_destino[idx]
        
        try:
            # Lista os arquivos na pasta de origem
            arquivos_origem = os.listdir(pasta_origem)

            for arquivo in arquivos_origem:
                # Verifica se o nome do arquivo começa com o padrão especificado
                if arquivo.startswith(padrao_inicio_nome): #"""or arquivo.startswith(padrao_inicio_nome_ret)"""
                    # Caminho completo do arquivo na pasta de origem
                    caminho_arquivo_origem = os.path.join(pasta_origem, arquivo)
                    # Caminho completo do arquivo na pasta de destino
                    caminho_arquivo_destino = os.path.join(pasta_destino, arquivo)
                    
                    # Verifica se o arquivo foi criado nos últimos 20 minutos
                    if time.time() - os.path.getctime(caminho_arquivo_origem) <= 360:  # 1200 segundos = 20 minutos # 7200 segundos = 2 hora
                        # Verifica se o arquivo já existe na pasta de destino
                        if not os.path.exists(caminho_arquivo_destino):
                            # Move o arquivo para a pasta de destino
                            shutil.move(caminho_arquivo_origem, pasta_destino)
                            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            print(f"[{current_time}] Arquivo {arquivo} movido para standby {pasta_destino}.")
                        else:
                            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            print(f"[{current_time}] Arquivo {arquivo} já está em standby {pasta_destino}. Ignorando.")
                    # else:
                        # print(f"Arquivo {arquivo} não foi criado nos últimos 10 minutos. Ignorando.")
        except Exception as e:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{current_time}] Erro ao acessar a pasta: {str(e)}")

    time.sleep(20)  # Verifica a cada 20 segundos
# pyinstaller --onefile '.\EnviaStandby.py'