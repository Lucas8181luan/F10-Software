import requests
from urllib.parse import quote
from pprint import pprint

def buscar_contratos_por_cpf(cpf, unidade_id=831):
    """
    Busca e exibe contratos por CPF no terminal
    Args:
        cpf (str): CPF do contratante (com ou sem formatação)
        unidade_id (int): ID da unidade (opcional, default=831)
    """
    # Configuração da API
    API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGVzc2FuZHJvQGdhbWEuY29tLmJyIiwiaXNzIjoiRjEwIEFQSSIsImlhdCI6MTc0ODAwOTkyMSwiZXhwIjoyMDMyMDI4MzIxfQ.gNHt7U1x97tzKAsNajrBK92eByq9WGKafFAn1uirSyc"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Formata o CPF
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    cpf = quote(cpf_limpo)
    
    # URL da API
    API_URL = f"https://api.f10.com.br/unidade/contratos/{unidade_id}?cnpjCpf={cpf}"
    
    print(f"\n🔍 Buscando contratos para CPF: {cpf_limpo}...")

    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Verifica erros HTTP
        
        dados = response.json()
        
        if dados:
            print(f"\n✅ {len(dados)} contrato(s) encontrado(s):")
            print("-" * 50)
            
            for i, contrato in enumerate(dados, 1):
                print(f"\n📋 Contrato #{i}")
                print(f"ID: {contrato.get('contrato_id')}")
                print(f"Número: {contrato.get('numero_contrato')}")
                print(f"Status: {contrato.get('x_status')}")
                print(f"Matrícula: {contrato.get('matricula')}")
                print(f"Curso ID: {contrato.get('curso_id')}")
                print(f"Titular ID: {contrato.get('titular_id')}")
                print("-" * 30)
        else:
            print(f"\n⚠️ Nenhum contrato encontrado para o CPF {cpf_limpo}")
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Erro na requisição: {str(e)}")

# Exemplo de uso
if __name__ == "__main__":
    # Teste com CPF formatado ou não
    buscar_contratos_por_cpf("85240281149")  # Substitua por um CPF real
    # Ou: buscar_contratos_por_cpf("00000000000")
