# F10 Software - Central de Controle

## 🚀 Descrição

Interface web moderna para centralizar todas as funcionalidades do F10 Software em um só lugar. Com uma interface intuitiva e responsiva, você pode executar todas as automações e sistemas com apenas um clique.

## ✨ Funcionalidades

### 🔍 Buscar Contratos
- **Busca por ID de Pessoa**: Integra com a API do F10 para buscar contratos específicos
- **Exportação CSV**: Salva automaticamente os resultados em arquivo CSV
- **Interface amigável**: Campos de entrada com validação

### ⚙️ Sistemas Principais
- **F10 - ENCJ**: Sistema de gestão ENCJ
- **F10 - APP**: Aplicação principal do F10
- **F10 - EDUCA.RIO**: Sistema educacional

### 🤖 Automação e Bots
- **Bot Nome do Curso**: Automação para inserir nomes de cursos
- **Incluir em Turma**: Automação para inclusão em turmas
- **Mudar Número de Contrato**: Alteração automatizada de contratos

### 💬 Comunicação
- **Disparo WhatsApp**: Sistema de disparo de mensagens

### 🔧 Utilitários
- **Confirmar CEP**: Validação de CEPs
- **Redefinir Senha**: Sistema de redefinição de senhas

## 🛠️ Instalação e Uso

### Método 1: Executar via Bat (Recomendado)
1. Clique duas vezes no arquivo `iniciar.bat`
2. O script instalará automaticamente as dependências
3. Abrirá o servidor web
4. Acesse `http://localhost:5000` no seu navegador

### Método 2: Instalação Manual
```bash
# Instalar dependências
pip install -r requirements.txt

# Iniciar servidor
python app.py
```

## 🌐 Como Usar

1. **Iniciar o Sistema**: Execute `iniciar.bat` ou `python app.py`
2. **Acessar Interface**: Abra `http://localhost:5000` no navegador
3. **Usar Funcionalidades**: Clique nos botões para executar as automações
4. **Buscar Contratos**: Preencha os campos e clique em "Buscar Contratos"

## 📋 Requisitos

- Python 3.7+
- Windows (devido ao uso de pyautogui)
- Acesso à internet para a API F10

## 🔧 Dependências

- Flask: Framework web
- pandas: Manipulação de dados CSV
- requests: Requisições HTTP para API
- pyautogui: Automação de interface
- pytesseract: OCR (se necessário)
- Pillow: Manipulação de imagens
- pyperclip: Manipulação de clipboard

## 📱 Interface

- **Design Responsivo**: Funciona em desktop, tablet e mobile
- **Tema Moderno**: Interface elegante com gradientes e animações
- **Alertas Visuais**: Feedback imediato para o usuário
- **Loading States**: Indicadores de carregamento durante processos

## 🔒 Segurança

- API Key configurada no código
- Execução local para maior segurança
- Logs de requisições para auditoria

## 🆘 Solução de Problemas

1. **Erro de dependências**: Execute `pip install -r requirements.txt`
2. **Porta ocupada**: Mude a porta no arquivo `app.py` (linha final)
3. **Erro de permissão**: Execute como administrador
4. **API não funciona**: Verifique a chave API no arquivo `pessoa_id.py`

## 📞 Suporte

Para problemas ou sugestões, entre em contato através dos logs do sistema.

## 📅 Versão

- **Versão Atual**: 1.0
- **Última Atualização**: Agosto 2025
- **Desenvolvedor**: Lucas
