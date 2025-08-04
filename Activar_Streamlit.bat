@echo off
REM Activar entorno virtual
call .venv\Scripts\activate

REM Ejecutar Streamlit con el archivo app.py
streamlit run Data\app.py

pause
