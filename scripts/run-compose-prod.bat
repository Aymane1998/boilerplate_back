@echo off
cd /d %~dp0\..

:: Run Docker Compose
docker compose -f docker-compose.prod.yml up -d --build