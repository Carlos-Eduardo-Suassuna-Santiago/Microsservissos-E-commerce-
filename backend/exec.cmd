@echo off
REM Criando diretório principal
mkdir order-service

REM Entrando no diretório
cd order-service

REM Criando arquivos na raiz
type nul > requirements.txt
type nul > Dockerfile
type nul > .env

REM Criando arquivos dentro do serviço
type nul > __init__.py
type nul > main.py
type nul > models.py
type nul > schemas.py
type nul > database.py
type nul > auth.py
type nul > routes.py

echo Estrutura de arquivos criada com sucesso!
pause
