import pandas as pd
import requests
from urllib.parse import quote

def buscar_pessoa_por_cpf(unidade_id, cpf):
    """
    Busca dados de uma pessoa específica por CPF em uma unidade
    Args:
        unidade_id (int): ID da unidade (ex: 831)
        cpf (str): CPF da pessoa (com ou sem formatação)
    Retorna:
        dict: Dados da pessoa ou None se não encontrado
    """
    # Remove formatação do CPF se existir
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    
    API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGVzc2FuZHJvQGdhbWEuY29tLmJyIiwiaXNzIjoiRjEwIEFQSSIsImlhdCI6MTc0ODAwOTkyMSwiZXhwIjoyMDMyMDI4MzIxfQ.gNHt7U1x97tzKAsNajrBK92eByq9WGKafFAn1uirSyc"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Codifica o CPF para URL (trata caracteres especiais)
    cpf_url = quote(cpf_limpo)
    API_URL = f"https://api.f10.com.br/unidade/pessoas/{unidade_id}?cnpjCpf={cpf_url}"

    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Lança erro para status 4XX/5XX
        
        dados = response.json()
        
        if dados:
            # Formata os dados para padronização
            pessoa = dados[0]
            return {
                'pessoa_id': pessoa.get('pessoa_id'),
                'nome': pessoa.get('nome'),
                'cpf': pessoa.get('cpf_cnpj'),
                'nascimento': pessoa.get('nascimento'),
                'email': pessoa.get('email'),
                'telefone': pessoa.get('telefone'),
                'celular': pessoa.get('celular'),
                'endereco': f"{pessoa.get('logradouro', '')} {pessoa.get('end_complemento', '')}".strip(),
                'bairro': pessoa.get('bairro'),
                'cidade': pessoa.get('cidade'),
                'estado': pessoa.get('estado'),
                'cep': pessoa.get('cep')
            }
        else:
            print(f"⚠️ Pessoa com CPF {cpf} não encontrada na unidade {unidade_id}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {str(e)}")
        return None

# --- Exemplo de uso ---
if __name__ == "__main__":
    # Teste com CPF formatado ou não
    resultado1 = buscar_pessoa_por_cpf(831, "852.402.811-49")
    
    if resultado1:
        print("\n🎉 Resultado 1 (CPF formatado):")
        print(pd.DataFrame([resultado1]))
