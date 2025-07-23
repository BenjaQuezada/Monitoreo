@echo off
echo Creando entorno virtual...
python -m venv venv

echo Activando entorno virtual...
call venv\Scripts\activate

echo Instalando dependencias necesarias...
pip install --upgrade pip
pip install -r requirements.txt

echo Configuración completada.
echo Puedes ejecutar 'Ejecutar main.bat' o 'Ejecutar monitoreo.bat' según necesites.

pause
