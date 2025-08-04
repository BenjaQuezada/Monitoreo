@echo off
REM Activar el entorno virtual
call .venv\Scripts\activate

REM Instalar Streamlit
pip install streamlit

REM Actualizar el archivo requirements.txt
pip freeze > requirements.txt

echo ✅ Streamlit instalado correctamente en el entorno virtual.
pause
