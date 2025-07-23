Programa para monitorear pantallas y guardar su contenido en un archivo .csv

Autor: Benjamín Ignacio Quezada Paredes. 2025.

Librerías utilizadas:
- ultralytics
- opencv-python (cv2)
- time
- csv
- os

Instrucciones de uso:

Requisitos previos:
- Tener Python instalado (preferentemente versión 3.10 o 3.11)
- Hacer doble clic en `Setup.bat` antes de ejecutar cualquier otro archivo.
  Este script instalará automáticamente todas las dependencias necesarias.

---

Aviso:
Este proyecto ya incluye un modelo YOLOv8 previamente entrenado, ubicado en la ruta:
  Data\runs\detect\
  
Por lo tanto, puede ejecutarse directamente el archivo: `TEMP_REGISTER.py`

Si desea entrenar el modelo desde cero, siga las instrucciones a continuación:

---

Entrenar el modelo desde cero:

NOTA: si se entrena un modelo mientras el actual tenga el mismo nombre, se creará una variación de este nombre y no se ejecutará.
      Se aconseja cambiar el nombre de la carpeta Data\runs\detect\7SD&1 , para evitar mayores problemas.

1️. Ejecutar el archivo: `Ejecutar main.bat`
   - Esto iniciará el proceso de entrenamiento usando el dataset ubicado en `Data\7SG&1`
   - El modelo se entrenará con 50 epochs y las clases del 0 al 9, más: "-", ".", "screen"

2️. Validar el modelo entrenado
   - Al finalizar el entrenamiento, verifique que se haya generado correctamente el archivo:
     `Data\runs\detect\7SG&1\weights\best.pt`

3️. Ejecutar el archivo: `Ejecutar monitoreo.bat`
   - Este script abrirá la cámara del sistema.
   - Detectará los números en pantalla y almacenará los valores en un archivo `.txt`
     con nombre del tipo: `templog_(fecha_hora).txt`

