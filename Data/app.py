import streamlit as st
import pandas as pd
import os

# 📌 Ruta fija de la carpeta donde se encuentran los archivos
CARPETA_ARCHIVOS = r"E:\Monitoreo"

# 🔄 Recarga automática cada 5 segundos
st_autorefresh = st.autorefresh(interval=5000, key="data_refresh")

# Título de la app
st.title("📡 Monitoreo en Tiempo Real desde Carpeta Fija")

# Verificar si la carpeta existe
if os.path.exists(CARPETA_ARCHIVOS):
    # Filtrar solo archivos Excel y CSV
    archivos = [f for f in os.listdir(CARPETA_ARCHIVOS) if f.lower().endswith((".xlsx", ".xls", ".csv"))]

    if archivos:
        # Seleccionar archivo
        archivo_seleccionado = st.selectbox("📑 Selecciona un archivo:", archivos)

        if archivo_seleccionado:
            ruta_archivo = os.path.join(CARPETA_ARCHIVOS, archivo_seleccionado)

            try:
                # Leer según formato
                if archivo_seleccionado.lower().endswith((".xlsx", ".xls")):
                    df = pd.read_excel(ruta_archivo)
                else:
                    df = pd.read_csv(ruta_archivo)

                # Mostrar datos
                st.subheader(f"📊 Datos - {archivo_seleccionado}")
                st.dataframe(df)

                # Mostrar gráfico si hay datos numéricos
                columnas_numericas = df.select_dtypes(include=['number'])
                if not columnas_numericas.empty:
                    st.subheader("📈 Gráfico de datos numéricos")
                    st.line_chart(columnas_numericas)
                else:
                    st.warning("⚠️ No hay columnas numéricas para graficar en este archivo.")
            except Exception as e:
                st.error(f"❌ Error al leer el archivo: {e}")
    else:
        st.warning("📂 No se encontraron archivos Excel o CSV en la carpeta.")
else:
    st.error(f"❌ La carpeta especificada no existe: {CARPETA_ARCHIVOS}")
