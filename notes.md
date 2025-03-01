uvicorn core.asgi:application --host 0.0.0.0 --port 8000 --workers 4 --log-level debug --reload
docker-compose up -d --build

<!-- 
wsl sh
wsl ./entrypoint.sh
wsl sh ./entrypoint.sh 
-->