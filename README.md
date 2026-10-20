# Segmentacion Multidimensional del Mercado Hotelero Colombiano y Visualizacion Interactiva con Shiny

Proyecto final de analitica de datos en Python que integra datos abiertos de oferta hotelera, demanda turistica, conectividad aerea y geografia oficial para segmentar establecimientos y municipios de Colombia mediante tecnicas de aprendizaje no supervisado (K-Means), desplegando los resultados en una aplicacion interactiva con Shiny for Python, ipyleaflet y Plotly.

---

## Integrantes del Equipo

* **Juan Jose Echeverry** - 202616233 (Ciencia de Datos y Modelado Estadistico)
* **Sergio Alejandro Lopez Valderrama** - 202111932 (Ingenieria de Datos y Pipeline ETL)
* **Miguelangel Palma** - 202621481 (Visualizacion Geoespacial y Shiny for Python)

---

## Roadmap del Proyecto

El desarrollo se estructura en cuatro fases secuenciales e iterativas. Cada fase cuenta con un responsable principal, entregables especificos y criterios de aceptacion claros para asegurar una distribucion equitativa del esfuerzo.

```text
[Fase 1: Ingestion y Calidad] ──> [Fase 2: Feature Engineering & Clustering] ──> [Fase 3: Aplicacion Shiny & Mapas] ──> [Fase 4: Integracion y QA]
   Responsable: Sergio               Responsable: Juan Jose                         Responsable: Miguelangel               Responsable: Todo el equipo
```

### Fase 1: Ingestion, Homologacion y Calidad de Datos (Semana 1)
* **Lider de Fase:** Sergio Alejandro Lopez Valderrama
* **Colaborador de Apoyo:** Juan Jose Echeverry
* **Hitos y Entregables:**
  * **Hito 1.1:** Cliente de conexion y paginacion para las 4 APIs SODA de datos.gov.co (`$limit`, `$offset` y filtros por endpoint).
  * **Hito 1.2:** Homologacion geografica con codigos DIVIPOLA (estandarizacion de codigos municipales de 5 digitos y departamentales de 2 digitos).
  * **Hito 1.3:** Auditoria de calidad de datos: remocion de duplicados, imputacion/tratamiento de valores faltantes y filtrado de registros activos del RNT.
  * **Hito 1.4:** Almacenamiento optimizado de datasets procesados en formato Parquet en `data/processed/`.
* **Criterio de Aceptacion:** Datasets limpios y cruzados al 100% con DIVIPOLA, listos para modelado sin errores de referencia espacial.

---

### Fase 2: Feature Engineering, Modelado K-Means y Validacion (Semana 2)
* **Lider de Fase:** Juan Jose Echeverry
* **Colaborador de Apoyo:** Sergio Alejandro Lopez Valderrama
* **Hitos y Entregables:**
  * **Hito 2.1:** Construccion de variables a nivel micro (hoteles): capacidad de habitaciones, camas por habitacion, empleados por habitacion y escala.
  * **Hito 2.2:** Construccion de variables a nivel macro (municipios): inventario total, flujo de extranjeros no residentes y conectividad aerea (pasajeros/rutas).
  * **Hito 2.3:** Pipeline de preprocesamiento estadistico: transformacion de asimetrias y estandarizacion de escalas con `StandardScaler`.
  * **Hito 2.4:** Entrenamiento de K-Means para rango k de 2 a 8, graficacion de curvas de inercia (metodo del codo) y evaluacion con Silhouette Score.
  * **Hito 2.5:** Perfilamiento e interpretacion de negocio para cada segmento identificado (tanto de hoteles como de municipios).
* **Criterio de Aceptacion:** Seleccion analitica justificada del numero optimo de clusters con perfiles descriptivos consolidados.

---

### Fase 3: Arquitectura Shiny, Mapas y Visualizacion Interactiva (Semana 3)
* **Lider de Fase:** Miguelangel Palma
* **Colaborador de Apoyo:** Juan Jose Echeverry
* **Hitos y Entregables:**
  * **Hito 3.1:** Estructuracion de la aplicacion en Shiny for Python (`app/app.py`) con navegacion modular por paneles y panel lateral de filtros reactivos.
  * **Hito 3.2:** Integracion de visualizacion geoespacial con `ipyleaflet` / marcadores agrupados (MarkerCluster) para optimizar el rendimiento del navegador.
  * **Hito 3.3:** Tablero analitico interactivo en `Plotly`: dispersion logaritmica de oferta vs. demanda turistica y diagramas de barras de perfiles operativos.
  * **Hito 3.4:** Directorio interactivo de hoteles priorizados con filtrado reactivo por departamento, escala y cluster territorial.
* **Criterio de Aceptacion:** Aplicacion web reactiva funcional, con tiempo de respuesta agil y navegacion intuitiva entre mapa, graficos y directorio.

---

### Fase 4: Integracion, Optimizacion, QA y Documentacion Final (Semana 4)
* **Lider de Fase:** Responsabilidad compartida (Juan Jose, Sergio, Miguelangel)
* **Hitos y Entregables:**
  * **Hito 4.1:** Pruebas integrales de flujo completo (extraccion -> procesamiento -> persistencia -> visualizacion).
  * **Hito 4.2:** Revision de rendimiento: tiempos de carga de la aplicacion Shiny y optimizacion de consultas a archivos Parquet.
  * **Hito 4.3:** Redaccion del informe tecnico / tutorial final detallando metodologia, hallazgos analiticos y conclusiones.
  * **Hito 4.4:** Preparacion del soporte de presentacion final y revision cruzada de codigo.
* **Criterio de Aceptacion:** Pipeline reproducible de extremo a extremo, documentacion completa y aplicacion desplegada sin fallos.

---

## Matriz de Responsabilidades (RACI)

| Actividad / Entregable | Sergio | Juan Jose | Miguelangel |
| :--- | :---: | :---: | :---: |
| Pipeline de extraccion y paginacion de APIs SODA | R / A | C | I |
| Homologacion con DIVIPOLA y auditoria de calidad | R / A | C | I |
| Construccion de metricas micro y macro | C | R / A | C |
| Modelado K-Means y validacion (Codo / Silueta) | I | R / A | C |
| Caracterizacion analitica de clusters | C | R | A |
| Arquitectura y servidor reactivo de Shiny | I | C | R / A |
| Visualizacion geoespacial y mapas interactivos | C | I | R / A |
| Componentes graficos interactivos Plotly | I | C | R / A |
| Revision de codigo mediante Pull Requests | R | R | R |
| Documento tutorial final y presentacion | R | R | R |

> Convencion: **R** = Responsable (ejecuta), **A** = Aprobador (valida), **C** = Consultado, **I** = Informado.

---

## Arquitectura del Repositorio

```text
Proyecto Final Python/
│
├── app/                        # Aplicacion interactiva Shiny for Python
│   └── app.py                  # Interfaz de usuario, servidor reactivo y visualizaciones
│
├── data/                       # Datos locales organizados (ignorado en control de versiones)
│   ├── raw/                    # Descargas crudas directas de endpoints SODA
│   ├── processed/              # Datasets limpios, enriquecidos y con clusters (Parquet)
│   └── geo/                    # Capas geograficas y diccionarios DIVIPOLA
│
├── docs/                       # Documentacion detallada de soporte
│   └── plan_de_trabajo.md      # Detalle de roles y acuerdos de equipo
│
├── notebooks/                  # Cuadernos para exploracion preliminar y validacion
│
├── src/                        # Modulos de codigo reutilizables
│   ├── __init__.py
│   ├── config.py               # Constantes globales, URLs de APIs y rutas
│   ├── ingestion.py            # Consulta paginada a APIs SODA
│   ├── processing.py           # Homologacion territorial y construccion de variables
│   └── modeling.py             # Pipeline K-Means, metricas y calculo de perfiles
│
├── .gitignore                  # Exclusion de entornos virtuales y archivos pesados
├── requirements.txt            # Dependencias fijadas del proyecto
└── README.md                   # Pagina principal del repositorio con el Roadmap
```

---

## Fuentes de Datos Oficiales (APIs SODA)

1. **Registro Nacional de Turismo (RNT) - MinCIT:** Establecimientos hoteleros formales activos, numero de habitaciones, camas, personal y ubicacion municipal.
2. **DIVIPOLA - DANE:** Nomenclatura oficial de departamentos y municipios con codigos estandarizados y coordenadas para georreferenciacion.
3. **Extranjeros No Residentes - MinCIT / Migracion Colombia:** Series mensuales de visitantes no residentes por destino nacional (indicador de demanda y estacionalidad).
4. **Transporte Aereo Comercial - Aerocivil:** Movimiento de pasajeros y rutas de vuelos nacionales e internacionales hacia cada destino (proxy de conectividad).

---

## Instalacion y Ejecucion Local

### 1. Clonar el repositorio y configurar entorno
```bash
git clone https://github.com/MPalma21/segmentacion-hotelera-colombia.git
cd segmentacion-hotelera-colombia
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# Linux / macOS
source venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicacion interactiva
```bash
shiny run --reload app/app.py
```
La aplicacion estara disponible en el navegador web en `http://127.0.0.1:8000`.
