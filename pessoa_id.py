import pandas as pd
import requests
import os

# Variável global para contar as requisições
CONTADOR_REQUISICOES = 0
ARQUIVO_CSV = 'contratos.csv'

def salvar_contrato_no_csv(dados):
    """Salva os dados do contrato no arquivo CSV, adicionando uma nova linha"""
    try:
        # Converte o dicionário para DataFrame
        df = pd.DataFrame([dados])
        
        # Verifica se o arquivo já existe
        file_exists = os.path.exists(ARQUIVO_CSV)
        
        # Salva no CSV (append se existir, cria se não existir)
        df.to_csv(ARQUIVO_CSV, index=False, 
                 mode='a' if file_exists else 'w', 
                 header=not file_exists, 
                 encoding='utf-8-sig')
        
        print(f"✅ Dados salvos em {ARQUIVO_CSV}")
    except Exception as e:
        print(f"❌ Erro ao salvar CSV: {str(e)}")

def buscar_contratos_por_pessoa_id(unidade_id, pessoa_id):
    """
    Busca contratos de uma pessoa específica por ID em uma unidade
    
    Args:
        unidade_id (int/str): ID da unidade (ex: 831)
        pessoa_id (int/str): ID da pessoa no sistema
    
    Retorna:
        list: Lista de contratos ou None se não encontrado
    """
    global CONTADOR_REQUISICOES
    API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGVzc2FuZHJvQGdhbWEuY29tLmJyIiwiaXNzIjoiRjEwIEFQSSIsImlhdCI6MTc0ODAwOTkyMSwiZXhwIjoyMDMyMDI4MzIxfQ.gNHt7U1x97tzKAsNajrBK92eByq9WGKafFAn1uirSyc"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # URL com apenas unidade_id e pessoa_id como parâmetro
    url = f"https://api.f10.com.br/unidade/contratos/{unidade_id}?pessoaId={pessoa_id}"
    
    try:
        # Incrementa o contador de requisições
        CONTADOR_REQUISICOES += 1
        print(f"\n🔔 Requisição #{CONTADOR_REQUISICOES}")
        print(f"🔍 URL: {url}")
        
        response = requests.get(url, headers=headers)
        
        # Verifica o status code
        if response.status_code == 401:
            print("❌ Erro 401: Não autorizado")
            return None
        elif response.status_code == 404:
            print(f"⚠️ Nenhum contrato para ID {pessoa_id}")
            return None
        elif not response.ok:
            print(f"❌ Erro {response.status_code}: {response.text}")
            return None
        
        contratos = response.json()
        print("✅ Dados recebidos com sucesso")
        
        if not contratos:
            print(f"⚠️ Nenhum contrato para ID {pessoa_id}")
            return None
            
        # Processa os contratos
        contratos_processados = []
        for contrato in contratos:
            try:
                dados_contrato = {
                    'contrato_id': contrato.get('contrato_id'),
                    'numero_contrato': contrato.get('numero_contrato'),
                    'pessoa_id': contrato.get('pessoa_id'),
                    'titular_id': contrato.get('titular_id'),
                    'curso_id': contrato.get('curso_id'),
                    'status': contrato.get('status'),
                    'x_status': contrato.get('x_status'),
                    'matricula': contrato.get('matricula'),
                    'data_cancelamento': contrato.get('data_cancelamento'),
                    'vendedor_id': contrato.get('vendedor_id'),
                    'telemarketing_id': contrato.get('telemarketing_id'),
                    'fonte_id': contrato.get('fonte_id'),
                    'fonte': contrato.get('fonte')
                }
                
                salvar_contrato_no_csv(dados_contrato)
                contratos_processados.append(dados_contrato)
            except Exception as e:
                print(f"⚠️ Erro ao processar contrato: {str(e)}")
                continue
        
        return contratos_processados if contratos_processados else None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {str(e)}")
        return None
    except ValueError as e:
        print(f"❌ Erro no JSON: {str(e)}")
        return None
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
        return None


# Executar apenas se chamado diretamente
if __name__ == "__main__":
    resultados = buscar_contratos_por_pessoa_id(unidade_id="831", pessoa_id="166374")
    print(resultados)
