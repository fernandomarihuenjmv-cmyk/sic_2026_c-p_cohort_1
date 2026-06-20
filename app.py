import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Dashboard Emprendimiento Chile",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>
.main{
    background-color:#f8f9fa;
}
.kpi{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
    text-align:center;
}
h1,h2,h3{
    color:#1f2937;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# CARGA
# --------------------------------------------------

@st.cache_data
def load_data():
    ruta_archivo = 'los-santos-en-la-corte/data/dataset_limpio.csv' 
    
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        primera_linea = f.readline()
        
    if primera_linea.startswith('<<<<<<< HEAD'):
        df = pd.read_csv(ruta_archivo, skiprows=1)
    else:
        df = pd.read_csv(ruta_archivo)
        
    # 1. Fuerza la conversión a números. 
    # errors='coerce' transforma cualquier texto (como "=======") en un valor nulo (NaN)
    df["ganancia_final"] = pd.to_numeric(df["ganancia_final"], errors='coerce')
    
    # 2. (Opcional pero recomendado) Elimina las filas corruptas que quedaron como nulas
    df = df.dropna(subset=["ganancia_final"])
    
    return df

df = load_data()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Filtros")

region = st.sidebar.multiselect("Región", sorted(df["region"].dropna().unique()), default=sorted(df["region"].dropna().unique()))
sexo = st.sidebar.multiselect("Sexo", sorted(df["sexo"].dropna().unique()), default=sorted(df["sexo"].dropna().unique()))
tramo = st.sidebar.multiselect("Tramo Etario", sorted(df["tramo_etario"].dropna().unique()), default=sorted(df["tramo_etario"].dropna().unique()))
rama = st.sidebar.multiselect("Rama Económica", sorted(df["rama_economica"].dropna().unique()), default=sorted(df["rama_economica"].dropna().unique()))
motivacion = st.sidebar.multiselect("Motivación", sorted(df["motivacion"].dropna().unique()), default=sorted(df["motivacion"].dropna().unique()))

df_f = df[
    (df["region"].isin(region)) &
    (df["sexo"].isin(sexo)) &
    (df["tramo_etario"].isin(tramo)) &
    (df["rama_economica"].isin(rama)) &
    (df["motivacion"].isin(motivacion))
]

# --------------------------------------------------
# TÍTULO
# --------------------------------------------------

st.title("📊 Emprendimiento en Chile")
st.subheader("¿Cómo influyen el sexo, la región y la rama económica en la informalidad, las ganancias y el acceso a financiamiento?")

# --------------------------------------------------
# KPIS
# --------------------------------------------------

total = len(df_f)

# Blindaje por si los filtros dejan el dataset vacío
if total > 0:
    informalidad = (df_f["informalidad"] == "Informal").mean() * 100
    ganancia_prom = df_f["ganancia_final"].mean()
    fondos = (df_f["financiamiento_inicial"] == "Subsidios públicos / Fondos del Estado").mean() * 100
    mujeres = (df_f["sexo"] == "Mujer").mean() * 100
    hombres = (df_f["sexo"] == "Hombre").mean() * 100
else:
    informalidad = ganancia_prom = fondos = mujeres = hombres = 0.0

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric("Emprendedores", f"{total:,}")
c2.metric("Tasa Informalidad", f"{informalidad:.1f}%")
c3.metric("Ganancia Promedio", f"${ganancia_prom:,.0f}")
c4.metric("% Fondos Públicos", f"{fondos:.1f}%")
c5.metric("% Mujeres", f"{mujeres:.1f}%")

# --------------------------------------------------
# PAGINAS
# --------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Resumen", "Informalidad", "Ganancias", "Financiamiento", "Insights"])

# ==================================================
# TAB 1
# ==================================================

with tab1:
    st.header("Resumen Ejecutivo")
    if not df_f.empty:
        fig = px.histogram(df_f, x="rama_economica", color="sexo", barmode="group")
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Ajusta los filtros para ver los datos.")

# ==================================================
# TAB 2
# ==================================================

with tab2:
    st.header("El Pilar de la Informalidad")
    if not df_f.empty:
        informalidad_sexo = df_f.groupby(["sexo","informalidad"]).size().reset_index(name="cantidad")
        fig1 = px.bar(informalidad_sexo, x="sexo", y="cantidad", color="informalidad", barmode="stack", title="Informalidad según Sexo")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Informalidad por Tramo Etario")
        edad_inf = df_f.groupby(["tramo_etario","informalidad"]).size().reset_index(name="cantidad")
        fig2 = px.bar(edad_inf, x="tramo_etario", y="cantidad", color="informalidad")
        st.plotly_chart(fig2, use_container_width=True)

        ranking = (
            df_f.assign(informal=lambda x: (x["informalidad"]=="Informal").astype(int))
            .groupby("region")["informal"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )
        ranking["informal"] *= 100

        st.subheader("Ranking Regiones Más Informales (%)")
        st.dataframe(ranking)

# ==================================================
# TAB 3
# ==================================================

with tab3:
    st.header("Brecha de Ganancias")
    if not df_f.empty:
        fig3 = px.histogram(df_f, x="tramos_ganancias", color="sexo", barmode="group")
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Distribución Ganancias")
        fig4 = px.box(df_f, x="sexo", y="ganancia_final", color="sexo")
        st.plotly_chart(fig4, use_container_width=True)

        heat = (
            df_f.groupby(["rama_economica","sexo"])["ganancia_final"]
            .mean()
            .reset_index()
            .pivot(index="rama_economica", columns="sexo", values="ganancia_final")
        )
        fig5 = px.imshow(heat, aspect="auto", title="Ingreso promedio")
        st.plotly_chart(fig5, use_container_width=True)

        hombres_avg = df_f[df_f["sexo"]=="Hombre"]["ganancia_final"].mean()
        mujeres_avg = df_f[df_f["sexo"]=="Mujer"]["ganancia_final"].mean()

        if pd.notna(hombres_avg) and hombres_avg > 0 and pd.notna(mujeres_avg):
            brecha = ((hombres_avg - mujeres_avg) / hombres_avg) * 100
            st.metric("Brecha de Ganancias", f"{brecha:.1f}%")
        else:
            st.metric("Brecha de Ganancias", "N/A")

# ==================================================
# TAB 4
# ==================================================

with tab4:
    st.header("Financiamiento y Motivación")
    if not df_f.empty:
        cruzado = pd.crosstab(df_f["motivacion"], df_f["financiamiento_inicial"])
        fig6 = px.bar(cruzado, barmode="stack")
        st.plotly_chart(fig6, use_container_width=True)

        pie = df_f["financiamiento_inicial"].value_counts().reset_index()
        fig7 = px.pie(pie, names="financiamiento_inicial", values="count")
        st.plotly_chart(fig7, use_container_width=True)

# ==================================================
# TAB 5
# ==================================================

with tab5:
    st.header("Hallazgos Automáticos")
    if not df_f.empty:
        ranking_tab5 = (
            df_f.assign(informal=lambda x: (x["informalidad"]=="Informal").astype(int))
            .groupby("region")["informal"].mean()
            .sort_values(ascending=False).reset_index()
        )
        region_vulnerable = ranking_tab5.iloc[0]["region"] if not ranking_tab5.empty else "N/A"

        sector_infl = (
            df_f.assign(informal=(df_f["informalidad"]=="Informal").astype(int))
            .groupby("rama_economica")["informal"].mean()
            .sort_values(ascending=False)
        )
        sector_informal = sector_infl.index[0] if not sector_infl.empty else "N/A"

        menor_fin_group = (
            df_f[df_f["financiamiento_inicial"] == "Subsidios públicos / Fondos del Estado"]
            .groupby("sexo").size()
        )
        menor_financiamiento = menor_fin_group.idxmin() if not menor_fin_group.empty else "N/A"

        st.success(f"Región más vulnerable: {region_vulnerable}")
        st.warning(f"Sector con mayor informalidad: {sector_informal}")
        st.info(f"Grupo con menor acceso a subsidios: {menor_financiamiento}")

        st.markdown("""
        ### Recomendaciones
        - Incrementar cobertura de subsidios en grupos vulnerables.
        - Potenciar programas de formalización.
        - Reducir brechas de género.
        - Capacitación financiera para emprendedores.
        """)
    else:
        st.warning("Selecciona al menos un valor en los filtros para generar hallazgos automáticos.")