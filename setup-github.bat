@echo off
REM Webscraping Platform - Quick Setup Script for Windows

echo 🚀 Configurando Webscraping Platform para GitHub/EasyPanel...

REM Verificar se Git está instalado
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git não encontrado. Instale o Git primeiro.
    pause
    exit /b 1
)

REM Inicializar repositório Git se não existir
if not exist ".git" (
    echo 📁 Inicializando repositório Git...
    git init
)

REM Adicionar todos os arquivos
echo 📋 Adicionando arquivos ao Git...
git add .

REM Fazer commit inicial
echo 💾 Fazendo commit inicial...
git commit -m "feat: initial commit - webscraping platform - Backend FastAPI with JWT authentication - Frontend React + Vite + Tailwind - Worker with Playwright scraping engine - Docker Compose setup - PostgreSQL + Redis infrastructure - Complete job management system - Dashboard with results visualization Ready for deployment on EasyPanel"

echo ✅ Projeto preparado para GitHub!
echo.
echo 📝 Próximos passos:
echo 1. Crie um repositório no GitHub
echo 2. Execute: git remote add origin https://github.com/seu-usuario/webscraping-platform.git
echo 3. Execute: git push -u origin main
echo 4. Siga as instruções em EASYPANEL.md para deploy
echo.
echo 📖 Documentação disponível em:
echo - README.md - Visão geral do projeto
echo - SETUP.md - Setup para desenvolvimento local
echo - EASYPANEL.md - Instruções para deploy no EasyPanel

pause