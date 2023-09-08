@echo off
cd /d %~dp0\..

:: Load http_proxy and https_proxy variables from .env.prod
for /f "tokens=1,2 delims==" %%a in ('findstr /r "^http_proxy=" .\.env.prod') do set "http_proxy=%%b"
for /f "tokens=1,2 delims==" %%a in ('findstr /r "^https_proxy=" .\.env.prod') do set "https_proxy=%%b"

:: Run Docker Compose
docker-compose -f docker-compose.prod.yml up -d --build