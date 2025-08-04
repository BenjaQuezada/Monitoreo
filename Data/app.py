import streamlit as st
import pandas as pd
import os

# 📌 Ruta de la carpeta que contiene los CSV generados
CARPETA_CSV = r"E:\Monitoreo\Data\csv_files"  # Cambia esta ruta a la tuya

# 🔄 Actualización automática cada 5 segundos
st_autorefresh = st.experimental_rerun
st_autorefresh = st.autorefresh(interval=5000, key="data_refresh")

# Título
st.title("📡 Monitoreo en Tiempo Real desde CSV")

# Verificar si la carpeta existe
if os.path.exists(CARPETA_CSV):
    # Listar solo archivos CSV
    archivos_csv = [f for f in os.listdir(CARPETA_CSV) if f.lower().endswith(".csv")]

    if archivos_csv:
        # Selección de archivo
        archivo_seleccionado = st.selectbox("📑 Selecciona un archivo CSV:", archivos_csv)

        if archivo_seleccionado:
            ruta_csv = os.path.join(CARPETA_CSV, archivo_seleccionado)

            try:
                # Leer CSV
                df = pd.read_csv(ruta_csv)

                # Mostrar datos
                st.subheader(f"📊 Datos - {archivo_seleccionado}")
                st.dataframe(df)

                # Mostrar gráfico si hay columnas numéricas
                columnas_numericas = df.select_dtypes(include=['number'])
                if not columnas_numericas.empty:
                    st.subheader("📈 Gráfico de datos numéricos")
                    st.line_chart(columnas_numericas)
                else:
                    st.warning("⚠️ No hay columnas numéricas para graficar en este archivo.")
            except Exception as e:
                st.error(f"❌ Error al leer el archivo: {e}")
    else:
        st.warning("📂 No se encontraron archivos CSV en la carpeta.")
else:
    st.error(f"❌ La carpeta especificada no existe: {CARPETA_CSV}")
