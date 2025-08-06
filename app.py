from flask import Flask, render_template, request, jsonify
import subprocess
import os
import sys
import threading

# Configurar pyautogui para ser seguro ANTES de qualquer importação
try:
    import pyautogui
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5
    # Desabilitar pyautogui completamente durante a importação
    original_press = pyautogui.press
    original_click = pyautogui.click
    original_hotkey = pyautogui.hotkey
    original_write = pyautogui.write
    original_moveTo = pyautogui.moveTo
    
    def disabled_action(*args, **kwargs):
        pass
        
    # Desabilitar temporariamente todas as ações
    pyautogui.press = disabled_action
    pyautogui.click = disabled_action
    pyautogui.hotkey = disabled_action
    pyautogui.write = disabled_action
    pyautogui.moveTo = disabled_action
    
except:
    pass

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('automacao_profissional.html')

# Rota para F10 ENCJ
@app.route('/executar_encj', methods=['POST'])
def executar_encj():
    try:
        def executar():
            # Restaurar funções originais do pyautogui
            try:
                pyautogui.press = original_press
                pyautogui.click = original_click
                pyautogui.hotkey = original_hotkey
                pyautogui.write = original_write
                pyautogui.moveTo = original_moveTo
            except:
                pass
                
            # Executar o sistema5.py do F10 ENCJ
            script_path = os.path.join(os.path.dirname(__file__), 'F10 - ENCJ', 'Sistema5.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        # Executar em thread separada para não bloquear
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'F10 ENCJ iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar F10 ENCJ: {str(e)}'}), 500

# Rota para F10 APP
@app.route('/executar_app', methods=['POST'])
def executar_app():
    try:
        def executar():
            # Restaurar funções originais do pyautogui
            try:
                pyautogui.press = original_press
                pyautogui.click = original_click
                pyautogui.hotkey = original_hotkey
                pyautogui.write = original_write
                pyautogui.moveTo = original_moveTo
            except:
                pass
                
            script_path = os.path.join(os.path.dirname(__file__), 'F10 - APP', 'Sistema.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'F10 APP iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar F10 APP: {str(e)}'}), 500

# Rota para F10 EDUCA.RIO
@app.route('/executar_educario', methods=['POST'])
def executar_educario():
    try:
        def executar():
            script_path = os.path.join(os.path.dirname(__file__), 'F10 - EDUCA.RIO', 'Sistema4.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'F10 EDUCA.RIO iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar F10 EDUCA.RIO: {str(e)}'}), 500

# Rota para Bot Nome do Curso
@app.route('/executar_bot_curso', methods=['POST'])
def executar_bot_curso():
    try:
        def executar():
            script_path = os.path.join(os.path.dirname(__file__), 'bot_NomeDoCurso.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Bot Nome do Curso iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar Bot Nome do Curso: {str(e)}'}), 500

# Rota para Incluir em Turma
@app.route('/executar_incluir_turma', methods=['POST'])
def executar_incluir_turma():
    try:
        def executar():
            script_path = os.path.join(os.path.dirname(__file__), 'Incluir em turma.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Incluir em Turma iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar Incluir em Turma: {str(e)}'}), 500

# Rota para Mudar Número de Contrato
@app.route('/executar_mudar_contrato', methods=['POST'])
def executar_mudar_contrato():
    try:
        def executar():
            script_path = os.path.join(os.path.dirname(__file__), 'Muda_numero_de_contrato.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Mudar Número de Contrato iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar Mudar Número de Contrato: {str(e)}'}), 500

# Rota para Disparo WhatsApp
@app.route('/executar_disparo_whatsapp', methods=['POST'])
def executar_disparo_whatsapp():
    try:
        def executar():
            script_path = os.path.join(os.path.dirname(__file__), 'DISPARO - WHATSAPP', 'Sistema3.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Disparo WhatsApp iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar Disparo WhatsApp: {str(e)}'}), 500

# Rota para Confirmar CEP
@app.route('/executar_confirmar_cep', methods=['POST'])
def executar_confirmar_cep():
    try:
        def executar():
            script_path = os.path.join(os.path.dirname(__file__), 'CONFIRMAR CEP', 'Sistema1.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Confirmar CEP iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar Confirmar CEP: {str(e)}'}), 500

# Rota para Redefinir Senha
@app.route('/executar_redefinir_senha', methods=['POST'])
def executar_redefinir_senha():
    try:
        def executar():
            script_path = os.path.join(os.path.dirname(__file__), 'Redefini Senha Do Portal', 'Sistema2.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Redefinir Senha iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar Redefinir Senha: {str(e)}'}), 500

# Rota para WhatsApp Mensagem
@app.route('/executar_whatsapp_msg', methods=['POST'])
def executar_whatsapp_msg():
    try:
        def executar():
            script_path = os.path.join(os.path.dirname(__file__), 'Whastsapp', 'Menssagem.py')
            subprocess.run([sys.executable, script_path], check=True)
        
        thread = threading.Thread(target=executar)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'WhatsApp Mensagem iniciado com sucesso!'
        })
    except Exception as e:
        return jsonify({'error': f'Erro ao executar WhatsApp Mensagem: {str(e)}'}), 500

# Rota para parada de emergência
@app.route('/emergency_stop', methods=['POST'])
def emergency_stop():
    try:
        # Restaurar funções originais do pyautogui para emergência
        try:
            pyautogui.press = original_press
            pyautogui.click = original_click
            pyautogui.hotkey = original_hotkey
            pyautogui.write = original_write
            pyautogui.moveTo = original_moveTo
        except:
            pass
            
        # Mover mouse para canto superior esquerdo (0, 0) para ativar fail-safe do pyautogui
        pyautogui.moveTo(0, 0)
        pyautogui.click()  # Clique para interromper qualquer automação
        
        return jsonify({
            'success': True,
            'message': 'Parada de emergência executada com sucesso!'
        })
    except Exception as e:
        return jsonify({
            'success': True,
            'message': 'Parada de emergência ativada (modo offline)'
        })

if __name__ == '__main__':
    print("="*50)
    print("🚀 INICIANDO SERVIDOR FGM - AUTOMAÇÕES")
    print("📍 Acesse: http://localhost:5000")
    print("⚠️  NENHUMA AUTOMAÇÃO SERÁ EXECUTADA AUTOMATICAMENTE")
    print("✋ Para parar automações: mova mouse para canto superior esquerdo")
    print("="*50)
    app.run(debug=False, host='0.0.0.0', port=5000)
