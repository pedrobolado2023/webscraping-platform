#!/bin/bash

# Webscraping Platform - Quick Setup Script

echo "🚀 Configurando Webscraping Platform para GitHub/EasyPanel..."

# Verificar se Git está instalado
if ! command -v git &> /dev/null; then
    echo "❌ Git não encontrado. Instale o Git primeiro."
    exit 1
fi

# Inicializar repositório Git se não existir
if [ ! -d ".git" ]; then
    echo "📁 Inicializando repositório Git..."
    git init
fi

# Adicionar todos os arquivos
echo "📋 Adicionando arquivos ao Git..."
git add .

# Fazer commit inicial
echo "💾 Fazendo commit inicial..."
git commit -m "feat: initial commit - webscraping platform

- Backend FastAPI with JWT authentication
- Frontend React + Vite + Tailwind
- Worker with Playwright scraping engine
- Docker Compose setup
- PostgreSQL + Redis infrastructure
- Complete job management system
- Dashboard with results visualization

Ready for deployment on EasyPanel"

echo "✅ Projeto preparado para GitHub!"
echo ""
echo "📝 Próximos passos:"
echo "1. Crie um repositório no GitHub"
echo "2. Execute: git remote add origin https://github.com/seu-usuario/webscraping-platform.git"
echo "3. Execute: git push -u origin main"
echo "4. Siga as instruções em EASYPANEL.md para deploy"
echo ""
echo "📖 Documentação disponível em:"
echo "- README.md - Visão geral do projeto"
echo "- SETUP.md - Setup para desenvolvimento local"
echo "- EASYPANEL.md - Instruções para deploy no EasyPanel"