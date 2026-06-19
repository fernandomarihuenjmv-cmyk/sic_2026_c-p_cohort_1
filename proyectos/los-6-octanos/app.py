"""
app.py — Dashboard de Precios de Combustibles en Chile
Datos en vivo de la Comisión Nacional de Energía (https://api.cne.cl).

Ejecutar:
    pip install -r requirements.txt
    streamlit run app.py

Credenciales: ver README (archivo .streamlit/secrets.toml).
"""

import os
import requests
import pandas as pd
import plotly.express as px
import streamlit as st
from google import genai
from google.genai import types

# --------------------------------------------------------------------------
# Configuración
# --------------------------------------------------------------------------
BASE = "https://api.cne.cl"
LOGIN_URL = f"{BASE}/api/login"
ESTACIONES_URL = f"{BASE}/api/v4/estaciones"

# Nombre amigable -> código del combustible en la API
COMBUSTIBLES = {
    "Gasolina 93": "93",
    "Gasolina 95": "95",
    "Gasolina 97": "97",
    "Diésel": "DI",
    "GLP vehicular": "GLP",
    "GNC": "GNC",
    "Kerosene": "KE",
}

st.set_page_config(
    page_title="Precios de Combustibles · Chile",
    page_icon="⛽",
    layout="wide",
)


# --------------------------------------------------------------------------
# Credenciales (desde secrets de Streamlit o variables de entorno)
# --------------------------------------------------------------------------
def obtener_credenciales():
    try:
        return st.secrets["CNE_EMAIL"], st.secrets["CNE_PASSWORD"]
    except Exception:
        return os.environ.get("CNE_EMAIL"), os.environ.get("CNE_PASSWORD")


# --------------------------------------------------------------------------
# Carga de datos (con caché: no vuelve a llamar a la API en cada clic)
# --------------------------------------------------------------------------
def _login(email, password):
    r = requests.post(LOGIN_URL, data={"email": email, "password": password}, timeout=30)
    r.raise_for_status()
    datos = r.json()
    for k in ("token", "access_token", "jwt"):
        if isinstance(datos, dict):
            if k in datos:
                return datos[k]
            if isinstance(datos.get("data"), dict) and k in datos["data"]:
                return datos["data"][k]
    raise RuntimeError("No se pudo obtener el token desde /api/login.")


def _col(df, c):
    """Devuelve la columna si existe; si no, una columna de NA del mismo largo."""
    return df[c] if c in df.columns else pd.Series([pd.NA] * len(df), index=df.index)


@st.cache_data(ttl=1800, show_spinner="Cargando estaciones desde la CNE…")
def cargar_datos(email, password):
    token = _login(email, password)
    r = requests.get(ESTACIONES_URL, headers={"Authorization": f"Bearer {token}"}, timeout=120)
    r.raise_for_status()
    payload = r.json()
    lista = payload["data"] if isinstance(payload, dict) and "data" in payload else payload

    df = pd.json_normalize(lista)

    out = pd.DataFrame(index=df.index)
    out["marca"] = _col(df, "distribuidor.marca")
    out["region"] = _col(df, "ubicacion.nombre_region")
    out["comuna"] = _col(df, "ubicacion.nombre_comuna")
    out["direccion"] = _col(df, "ubicacion.direccion")
    out["lat"] = pd.to_numeric(_col(df, "ubicacion.latitud"), errors="coerce")
    out["lon"] = pd.to_numeric(_col(df, "ubicacion.longitud"), errors="coerce")

    for nombre, code in COMBUSTIBLES.items():
        out[nombre] = pd.to_numeric(_col(df, f"precios.{code}.precio"), errors="coerce")
        out[f"_fecha_{nombre}"] = _col(df, f"precios.{code}.fecha_actualizacion")

    # Dejar solo coordenadas válidas dentro del territorio chileno
    out = out[out["lat"].between(-56, -17) & out["lon"].between(-110, -66)]
    return out.reset_index(drop=True)


def fig_mapa(d, combustible):
    """Mapa de estaciones coloreado por precio. Compatible con plotly nuevo y antiguo."""
    kwargs = dict(
        lat="lat", lon="lon", color=combustible, hover_name="marca",
        hover_data={"comuna": True, "direccion": True,
                    combustible: ":$,.0f", "lat": False, "lon": False},
        color_continuous_scale="RdYlGn_r", zoom=3, height=600,
    )
    if hasattr(px, "scatter_map"):          # plotly >= 5.24 (MapLibre)
        fig = px.scatter_map(d, map_style="open-street-map", **kwargs)
    else:                                   # plotly antiguo (Mapbox)
        fig = px.scatter_mapbox(d, **kwargs)
        fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), coloraxis_colorbar_title="Precio")
    return fig


def pesos(x):
    """Formatea un número como pesos chilenos: 1234567 -> $1.234.567"""
    return f"${x:,.0f}".replace(",", ".")


# --------------------------------------------------------------------------
# Interfaz
# --------------------------------------------------------------------------
st.title("⛽ Precios de Combustibles en Chile")
st.caption("Datos en vivo de la Comisión Nacional de Energía · api.cne.cl")
                    
email, password = obtener_credenciales()
if not email or not password:
    st.error(
        "Faltan las credenciales. Crea el archivo `.streamlit/secrets.toml` con:\n\n"
        '```\nCNE_EMAIL = "tu_correo"\nCNE_PASSWORD = "tu_clave"\n```'
    )
    st.stop()

try:
    df = cargar_datos(email, password)
except Exception as e:
    st.error(f"No se pudieron cargar los datos: {e}")
    st.stop()

# ---- Filtros (barra lateral) ----
st.sidebar.header("Filtros")
combustible = st.sidebar.selectbox("Combustible", list(COMBUSTIBLES.keys()))
regiones = sorted(df["region"].dropna().unique())
sel_regiones = st.sidebar.multiselect("Región", regiones, default=regiones)

d = df[df["region"].isin(sel_regiones)].dropna(subset=[combustible]).copy()

if d.empty:
    st.warning("No hay estaciones con ese combustible en la selección.")
    st.stop()

# ---- Fecha de actualización ----
fechas = pd.to_datetime(d[f"_fecha_{combustible}"], errors="coerce")
if fechas.notna().any():
    st.caption(f"Última actualización de precios en la selección: **{fechas.max().date()}**")

# ==========================================================================
# ESTRUCTURA DE COLUMNAS (UX MEJORADA)
# ==========================================================================
# col_viz tomará el 70% de la pantalla (Gráficos), col_chat el 30% (Chatbot)
col_viz, col_chat = st.columns([7, 3], gap="large")

with col_viz:
    # ---- KPIs ----
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Estaciones", f"{len(d):,}".replace(",", "."))
    c2.metric("Precio promedio", pesos(d[combustible].mean()))
    c3.metric("Más barato", pesos(d[combustible].min()))
    c4.metric("Más caro", pesos(d[combustible].max()))

    st.divider()

    # ---- Visualización 1: Mapa ----
    st.subheader(f"🗺️ Mapa de precios · {combustible}")
    st.plotly_chart(fig_mapa(d, combustible), use_container_width=True)

    # ---- Visualización 2: Ranking de comunas ----
    st.subheader(f"🏆 Ranking de comunas · {combustible}")
    col_a, col_b = st.columns(2)
    orden = col_a.radio("Mostrar", ["Más baratas", "Más caras"], horizontal=True)
    topn = col_b.slider("Cantidad de comunas", 5, 30, 15)

    asc = orden == "Más baratas"
    rank = (d.groupby("comuna")[combustible].mean()
              .sort_values(ascending=asc).head(topn).reset_index())
    fig_rank = px.bar(
        rank.sort_values(combustible, ascending=not asc),
        x=combustible, y="comuna", orientation="h",
        color=combustible, color_continuous_scale="RdYlGn_r",
        labels={combustible: "Precio promedio ($)", "comuna": ""}, height=500,
    )
    fig_rank.update_layout(coloraxis_showscale=False, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig_rank, use_container_width=True)

    # ---- Visualización 3: Comparación por distribuidor (marca) ----
    st.subheader(f"🏷️ Precio promedio por distribuidor · {combustible}")
    marca = (d.groupby("marca")[combustible]
               .agg(precio="mean", estaciones="count").reset_index())
    marca = marca[marca["estaciones"] >= 3].sort_values("precio")
    fig_marca = px.bar(
        marca, x="precio", y="marca", orientation="h",
        color="precio", color_continuous_scale="RdYlGn_r",
        hover_data={"estaciones": True, "precio": ":$,.0f"},
        labels={"precio": "Precio promedio ($)", "marca": ""}, height=500,
    )
    fig_marca.update_layout(coloraxis_showscale=False, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig_marca, use_container_width=True)
    st.caption("Solo se muestran marcas con 3 o más estaciones en la selección.")
    st.caption("Fuente: Comisión Nacional de Energía (CNE) · Proyecto SIC Coding & Programming")

with col_chat:
    # ==========================================================================
    # 🤖 MÓDULO DE IA: ESTILO ASTRO-PAWS (PURO Y SIN LANGCHAIN)
    # ==========================================================================
    if df is not None:
        st.subheader("🤖 Asistente Virtual")
        st.markdown("<small>Pregúntame sobre los datos. Ej: *¿En qué comuna está la Gasolina 95 más barata?*</small>", unsafe_allow_html=True)

        try:
            google_api_key = st.secrets["GOOGLE_API_KEY"]
        except Exception:
            google_api_key = os.environ.get("GOOGLE_API_KEY")

        if not google_api_key:
            st.warning("Configura GOOGLE_API_KEY en secrets.toml")
        else:
            # 1. Inicializamos el cliente exacto que usaste en Astro-Paws
            cliente = genai.Client(api_key=google_api_key)

            # 2. Transformamos la base de datos a un formato que Gemini pueda "leer"
            # Nos quedamos con las columnas clave para ahorrar memoria
            columnas_clave = ['region', 'comuna', 'direccion', 'marca', 'Gasolina 93', 'Gasolina 95', 'Diésel']
            datos_texto = df[columnas_clave].to_csv(index=False)

            # 3. El System Prompt directo y claro
            INSTRUCCIONES = f"""
            Eres un asistente experto en el mercado de combustibles de Chile.
            
            Aquí tienes la base de datos completa y actualizada de las estaciones de servicio en formato CSV:
            --- INICIO DE DATOS ---
            {datos_texto}
            --- FIN DE DATOS ---

            REGLAS:
            1. Responde preguntas basándote ÚNICAMENTE en los datos de arriba.
            2. Si preguntan por "bencina" asume 'Gasolina 93'.
            3. Formatea los precios siempre como peso chileno (Ej: $1.250 sin decimales).
            4. Responde de manera natural, conversacional y directa, sin mostrar tablas a menos que se te pida.
            """

            # 4. Manejo del historial en la memoria de Streamlit
            if "chat_sesion" not in st.session_state:
                # Creamos el chat con memoria nativa, igual que en tu backend de Flask
                st.session_state.chat_sesion = cliente.chats.create(
                    model="gemini-2.5-flash",
                    config=types.GenerateContentConfig(
                        system_instruction=INSTRUCCIONES,
                        temperature=0.2 # Un toque de naturalidad sin perder precisión
                    )
                )
                st.session_state.mensajes_chat = []

            chat_container = st.container(height=600)

            # Dibujar mensajes previos
            for mensaje in st.session_state.mensajes_chat:
                with chat_container.chat_message(mensaje["rol"]):
                    st.markdown(mensaje["contenido"])

            pregunta = st.chat_input("Escribe tu pregunta aquí...")

            if pregunta:
                st.session_state.mensajes_chat.append({"rol": "user", "contenido": pregunta})
                with chat_container.chat_message("user"):
                    st.markdown(pregunta)

                with chat_container.chat_message("assistant"):
                    with st.spinner("Leyendo la base de datos..."):
                        try:
                            # Enviamos el mensaje directo, el SDK maneja la memoria solo
                            respuesta = st.session_state.chat_sesion.send_message(pregunta)
                            st.markdown(respuesta.text)
                            st.session_state.mensajes_chat.append({"rol": "assistant", "contenido": respuesta.text})
                            
                        except Exception as e:
                            st.error(f"Error de conexión espacial: {e}")