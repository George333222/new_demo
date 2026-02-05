@echo off

REM Go to project root (folder of this bat file)
cd /d %~dp0

REM Create venv if it does not exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
python -m pip install -r requirements.txt

REM Run smoke tests
python -m pytest tests/ -m smoke --html=report.html --self-contained-html

pause
