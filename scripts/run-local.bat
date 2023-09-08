@echo off

:: Navigate to the base directory
cd /d %~dp0\..

:: Load environment variables from .env.local
for /f "tokens=1,* delims== eol=" %%a in ('type .env.local') do (
    set "%%a=%%b"
)

:: Run Django development server
python manage.py runserver