import streamlit as st
import pandas as pd
import os

# Configuración de la app
st.title("Monitoreo desde Carpeta de Excels")

# Selector de carpeta
carpeta = st.text_input("📂 Ruta de la carpeta con archivos Excel:")

if carpeta and os.path.isdir(carpeta):
    # Listar solo archivos Excel en la carpeta
    archivos_excel = [f for f in os.listdir(carpeta) if f.lower().endswith((".xlsx", ".xls"))]

    if archivos_excel:
        # Selección de archivo
        archivo_seleccionado = st.selectbox("📑 Selecciona un archivo Excel:", archivos_excel)

        if archivo_seleccionado:
            ruta_archivo = os.path.join(carpeta, archivo_seleccionado)

            try:
                # Leer el archivo Excel y mostrar hojas
                excel_file = pd.ExcelFile(ruta_archivo)
                hoja_seleccionada = st.selectbox("📄 Selecciona una hoja:", excel_file.sheet_names)

                # Leer la hoja seleccionada
                df = pd.read_excel(ruta_archivo, sheet_name=hoja_seleccionada)

                # Mostrar datos
                st.subheader(f"📊 Datos - {archivo_seleccionado} ({hoja_seleccionada})")
                st.dataframe(df)

                # Mostrar gráfico si hay datos numéricos
                columnas_numericas = df.select_dtypes(include=['number'])
                if not columnas_numericas.empty:
                    st.subheader("📈 Gráfico de datos numéricos")
                    st.line_chart(columnas_numericas)
                else:
                    st.warning("No hay columnas numéricas para graficar en esta hoja.")
            except Exception as e:
                st.error(f"Error al leer el archivo: {e}")
    else:
        st.warning("No se encontraron archivos Excel en la carpeta seleccionada.")
else:
    st.info("Por favor, ingresa una ruta válida de carpeta.")
