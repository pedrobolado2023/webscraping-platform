# Configuração de Desenvolvimento Local

## Pré-requisitos
- Docker e Docker Compose
- Node.js 18+ (para desenvolvimento local do frontend)
- Python 3.11+ (para desenvolvimento local do backend/worker)

## Setup Rápido

### 1. Clone e Configure
```bash
git clone <repo-url>
cd webscraping-platform
```

### 2. Configure Variáveis de Ambiente
```bash
# Backend
cp backend/.env.example backend/.env

# Frontend  
cp frontend/.env.example frontend/.env

# Worker
cp worker/.env.example worker/.env
```

### 3. Inicie com Docker Compose
```bash
docker-compose up --build
```

### 4. Acesse a Aplicação
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Desenvolvimento Local

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend (React)
```bash
cd frontend
npm install
npm run dev
```

### Worker (Playwright)
```bash
cd worker
pip install -r requirements.txt
playwright install chromium
python worker.py
```

## Primeiros Passos

1. **Registre um usuário** via frontend ou API
2. **Crie um job** simples para testar (use o exemplo em `backend/examples/jobs_seed.json`)
3. **Execute o job** e veja os resultados no dashboard

## Estrutura do Banco de Dados

O PostgreSQL será inicializado automaticamente com as tabelas:
- `users` - Usuários da plataforma
- `jobs` - Jobs de scraping configurados
- `job_results` - Resultados das execuções

## Troubleshooting

### Problemas Comuns

1. **Porta já em uso**: Modifique as portas no `docker-compose.yml`
2. **Problemas de permissão**: Verifique permissões do Docker
3. **Dependências faltando**: Execute `docker-compose build --no-cache`

### Logs
```bash
# Ver logs de todos os serviços
docker-compose logs -f

# Ver logs de um serviço específico
docker-compose logs -f backend
```

## Segurança

⚠️ **IMPORTANTE**: 
- Altere `SECRET_KEY` no backend para produção
- Use credenciais seguras para PostgreSQL
- Não commite arquivos `.env` com dados reais

## Legal e Ética

Este projeto é para uso educacional e legítimo. Respeite:
- Termos de serviço dos sites alvo
- Rate limits e robots.txt
- Leis de privacidade e proteção de dados
- Não use para contornar medidas de segurança