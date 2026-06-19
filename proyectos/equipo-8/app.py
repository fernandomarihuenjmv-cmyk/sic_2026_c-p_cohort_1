import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Fashion Boutique", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('data/dataset_limpio.csv')

try:
    df = load_data()
except FileNotFoundError:
    st.error("No se encuentra el archivo dataset_limpio.csv. Ejecuta el notebook de limpieza primero.")
    st.stop()

st.title("👗 Análisis de Ventas: Fashion Boutique 2025")
st.markdown("""
**Pregunta de análisis:** ¿Qué categorías de prendas tienen mejor rendimiento de ventas según los descuentos aplicados?

**Hallazgo principal:** Las categorías con descuentos moderados mantienen un mayor volumen de ventas sin sacrificar drásticamente los ingresos totales.
""")

st.sidebar.header("Filtros Interactivos")

# Filtro 1: Categoría
categoria_seleccionada = st.sidebar.multiselect(
    "1. Categoría", 
    df['category'].unique(), 
    default=df['category'].unique()
)

# Filtro 2: Rango de descuento (markdown_percentage)
min_desc, max_desc = float(df['markdown_percentage'].min()), float(df['markdown_percentage'].max())
rango_descuento = st.sidebar.slider(
    "2. Porcentaje de Descuento (%)",
    min_value=min_desc, max_value=max_desc, value=(min_desc, max_desc)
)

# Filtrado dinámico
df_filtrado = df[
    (df['category'].isin(categoria_seleccionada)) & 
    (df['markdown_percentage'] >= rango_descuento[0]) & 
    (df['markdown_percentage'] <= rango_descuento[1])
]

st.subheader("Indicadores de Rendimiento")
col1, col2, col3 = st.columns(3)
col1.metric("Transacciones Totales", len(df_filtrado))
col2.metric("Ingresos (Ventas)", f"${df_filtrado['current_price'].sum():,.2f}") 
col3.metric("Descuento Promedio", f"{df_filtrado['markdown_percentage'].mean():.2f}%") 

st.divider()

col_graf1, col_graf2 = st.columns(2)
with col_graf1:
    st.subheader("Ingresos por Categoría")
    df_agrupado = df_filtrado.groupby('category')['current_price'].sum().reset_index()
    fig_bar = px.bar(df_agrupado, x='category', y='current_price', color='category')
    st.plotly_chart(fig_bar, use_container_width=True)

with col_graf2:
    st.subheader("Distribución de Tallas")
    fig_pie = px.pie(df_filtrado, names='size', values='current_price', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)