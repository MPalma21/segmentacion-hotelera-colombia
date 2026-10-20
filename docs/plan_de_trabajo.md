# Plan de Trabajo y Asignación Equitativa de Responsabilidades

**Proyecto:** Segmentación multidimensional del mercado hotelero colombiano y visualización interactiva con Shiny  
**Equipo:**
* **Juan José Echeverry** (202616233)
* **Sergio Alejandro López Valderrama** (202111932)
* **Miguelangel Palma** (202621481)

---

## 1. Distribución de Roles Principales

Para garantizar un balance real de carga y especialización técnica, el proyecto se divide en 3 áreas nucleares, asignando un responsable principal por área con acompañamiento transversal:

```
                    ┌───────────────────────────────────────────────┐
                    │          COORDINACIÓN & INTEGRACIÓN           │
                    │   (Revisión cruzada de código y entregable)   │
                    └───────────────────────┬───────────────────────┘
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
┌───────────────────────┐   ┌───────────────────────────────┐   ┌───────────────────────────────┐
│       SERGIO          │   │           JUAN JOSÉ           │   │          MIGUELANGEL          │
│ Ingestión & Calidad   │   │     Analítica & Modelado      │   │  Interactividad & Geosistemas │
│   (Data Engineering)  │   │        (Data Science)         │   │       (Fullstack Shiny)       │
└───────────────────────┘   └───────────────────────────────┘   └───────────────────────────────┘
```

### **A. Sergio Alejandro López — Data Engineering & Cruces Geoespaciales**
* **Responsabilidad central:** Construir el pipeline de ingestión y asegurar la calidad e integridad de los datos.
* **Tareas específicas:**
  1. Diseñar el cliente de extracción para las 4 APIs SODA (`RNT`, `DIVIPOLA`, `Extranjeros No Residentes`, `Transporte Aéreo Comercial`) con paginación (`$limit`, `$offset`).
  2. Implementar la auditoría de calidad de datos: detección de nulos, duplicados, registros inactivos y consistencia de tipos.
  3. Ejecutar la homologación geográfica contra la base oficial de códigos DIVIPOLA (estandarización de códigos de 5 y 2 dígitos).
  4. Generar el esquema de persistencia local en formato Parquet en `data/raw` y `data/processed` con documentación de diccionarios de variables.

---

### **B. Juan José Echeverry — Feature Engineering, Clustering & Validación Estadística**
* **Responsabilidad central:** Formulación de variables y modelado analítico no supervisado con `scikit-learn`.
* **Tareas específicas:**
  1. Diseñar y construir los indicadores analíticos:
     - **Micro (Hoteles):** Ratios operativos (camas/habitación, personal por habitación, escala).
     - **Macro (Municipios):** Densidad hotelera, ratio oferta/demanda internacional y conectividad aérea.
  2. Implementar el pipeline de preprocesamiento (imputación, transformaciones logarítmicas ante asimetrías y estandarización con `StandardScaler`).
  3. Ejecutar los modelos K-Means para ambos niveles (hoteles y municipios), evaluando el rango $k = 2 \dots 8$.
  4. Evaluar la estabilidad y calidad de agrupamiento mediante curvas de inercia (método del codo) y *Silhouette Scores*.
  5. Interpretar y redactar la caracterización y perfil de negocio de cada clúster.

---

### **C. Miguelangel Palma — Arquitectura Shiny, Mapas Interactivos & Dashboarding**
* **Responsabilidad central:** Construcción de la experiencia de usuario y visualización interactiva.
* **Tareas específicas:**
  1. Diseñar y estructurar la aplicación interactiva en **Shiny for Python** (`app/app.py`) con navegación por pestañas (`ui.page_navbar`) y panel lateral de filtros reactivos.
  2. Desarrollar el módulo de visualización geoespacial con `ipyleaflet` / `plotly`, integrando agrupamiento de marcadores (*MarkerCluster*) y capas temáticas para evitar degradación de rendimiento.
  3. Implementar los gráficos analíticos con `Plotly` (diagramas de dispersión oferta vs. demanda en escala logarítmica, gráficos de barras de perfiles y radar charts).
  4. Crear la vista de directorio de hoteles priorizados con tabla interactiva, filtros dinámicos y métricas de resumen reactivas.

---

## 2. Cronograma de Hitos y Entregables (Sprints)

| Sprint / Hito | Duración | Objetivos y Entregables | Responsable Principal | Apoyo |
| :--- | :---: | :--- | :--- | :--- |
| **Sprint 1: Ingestión y Pipeline ETL** | Semana 1 | Ingestión funcional de las 4 APIs SODA; limpieza y homologación DIVIPOLA; datasets en Parquet. | **Sergio** | Juan José |
| **Sprint 2: Feature Engineering & Clustering** | Semana 2 | Construcción de variables; K-Means $k=2\dots8$; curvas de inercia y silueta; perfiles de clústeres listos. | **Juan José** | Sergio |
| **Sprint 3: Desarrollo App Shiny & Mapas** | Semana 3 | App Shiny funcional; integración de mapas (`ipyleaflet`), filtros reactivos y visualizaciones `Plotly`. | **Miguelangel** | Juan José |
| **Sprint 4: Integración, QA y Documentación** | Semana 4 | Pruebas de extremo a extremo, optimización de tiempos de carga, redacción del tutorial/reporte y validación final. | **Todos** (Equitativo) | **Todos** |

---

## 3. Matriz RACI (Responsable, Aprobador, Consultado, Informado)

| Tarea / Actividad | Sergio | Juan José | Miguelangel |
| :--- | :---: | :---: | :---: |
| Conexión y paginación APIs SODA | **R / A** | C | I |
| Limpieza y homologación con DIVIPOLA | **R / A** | C | I |
| Construcción de variables micro y territoriales | C | **R / A** | C |
| Modelado K-Means y validación (Elbow/Silhouette) | I | **R / A** | C |
| Interpretación de perfiles de clústeres | C | **R** | **A** |
| Arquitectura UI/Server en Shiny for Python | I | C | **R / A** |
| Mapas interactivos (`ipyleaflet` / marcadores) | C | I | **R / A** |
| Gráficos interactivos Plotly | I | C | **R / A** |
| Revisión cruzada de código (Pull Requests) | **R** | **R** | **R** |
| Redacción del documento final y diapositivas | **R** | **R** | **R** |

> **Convención RACI:**  
> **R** = *Responsible* (quien ejecuta la tarea)  
> **A** = *Accountable* (quien aprueba y valida la entrega final de esa tarea)  
> **C** = *Consulted* (quien aporta insumos y retroalimentación)  
> **I** = *Informed* (quien se mantiene al tanto del progreso)

---

## 4. Acuerdos de Buenas Prácticas del Equipo

1. **Gestión de Versiones (Git):**
   - Prohibido hacer commits directos a `main`. Cada integrante trabaja en ramas con nombres semánticos:
     - `feature/data-ingestion-soda` (Sergio)
     - `feature/clustering-kmeans` (Juan José)
     - `feature/shiny-dashboard-maps` (Miguelangel)
   - Todo cambio a `main` requiere al menos 1 aprobación mediante Pull Request (*Peer Code Review*).
2. **Reproducibilidad y Datos:**
   - No versionar archivos masivos de datos (`data/raw/*` y `data/processed/*` están ignorados en `.gitignore`).
   - El pipeline debe poder reejecutarse desde cero corriendo los scripts o notebooks correspondientes.
3. **Manejo de Dependencias:**
   - Cualquier nueva librería requerida debe agregarse a `requirements.txt` previa socialización con el equipo.
