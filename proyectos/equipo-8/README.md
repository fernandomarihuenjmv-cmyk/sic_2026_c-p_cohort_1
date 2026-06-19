# Proyectos Grupales — Samsung Innovation Campus Chile 2026

**Cohort 1 | Curso de Codigo y Programacion (C&P)**

Repositorio oficial: [github.com/davidlealo/sic_2026_c-p_cohort_1](https://github.com/davidlealo/sic_2026_c-p_cohort_1)
Ejemplos de referencia: [Google Drive](https://drive.google.com/drive/u/0/folders/1xwwwXiazR4v2h3KRfgm5C9xarGMpZ5P_)

---

## Indice

1. [Que es este proyecto](#1-que-es-este-proyecto)
2. [Equipos y fechas clave](#2-equipos-y-fechas-clave)
3. [Lo que deben entregar](#3-lo-que-deben-entregar)
4. [Estructura de carpetas](#4-estructura-de-carpetas)
5. [La presentacion de 7 minutos](#5-la-presentacion-de-7-minutos)
6. [Pauta de evaluacion](#6-pauta-de-evaluacion)
7. [Criterios de calidad del codigo](#7-criterios-de-calidad-del-codigo)
8. [Como hacer el Pull Request](#8-como-hacer-el-pull-request)
9. [Proyectos del Cohort 1](#9-proyectos-del-cohort-1)

---

## 1. Que es este proyecto

El proyecto grupal final es la actividad de cierre del curso de Codigo y Programacion del Samsung Innovation Campus Chile 2026.

Cada equipo elige un dataset de datos reales, formula una pregunta de analisis concreta, construye un dashboard interactivo con Streamlit o Gradio y presenta sus hallazgos en 7 minutos el 24 de junio.

**El objetivo no es mostrar que saben usar todas las herramientas del curso. Es demostrar que pueden usar las herramientas correctas para responder una pregunta con datos y comunicar el resultado a una audiencia no tecnica.**

---

## 2. Equipos y fechas clave

| Fecha | Actividad |
|-------|-----------|
| Lunes 15 jun — Clase 7 | Kickoff: registrar equipo y dataset al inicio de la clase |
| Miercoles 17 jun — Clase 8 | Cargar datos, EDA inicial, formular pregunta de analisis |
| Viernes 19 jun — Clase 9 | Limpieza, analisis principal, construir el dashboard |
| Lunes 22 jun — Clase 10 | Pulir dashboard, publicar, documentar repo, presentaciones finales (7 min por equipo) |
| **Lunes 22 jun — 22:00 hrs** | **Fecha limite para enviar el Pull Request** |
| Miercoles 24 jun — Clase 11 | Presentaciones (en caso de que falten grupos) |

**Equipos:** hasta 6 estudiantes. Solo estudiantes del Cohort 1. Un solo PR por equipo.

---

## 3. Lo que deben entregar

### Entregable 1: Pull Request en GitHub

Antes del lunes 22 de junio a las 22:00 hrs, el equipo debe tener un PR aprobado con:

* Carpeta `/proyectos/nombre-del-equipo/` con la estructura requerida
* Al menos un notebook `.ipynb` con el análisis documentado y comentado
* Una aplicación funcional (`app.py` o archivo equivalente) desarrollada con **Streamlit o Gradio**
* `requirements.txt` actualizado
* `README.md` con descripción, dataset, pregunta de análisis, hallazgos, link al dashboard/app e integrantes
* Aplicación publicada en **Streamlit Cloud, Hugging Face Spaces o plataforma equivalente** (URL en el README)

### Entregable 2: Presentación en la Clase 10 u 11

* 7 minutos de presentación con la aplicación abierta en pantalla
* 3 minutos de preguntas del docente y del grupo
* Todos los integrantes deben estar presentes

### Requisitos mínimos de la aplicación

| Elemento        | Requisito mínimo                                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Visualizaciones | Al menos 3 visualizaciones relevantes para responder la pregunta de análisis                                           |
| Interactividad  | Al menos 2 controles interactivos (filtros, sliders, dropdowns, inputs, etc.) que actualicen resultados en tiempo real |
| Indicadores     | Al menos 3 métricas, KPIs o valores resumen visibles en la interfaz                                                    |
| Texto           | Una sección que explique el hallazgo principal en lenguaje no técnico                                                  |
| Dataset         | Datos reales con volumen suficiente para responder la pregunta, licencia verificable y fuente citada en el README      |
| Publicación     | URL pública funcionando correctamente                                                                                  |

**Bibliotecas sugeridas para visualización:** Plotly, Altair, Folium, Matplotlib, PyDeck u otras equivalentes.

---

## 4. Estructura de carpetas

Cada equipo crea su carpeta dentro de `/proyectos/`. El nombre debe ser en minusculas y con guion medio.

```
proyectos/
  nombre-del-equipo/
    data/
      dataset_original.csv      <- datos originales (o link si pesa mas de 50 MB)
      dataset_limpio.csv        <- datos procesados
    notebooks/
      01_eda.ipynb
      02_limpieza.ipynb
      03_analisis.ipynb
    outputs/
      dashboard_preview.png     <- captura del dashboard
    app.py                      <- app Streamlit principal
    requirements.txt
    README.md
```

> **Atencion:** no subir archivos mayores a 50 MB. Para datasets grandes, subir a Google Drive o Kaggle y poner el link de descarga en el README.

---

## 5. La presentacion de 7 minutos

La presentacion sigue esta estructura. El docente hace sonar una senal a los 7 minutos.

| Bloque | Tiempo | Contenido |
|--------|--------|-----------|
| 1 | 1 min | **Problema y dataset:** que datos usan, de donde vienen, por que son relevantes |
| 2 | 1.5 min | **Pregunta de analisis:** cual es la pregunta que responden y por que importa. Quien se beneficia de la respuesta |
| 3 | 3 min | **Dashboard en vivo:** mostrar el dashboard funcionando. Explicar cada visualizacion. Mostrar los filtros. Enunciar el hallazgo principal |
| 4 | 1.5 min | **Conclusion y limitaciones:** que responde el analisis, que no puede responder, una cosa que harian distinto con mas tiempo |

> El dashboard debe estar abierto en el navegador antes de que empiece la presentacion. No se cuenta el tiempo de carga.

---

## 6. Pauta de evaluacion

El proyecto vale el **60% de la nota final del curso**. Se evaluan 6 criterios con tres niveles cada uno.

Para obtener el certificado: asistencia igual o mayor al 90% y nota total del curso igual o mayor al 50.

### Rubrica

#### Innovacion — 20 pts

| Nivel | Descripcion |
|-------|-------------|
| Insuficiente (0-10 pts) | Replica un tutorial existente sin modificaciones propias. El dataset y la pregunta son triviales o genericos |
| Logrado (11-16 pts) | El enfoque tiene algo propio. El dataset es real y la pregunta es especifica aunque no original |
| Destacado (17-20 pts) | El proyecto aborda un problema no trivial con un enfoque diferenciado. El dataset y la pregunta aportan algo que va mas alla de los ejemplos del curso |

#### Utilidad del dashboard — 20 pts

| Nivel | Descripcion |
|-------|-------------|
| Insuficiente (0-10 pts) | El dashboard no funciona al momento de la presentacion, los filtros no tienen efecto, o las visualizaciones no son relevantes para la pregunta |
| Logrado (11-16 pts) | El dashboard funciona. Las visualizaciones son correctas. Hay al menos 2 filtros operativos |
| Destacado (17-20 pts) | El dashboard funciona sin errores. Los 3 graficos son directamente relevantes para la pregunta. Los filtros actualizan las metricas en tiempo real |

#### Valor del analisis — 20 pts

| Nivel | Descripcion |
|-------|-------------|
| Insuficiente (0-10 pts) | El analisis se limita a estadisticas descriptivas sin interpretar resultados. No se responde la pregunta formulada |
| Logrado (11-16 pts) | El analisis responde parcialmente la pregunta. Hay interpretacion de los resultados aunque superficial |
| Destacado (17-20 pts) | El analisis responde la pregunta con evidencia clara. El hallazgo es especifico, medible y esta comunicado en lenguaje accesible |

#### Cumplimiento tecnico — 10 pts

| Nivel | Descripcion |
|-------|-------------|
| Insuficiente (0-5 pts) | El repositorio no tiene la estructura requerida, el `requirements.txt` no funciona, o el README no tiene los campos minimos |
| Logrado (6-8 pts) | El repositorio tiene estructura correcta. El README tiene los campos principales. El `requirements.txt` funciona |
| Destacado (9-10 pts) | README completo con todos los campos y link al dashboard. `requirements.txt` permite reproducir el proyecto sin errores. Notebooks con comentarios |

#### Presentacion — 20 pts

| Nivel | Descripcion |
|-------|-------------|
| Insuficiente (0-10 pts) | No sigue la estructura de 4 bloques. El equipo no puede explicar el codigo o las decisiones tomadas. Se excede el tiempo en mas de 1 minuto |
| Logrado (11-16 pts) | Sigue la estructura. El dashboard se muestra en vivo. El equipo puede responder preguntas basicas. Respeta el tiempo |
| Destacado (17-20 pts) | Presentacion clara y fluida. El hallazgo queda comunicado en el bloque del dashboard. El equipo responde preguntas con precision. Respeta los 7 minutos |

#### Trabajo en equipo — 10 pts

| Nivel | Descripcion |
|-------|-------------|
| Insuficiente (0-5 pts) | Solo uno o dos integrantes participan. El historial de commits muestra contribuciones de menos de la mitad del equipo |
| Logrado (6-8 pts) | La mayoria participa. El historial de commits muestra contribuciones de varios miembros |
| Destacado (9-10 pts) | Todos los integrantes tienen un rol visible. Commits distribuidos. El equipo responde preguntas de forma coordinada |

### Ponderacion del curso

| Componente | Ponderacion |
|------------|-------------|
| Quizzes de cierre (4 quizzes) | 20% |
| Post-exam final | 20% |
| **Proyecto grupal final** | **60%** |

---

## 7. Criterios de calidad del codigo

El codigo se revisa para el criterio de Cumplimiento Tecnico.

### El notebook

- Celdas de Markdown al inicio de cada seccion explicando que se hace y por que
- Comentarios en el codigo para decisiones no obvias
- Las celdas corren en orden de arriba a abajo sin errores — antes del PR: `Kernel > Restart & Run All`
- Los outputs estan guardados y son visibles sin ejecutar

### El archivo app.py

- Corre con `streamlit run app.py` sin modificaciones
- Usa `@st.cache_data` para cargar los datos
- Los filtros del sidebar afectan graficos y metricas en tiempo real
- Sin credenciales ni API keys hardcodeadas en el codigo

### El requirements.txt

Generarlo con:

```bash
pip freeze > requirements.txt
```

Debe incluir al minimo: `streamlit`, `pandas`, `plotly` o `altair`, y cualquier libreria especifica del analisis.

### Commits

```bash
# Mensajes correctos
git commit -m "Agrega EDA con histogramas y heatmap de correlacion"
git commit -m "Limpia nulos en columna monto usando mediana por region"
git commit -m "Agrega filtro de rango de fechas al sidebar"
git commit -m "Publica app en Streamlit Cloud y agrega URL al README"

# No aceptados
git commit -m "update"
git commit -m "cambios"
```

Al menos un commit por etapa (EDA, limpieza, analisis, dashboard) y al menos un commit por integrante desde su propia cuenta de GitHub.

---

## 8. Como hacer el Pull Request

### Paso 1: Hacer fork del repositorio oficial

Ir a [github.com/davidlealo/sic_2026_c-p_cohort_1](https://github.com/davidlealo/sic_2026_c-p_cohort_1) y hacer clic en **Fork**.

### Paso 2: Clonar el fork

```bash
git clone https://github.com/TU-USUARIO/sic_2026_c-p_cohort_1.git
cd sic_2026_c-p_cohort_1
```

### Paso 3: Crear la carpeta del equipo

```bash
mkdir -p proyectos/nombre-del-equipo/data
mkdir -p proyectos/nombre-del-equipo/notebooks
mkdir -p proyectos/nombre-del-equipo/outputs
```

### Paso 4: Copiar los archivos y hacer commit

```bash
git add proyectos/nombre-del-equipo/
git commit -m "Agrega proyecto final equipo nombre-del-equipo"
git push origin main
```

### Paso 5: Abrir el Pull Request

En GitHub, ir al fork y hacer clic en **Compare & pull request**.

Verificar que apunte a: `base repository: davidlealo/sic_2026_c-p_cohort_1` | `base: main`

**Titulo del PR:**
```
[Proyecto] nombre-equipo — Nombre del Proyecto
```

**Descripcion del PR (copiar y completar):**

```markdown
## Equipo
- Integrante 1 (GitHub: @usuario1)
- Integrante 2 (GitHub: @usuario2)

## Dataset
Fuente: [nombre y URL]
Filas: N  |  Columnas: N  |  Licencia: CC0 / CC BY / etc.

## Pregunta de analisis
[Una oracion con la pregunta que responde el proyecto]

## Hallazgo principal
[Una o dos oraciones con el resultado mas importante]

## Link al dashboard
https://tu-proyecto.streamlit.app

## Checklist
- [ ] README con descripcion, dataset, pregunta, hallazgos y link al dashboard
- [ ] requirements.txt actualizado
- [ ] Dashboard publicado y accesible
- [ ] Notebooks con comentarios en espanol
- [ ] Sin archivos mayores a 50 MB
```

### Paso 6: Notificar

Enviar la URL del PR al grupo de WhatsApp del Cohort 1:
`PR enviado - Equipo [nombre]: [URL del PR]`

---

## 9. Proyectos del Cohort 1

| Equipo | Tema | Dataset | Dashboard |
|--------|------|---------|-----------|
| *(por completar a medida que llegan los PRs)* | | | |

---

**Programa:** Samsung Innovation Campus Chile 2026
**Ejecutora:** [Innovacien](https://innovacien.org) — contacto@innovacien.org
**Licencia:** MIT
