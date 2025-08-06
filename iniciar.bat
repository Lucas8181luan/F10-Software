@echo off
title FGM - Automações FGM
color 0A

echo ========================================
echo    FGM - AUTOMAÇÕES FGM
echo ========================================
echo.

echo Verificando e instalando dependencias...
echo.

REM Instalar dependências
pip install -r requirements.txt

echo.
echo ========================================
echo    INICIANDO SERVIDOR FGM...
echo ========================================
echo.
echo Aguarde 3 segundos...
echo O navegador será aberto automaticamente
echo Para parar o servidor, pressione Ctrl+C
echo.
echo IMPORTANTE: Mova o mouse para o canto superior esquerdo para parar qualquer automacao
echo.

REM Definir variável de ambiente para evitar execução automática
set FLASK_ENV=production
set PYTHONPATH=%cd%

REM Abrir navegador após 3 segundos em background
start "" cmd /c "timeout /t 3 >nul && start http://localhost:5000"

REM Iniciar o servidor Flask
python app.py

pause