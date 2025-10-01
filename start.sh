# Escolha o serviço a ser executado via variável de ambiente
SERVICE_TYPE=${SERVICE_TYPE:-backend}

if [ "$SERVICE_TYPE" = "backend" ]; then
    cd backend
    pip install -r requirements.txt
    uvicorn app.main:app --host 0.0.0.0 --port 8000
elif [ "$SERVICE_TYPE" = "worker" ]; then
    cd worker
    pip install -r requirements.txt
    playwright install chromium --with-deps
    python worker.py
elif [ "$SERVICE_TYPE" = "frontend" ]; then
    cd frontend
    npm install
    npm run build
    npm run preview -- --host 0.0.0.0 --port 3000
else
    echo "SERVICE_TYPE deve ser: backend, worker ou frontend"
    exit 1
fi