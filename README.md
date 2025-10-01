# Webscraping Platform

Uma plataforma completa para web scraping com autenticação, gestão de jobs, execução assíncrona e dashboard de resultados.

## 🚀 Funcionalidades

### ✅ Autenticação e Segurança
- Sistema de login/registro com JWT
- Credenciais criptografadas para sites alvo
- Rate limiting e logs de auditoria

### ✅ Gestão de Jobs
- CRUD completo de jobs de scraping
- Suporte a múltiplos métodos de autenticação (formulário, OAuth, cookies)
- Scripts personalizados de navegação e extração
- Agendamento simples (manual, diário, por hora)

### ✅ Engine de Scraping
- Baseado em Playwright (suporte completo a JavaScript)
- Sessões autenticadas em sites alvo
- Extração automática ou com scripts customizados
- Screenshots e logs detalhados

### ✅ Dashboard e Resultados
- Interface responsiva com React + Tailwind
- Histórico de execuções com status e tempos
- Visualização detalhada de dados extraídos
- Export de resultados em JSON

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │     Worker      │
│   React+Vite    │◄──►│    FastAPI      │◄──►│   Playwright    │
│   Tailwind CSS  │    │   PostgreSQL    │    │     Redis       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Serviços
- **Frontend**: SPA React com Vite e Tailwind CSS
- **Backend**: API REST FastAPI com autenticação JWT
- **Worker**: Engine assíncrona de scraping com Playwright
- **Database**: PostgreSQL para persistência
- **Queue**: Redis para fila de jobs

## 🛠️ Setup Rápido

```bash
# 1. Clone o repositório
git clone <repo-url>
cd webscraping-platform

# 2. Configure variáveis de ambiente
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
cp worker/.env.example worker/.env

# 3. Inicie com Docker Compose
docker-compose up --build

# 4. Acesse a aplicação
# Frontend: http://localhost:3000
# API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## 📚 Documentação

- [Setup Detalhado](./SETUP.md)
- [Backend README](./backend/README.md)
- [Frontend README](./frontend/README.md)
- [Worker README](./worker/README.md)

## 🔧 Exemplo de Job

```json
{
  "name": "Exemplo Básico",
  "url": "https://httpbin.org/html",
  "login_method": "none",
  "script": "return { title: document.title, paragraphs: Array.from(document.querySelectorAll('p')).map(p => p.textContent) };"
}
```

## 🛡️ Segurança e Legalidade

### ⚠️ Avisos Importantes
- **Use apenas para sites onde você tem permissão**
- **Respeite robots.txt e termos de serviço**
- **Não contorne medidas de segurança (MFA, CAPTCHA)**
- **Implemente rate limiting apropriado**

### 🔒 Práticas de Segurança
- Credenciais criptografadas at-rest
- Autenticação JWT com expiração
- Logs de auditoria completos
- Isolamento com Docker

## 🚦 Status do Projeto

- ✅ Estrutura base criada
- ✅ Backend API implementado
- ✅ Frontend com componentes essenciais
- ✅ Worker de scraping funcional
- ✅ Docker Compose configurado
- 🔄 Pronto para desenvolvimento e testes

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é para fins educacionais. Use de forma responsável e ética.

## 📞 Suporte

Para issues ou dúvidas, abra uma issue no GitHub.
