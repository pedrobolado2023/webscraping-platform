# Configuração para EasyPanel

## Deployment no EasyPanel

### 1. Preparação do Repositório GitHub

1. **Crie um repositório no GitHub** e faça push do código:
```bash
git init
git add .
git commit -m "Initial commit - Webscraping Platform"
git remote add origin https://github.com/seu-usuario/webscraping-platform.git
git push -u origin main
```

### 2. Configuração no EasyPanel

#### Serviços Necessários:

1. **PostgreSQL Database**
   - Template: PostgreSQL
   - Database: `webscraping`
   - Username: `postgres`
   - Password: `[gerar senha segura]`

2. **Redis Cache**
   - Template: Redis
   - Configuração padrão

3. **Backend API**
   - Source: GitHub Repository
   - Build Pack: Python
   - Port: 8000
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
   - Working Directory: `backend/`

4. **Worker**
   - Source: GitHub Repository
   - Build Pack: Python
   - Build Command: `pip install -r requirements.txt && playwright install chromium`
   - Start Command: `python worker.py`
   - Working Directory: `worker/`

5. **Frontend**
   - Source: GitHub Repository
   - Build Pack: Node.js
   - Port: 3000
   - Build Command: `npm install && npm run build`
   - Start Command: `npm run preview -- --host 0.0.0.0 --port 3000`
   - Working Directory: `frontend/`

### 3. Variáveis de Ambiente

#### Backend:
```
DATABASE_URL=postgresql://postgres:[password]@[db-host]:5432/webscraping
REDIS_URL=redis://[redis-host]:6379/0
SECRET_KEY=[gerar chave segura]
```

#### Frontend:
```
VITE_API_URL=https://[seu-backend-url]
```

#### Worker:
```
DATABASE_URL=postgresql://postgres:[password]@[db-host]:5432/webscraping
REDIS_URL=redis://[redis-host]:6379/0
```

### 4. Ordem de Deploy

1. PostgreSQL Database
2. Redis Cache
3. Backend API (aguardar estar funcionando)
4. Worker (aguardar backend estar funcionando)
5. Frontend (configurar VITE_API_URL com URL do backend)

### 5. Configurações Especiais

#### Backend (app.main.py):
- Adicionar o domínio do EasyPanel em `allow_origins`

#### Worker:
- Certificar que o Playwright está configurado para headless
- Verificar se as dependências do sistema estão instaladas

### 6. Monitoramento

- Verificar logs de cada serviço no EasyPanel
- Testar endpoints: `https://[backend-url]/health`
- Testar frontend: `https://[frontend-url]`

### 7. Troubleshooting

- **Erro de conexão DB**: Verificar DATABASE_URL
- **Worker não processa jobs**: Verificar conexão Redis
- **Frontend não conecta**: Verificar VITE_API_URL
- **CORS errors**: Adicionar domínio frontend em backend CORS