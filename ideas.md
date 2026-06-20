# Preguntas para resolver:

Con solo la VIII EME 2025 (corte transversal, sin serie de tiempo), puedes plantear preguntas de **asociación entre grupos**, no de evolución. Te dejo varias opciones agrupadas por tema, cada una con las variables que ya están en tu CSV:

**Informalidad**

- ¿Qué proporción de microemprendedores opera de manera informal en 2025, y cómo varía según sexo, región, rama económica y nivel educacional?
*(variables: `e1`, `e2`, `e3` → informalidad construida igual que en la Programación 5 del manual; cruces con `sexo`, `region`, `c1_b`)*

**Brecha de género**

- ¿Existe una brecha de ganancias entre hombres y mujeres microemprendedores en 2025? ¿En qué rama económica o región es más amplia?
*(variables: `ganancia_final`, `sexo`, `c1_b`, `region`)*
- ¿Las mujeres microemprendedoras destinan más tiempo a trabajo doméstico/de cuidado no remunerado que los hombres, y eso se relaciona con menos horas dedicadas al negocio?
*(variables: Módulo L, `c6_1/c6_2/c6_3` horas trabajadas, `sexo`)*

**Acceso a financiamiento público**

- ¿Qué porcentaje de microemprendedores conoce, ha postulado y ha sido beneficiario de programas estatales (Fosis, Sercotec, Corfo, Indap, etc.), y qué factores (región, formalidad, sexo) se asocian a mayor acceso?
*(variables: `k12_1` a `k12_11`, `k13_x`, `k14_x`, `e3`, `sexo`, `region`)*
- Entre quienes han solicitado crédito, ¿qué tipo de financiamiento es más común y cuál es la principal razón para no solicitarlo?
*(variables: `g1` y siguientes del módulo G — revisa si están en tu CSV, pueden no estar todas)*

**Motivación y resultados del negocio**

- ¿La motivación para emprender (necesidad vs. oportunidad) está asociada con mayor o menor formalidad y ganancia?
*(variable: `b1` recodificada como en la Programación 3 del manual)*

**Tecnología**

- ¿El uso de internet o el conocimiento de inteligencia artificial entre microemprendedores se relaciona con mayores ganancias o formalidad?
*(variables: `i5_x`, `i8`, `ganancia_final`, informalidad)*

**Generación de empleo**

- ¿Qué características del negocio (formalidad, rama, región) se asocian con tener trabajadores contratados o con la intención de contratar en los próximos 12 meses?
*(variables: `f1`, `f5`, informalidad, `c1_b`)*

**Entorno y redes de apoyo**

- ¿Pertenecer a una cooperativa, gremio o asociación se asocia con mejores resultados económicos o mayor acceso a financiamiento?
*(variables: `k16_1`, `k16_2`, `ganancia_final`, `k12_x`)*

**Medioambiente**

- ¿Qué regiones o tipos de negocio han sido más afectados por desastres naturales en los últimos 5 años, y qué medidas de mitigación han tomado?
*(variables: Módulo M, `region`)*

---

Para tu dashboard, te recomendaría una **pregunta central** que combine los tres pilares que ya tenías en la propuesta, pero adaptada a un solo año:

> *¿Cómo se relacionan el sexo, la región y la rama económica de los microemprendedores con su nivel de informalidad, sus ganancias y su acceso a financiamiento público, según la VIII Encuesta de Microemprendimiento 2025?*
> 

Esto mantiene tus 3 KPIs (ganancia promedio, tasa de formalización, índice de apoyo estatal) intactos. Eso sí, como ya no tienes el filtro de "año", para cumplir el mínimo de 2 controles interactivos en Streamlit/Gradio te conviene reemplazarlo por algo como **rama económica** (`c1_b`) o **tramo de edad** (`tramo_etario`), dejando **región** como el otro filtro.

cris: Creo que esta ultima pregunta es quizás la más acertada para investigar y explorar en nuestro data set