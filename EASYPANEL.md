# Configuração para EasyPanel - Monorepo

## ⚠️ SOLUÇÃO: Usar Variável SERVICE_TYPE

Como o EasyPanel não suporta Root Directory, criei uma configuração que usa a variável de ambiente `SERVICE_TYPE` para determinar qual serviço executar.

## Deployment no EasyPanel

### **ORDEM DE IMPLANTAÇÃO:**

### **1º - PostgreSQL Database**
- **Template**: PostgreSQL
- **Nome**: `webscraping-db`
- **Database**: `webscraping`
- **Username**: `postgres`
- **Password**: `[gere uma senha segura]`

### **2º - Redis Cache**
- **Template**: Redis
- **Nome**: `webscraping-redis`

### **3º - Backend API**
- **Tipo**: App from Source
- **Repository**: `pedrobolado2023/webscraping-platform`
- **Branch**: `main`
- **Build Provider**: Nixpacks (detectará Python/Node.js automaticamente)

**⚠️ IMPORTANTE: Use exatamente estas variáveis de ambiente:**
```
SERVICE_TYPE=backend
DATABASE_URL=postgresql://postgres:[SUA_SENHA]@[DB_HOST]:5432/webscraping
REDIS_URL=redis://[REDIS_HOST]:6379/0
SECRET_KEY=[GERE_UMA_CHAVE_SEGURA]
ALGORITHM=HS256
FRONTEND_URL=https://[SEU_FRONTEND_DOMAIN]
```

### **4º - Worker**
- **Tipo**: App from Source
- **Repository**: `pedrobolado2023/webscraping-platform`
- **Branch**: `main`
- **Build Provider**: Nixpacks

**Variáveis de Ambiente:**
```
SERVICE_TYPE=worker
DATABASE_URL=postgresql://postgres:[SUA_SENHA]@[DB_HOST]:5432/webscraping
REDIS_URL=redis://[REDIS_HOST]:6379/0
```

### **5º - Frontend**
- **Tipo**: App from Source
- **Repository**: `pedrobolado2023/webscraping-platform`
- **Branch**: `main`
- **Build Provider**: Nixpacks

**Variáveis de Ambiente:**
```
SERVICE_TYPE=frontend
VITE_API_URL=https://[SEU_BACKEND_DOMAIN]
```

## 🔧 Como Funciona

O arquivo `nixpacks.toml` na raiz detecta a variável `SERVICE_TYPE` e:
- `SERVICE_TYPE=backend` → Executa o backend FastAPI
- `SERVICE_TYPE=worker` → Executa o worker Playwright  
- `SERVICE_TYPE=frontend` → Executa o frontend React

## ⚠️ IMPORTANTE

**Para cada serviço no EasyPanel, você DEVE configurar a variável `SERVICE_TYPE` corretamente:**
- Backend: `SERVICE_TYPE=backend`
- Worker: `SERVICE_TYPE=worker`
- Frontend: `SERVICE_TYPE=frontend`

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

### **Erro 502 (Bad Gateway)**
**Possíveis causas:**
- **SERVICE_TYPE não definido** - Verifique se a variável está configurada
- **Variáveis de ambiente faltando** - Consulte `.env.example`
- **Backend não iniciou** - Verifique DATABASE_URL e REDIS_URL
- **Frontend não construiu** - Verifique se npm build executou corretamente

**Como diagnosticar:**
1. Verifique os logs do serviço no EasyPanel
2. Teste o endpoint `/health` do backend
3. Confirme se `SERVICE_TYPE` está definido corretamente
4. Verifique se todas as URLs de dependências estão corretas

### **Erro de CORS**
- Adicione a URL do frontend em `FRONTEND_URL` no backend
- Exemplo: `FRONTEND_URL=https://seu-frontend.easypanel.host`

### **Worker não processa jobs**
- Verifique conexão Redis com `REDIS_URL`
- Verifique logs do worker no EasyPanel
- Confirme se `SERVICE_TYPE=worker` está definido

### **Frontend não conecta ao backend**
- Verifique se `VITE_API_URL` aponta para o backend correto
- Exemplo: `VITE_API_URL=https://seu-backend.easypanel.host`

**📋 Checklist para deploy com erro 502:**
- [ ] DATABASE_URL configurado corretamente
- [ ] REDIS_URL configurado corretamente  
- [ ] SERVICE_TYPE definido (backend/worker/frontend)
- [ ] FRONTEND_URL no backend aponta para frontend
- [ ] VITE_API_URL no frontend aponta para backend
- [ ] SECRET_KEY definido no backend
- [ ] Logs do serviço verificados no EasyPanel

### **Frontend não carrega**
- Verifique `VITE_API_URL`
- Teste conexão com backend