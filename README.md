# Segmentación Multidimensional del Mercado Hotelero Colombiano y Visualización Interactiva con Shiny

Proyecto final de analítica de datos en Python que integra datos abiertos de turismo, conectividad aérea y geografía para segmentar la oferta hotelera y los municipios de Colombia mediante técnicas de aprendizaje no supervisado (**K-Means**), presentando los resultados en un tablero interactivo con **Shiny for Python**, **ipyleaflet** y **Plotly**.

---

## 👥 Equipo de Trabajo
* **Juan José Echeverry** — 202616233 (*Data Science & Modelado*)
* **Sergio Alejandro López Valderrama** — 202111932 (*Data Engineering & Pipeline ETL*)
* **Miguelangel Palma** — 202621481 (*UI/UX, Visualización Geoespacial & Shiny*)

El plan de trabajo detallado y la matriz RACI se encuentran en [docs/plan_de_trabajo.md](docs/plan_de_trabajo.md).

---

## 🏗️ Arquitectura del Repositorio

```text
Proyecto Final Python/
│
├── app/                        # Aplicación interactiva Shiny for Python
│   └── app.py                  # Definición de UI, servidor y widgets reactivos
│
├── data/                       # Almacenamiento local de datos (ignorado en git)
│   ├── raw/                    # Descargas crudas desde APIs SODA
│   ├── processed/              # Datasets consolidados, limpios y etiquetados (Parquet)
│   └── geo/                    # Capas geográficas y homologaciones DIVIPOLA
│
├── docs/                       # Documentación metodológica y gestión del proyecto
│   └── plan_de_trabajo.md      # Asignación de roles, cronograma de sprints y matriz RACI
│
├── notebooks/                  # Cuadernos de experimentación, EDA y validación estadística
│
├── src/                        # Módulos Python reutilizables
│   ├── __init__.py
│   ├── config.py               # Constantes, rutas y endpoints de APIs
│   ├── ingestion.py            # Funciones de consulta a APIs SODA con paginación
│   ├── processing.py           # Limpieza, cruces con DIVIPOLA y agregación territorial
│   └── modeling.py             # Pipeline de escalado, K-Means, métricas y perfiles
│
├── .gitignore                  # Exclusiones de Git (entornos virtuales, data pesada)
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación principal
```

---

## 📊 Fuentes de Datos (APIs SODA - Datos Abiertos Colombia)

1. **Registro Nacional de Turismo (RNT) — MinCIT:** Hoteles formales activos, capacidad en habitaciones, camas, personal y ubicación.
2. **DIVIPOLA — DANE:** Códigos oficiales departamentales y municipales para homologación territorial y coordenadas.
3. **Extranjeros No Residentes — MinCIT / Migración Colombia:** Flujos mensuales de turismo internacional para estimar demanda y estacionalidad.
4. **Transporte Aéreo Comercial — Aerocivil:** Tráfico origen-destino de pasajeros y rutas activas como proxy de conectividad.

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonar el repositorio y crear entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activar entorno (Linux/macOS)
source venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación Shiny
```bash
shiny run --reload app/app.py
```
La aplicación quedará disponible en el navegador en `http://127.0.0.1:8000`.

---

## 📈 Metodología Analítica

1. **Ingestión & Calidad:** Consulta paginada a endpoints SODA, auditoría de valores atípicos y cruce con códigos DIVIPOLA.
2. **Feature Engineering:** Construcción de variables a nivel establecimiento (escala operativa) y a nivel territorial (densidad, demanda turística, conectividad).
3. **Clustering:** Implementación de K-Means evaluando $k \in [2, 8]$ mediante curva de inercia (método del codo) y *Silhouette Score*.
4. **Visualización Reactiva:** Panel web con filtros dinámicos por departamento y clúster, mapa interactivo y gráficos analíticos.
