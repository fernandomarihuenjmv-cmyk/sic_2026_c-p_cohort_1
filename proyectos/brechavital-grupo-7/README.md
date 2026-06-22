# 🏥 GESAssist: Análisis y Clasificación de Diagnósticos GES

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![Plotly](https://img.shields.io/badge/Plotly-Express-orange.svg)

## 📌 Descripción del Proyecto
GESAssist es una aplicación interactiva desarrollada en **Python** con **Streamlit** que permite analizar y visualizar un conjunto de datos médicos enfocado en la clasificación de Garantías Explícitas en Salud (GES). 

El objetivo principal de este proyecto es explorar patrones en los diagnósticos para entender **qué variables (como la edad o el tipo de diagnóstico) influyen en que un caso sea clasificado como GES o No GES**. A través de visualizaciones interactivas y métricas en tiempo real, facilitamos la toma de decisiones exploratorias basadas en datos.

---

## 🚀 Aplicación en Vivo (Dashboard)
Puedes acceder y probar la aplicación directamente desde tu navegador sin instalar nada:

🌐 **[🔗 Enlace al Dashboard GESAssist en Streamlit Cloud](https://mtys24-gesassist-app-trds27.streamlit.app/)**  


---

## 📊 Dataset y Origen de los Datos
El conjunto de datos utilizado para este análisis contiene registros anónimos de diagnósticos médicos y las edades de los pacientes.

* **Fuente:** Datos simulados / extraídos con propósitos educativos y analíticos basados en la estructura del sistema de salud chileno (Ajustar si proviene de MINSAL o plataforma de datos abiertos).
* **Licencia:** El uso de este dataset es exclusivamente para fines académicos y de investigación. Licencia de uso libre (Open Data).
* **Volumen:** El dataset contiene miles de registros procesados, garantizando representatividad en el análisis.

---

## 🛠️ Instrucciones de Instalación Local
Si deseas ejecutar este proyecto en tu propia máquina, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Mtys24/GESAssist.git
   cd GESAssist
   ```

2. **Crear un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación Streamlit:**
   ```bash
   streamlit run app.py
   ```

---

## 📂 Estructura del Repositorio
```
GESAssist/
├── app.py                   # Script principal del Dashboard en Streamlit
├── data/
│   ├── dataset_original.csv # Dataset crudo
│   └── dataset_limpio.csv   # Dataset procesado
├── notebooks/
│   ├── 01_eda.ipynb         # Análisis Exploratorio de Datos
│   ├── 02_limpieza.ipynb    # Pipeline de limpieza y transformación
│   └── 03_analisis.ipynb    # Respuestas a la pregunta principal
├── outputs/                 # Gráficos e imágenes exportadas
├── requirements.txt         # Dependencias del proyecto

```

---

## 🧑‍💻 Equipo de Trabajo

| Integrante                | Rol en el Proyecto                 | GitHub                                      |
|---------------------------|------------------------------------|---------------------------------------------|
| **Matías Manríquez**      | Data Scientist & Analista de Datos | [@Mtys24](https://github.com/Mtys24)        |
| **José Salgado Escalona** | Data Scientist & Analista de Datos | [@JoseRicardoSE](https://github.com/JoseRicardoSE) |
| **Ignacio Madriaga**      | Data Scientist & Analista de Datos | [@VonCreed-tech](https://github.com/VonCreed-tech) |
| **Daniel Segovia**        | Data Scientist & Analista de Datos | [@reyconker](https://github.com/reyconker)   |

---
*Desarrollado para el proyecto final de Data Science.*
