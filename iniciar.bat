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
echo    INICIANDO AUTOMAÇÕES FGM...
echo ========================================
echo.
echo Acesse: http://localhost:5000
echo Para parar o servidor, pressione Ctrl+C
echo.

REM Iniciar o servidor Flask
python app_automacao.py

pause