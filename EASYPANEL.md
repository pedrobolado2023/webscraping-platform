# Configuração para EasyPanel - Monorepo

## ⚠️ IMPORTANTE: Configuração de Monorepo

Este projeto usa uma estrutura de monorepo (múltiplos serviços em um repositório). No EasyPanel, você precisa criar **serviços separados** para cada parte.

## Deployment no EasyPanel

### 1. Preparação do Repositório GitHub

✅ **Já feito** - Código está em: `https://github.com/pedrobolado2023/webscraping-platform`

### 2. Configuração no EasyPanel

#### **Ordem de Deploy (IMPORTANTE):**

### **1º - PostgreSQL Database**
- **Template**: PostgreSQL
- **Nome**: `webscraping-db`
- **Database**: `webscraping`
- **Username**: `postgres`
- **Password**: `[gere uma senha segura]`
- **Port**: 5432

### **2º - Redis Cache**
- **Template**: Redis
- **Nome**: `webscraping-redis`
- **Port**: 6379

### **3º - Backend API**
- **Tipo**: App from Source
- **Source**: GitHub Repository
- **Repository**: `pedrobolado2023/webscraping-platform`
- **Branch**: `main`
- **Root Directory**: `backend/` ⚠️ **CRÍTICO**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- **Port**: 8000
- **Build Provider**: Nixpacks (detectará Python automaticamente)

**Variáveis de Ambiente do Backend:**
```
DATABASE_URL=postgresql://postgres:[SUA_SENHA]@[DB_HOST]:5432/webscraping
REDIS_URL=redis://[REDIS_HOST]:6379/0
SECRET_KEY=[GERE_UMA_CHAVE_SEGURA_ALEATORIA]
FRONTEND_URL=https://[SEU_FRONTEND_DOMAIN]
```

### **4º - Worker**
- **Tipo**: App from Source
- **Source**: GitHub Repository  
- **Repository**: `pedrobolado2023/webscraping-platform`
- **Branch**: `main`
- **Root Directory**: `worker/` ⚠️ **CRÍTICO**
- **Build Command**: `pip install -r requirements.txt && playwright install chromium --with-deps`
- **Start Command**: `python worker.py`
- **Build Provider**: Nixpacks

**Variáveis de Ambiente do Worker:**
```
DATABASE_URL=postgresql://postgres:[SUA_SENHA]@[DB_HOST]:5432/webscraping
REDIS_URL=redis://[REDIS_HOST]:6379/0
```

### **5º - Frontend**
- **Tipo**: App from Source
- **Source**: GitHub Repository
- **Repository**: `pedrobolado2023/webscraping-platform`
- **Branch**: `main`
- **Root Directory**: `frontend/` ⚠️ **CRÍTICO**
- **Build Command**: `npm install && npm run build`
- **Start Command**: `npm run preview -- --host 0.0.0.0 --port 3000`
- **Port**: 3000
- **Build Provider**: Nixpacks (detectará Node.js automaticamente)

**Variáveis de Ambiente do Frontend:**
```
VITE_API_URL=https://[SEU_BACKEND_DOMAIN]
```

## 3. Configurações Especiais para Monorepo

### **Root Directory é OBRIGATÓRIO**
Para cada serviço no EasyPanel, você DEVE especificar:
- Backend: `Root Directory = backend/`
- Frontend: `Root Directory = frontend/`  
- Worker: `Root Directory = worker/`

### **Arquivos de Configuração Criados**
Cada serviço agora tem:
- `nixpacks.toml` - Configuração Nixpacks
- `Procfile` - Comandos de execução
- `runtime.txt` - Versão do Python (backend/worker)

## 4. URLs e Conexões

Após o deploy, você terá:
- **Database**: URL interna do PostgreSQL
- **Redis**: URL interna do Redis
- **Backend**: `https://[seu-backend].easypanel.host`
- **Worker**: Executa em background (sem URL pública)
- **Frontend**: `https://[seu-frontend].easypanel.host`

## 5. Testando o Deploy

1. **Teste o Backend**: `https://[backend-url]/health`
2. **Teste o Frontend**: Abra a URL e tente fazer login
3. **Verifique os Logs**: No painel do EasyPanel

## 6. Troubleshooting

### **Erro "Nixpacks unable to generate build plan"**
✅ **Resolvido** - Adicionados arquivos de configuração específicos

### **Erro de CORS**
- Adicione a URL do frontend em `FRONTEND_URL` no backend

### **Worker não processa jobs**
- Verifique conexão Redis
- Verifique logs do worker

### **Frontend não carrega**
- Verifique `VITE_API_URL`
- Teste conexão com backend