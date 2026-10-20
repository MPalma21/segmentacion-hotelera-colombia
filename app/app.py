"""Aplicación interactiva Shiny for Python para la exploración de segmentos hoteleros y territoriales."""
from pathlib import Path
import pandas as pd
from shiny import App, render, ui
from shinywidgets import output_widget, render_widget
import plotly.express as px

# Directorio de datos procesados
DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"

# Definición de Interfaz de Usuario (UI)
app_ui = ui.page_navbar(
    ui.nav_panel(
        "🗺️ Mapa Territorial",
        ui.layout_sidebar(
            ui.sidebar(
                ui.h4("Filtros Territoriales"),
                ui.input_select(
                    "depto_select",
                    "Departamento:",
                    choices=["TODOS", "ANTIOQUIA", "BOGOTA D.C.", "BOLIVAR", "VALLE DEL CAUCA"],
                    selected="TODOS"
                ),
                ui.input_checkbox_group(
                    "cluster_select",
                    "Clústeres Municipales:",
                    choices={"0": "Alta Demanda y Alta Oferta", "1": "Mercado Emergente", "2": "Escala Local"},
                    selected=["0", "1", "2"]
                ),
                ui.hr(),
                ui.help_text("Filtre por departamento y clúster para visualizar la distribución geográfica de oferta y demanda.")
            ),
            ui.card(
                ui.card_header("Distribución Espacial de Segmentos"),
                output_widget("mapa_interactivo")
            )
        )
    ),
    ui.nav_panel(
        "📊 Perfiles de Clústeres",
        ui.layout_columns(
            ui.card(
                ui.card_header("Oferta vs. Demanda Turística"),
                output_widget("scatter_oferta_demanda")
            ),
            ui.card(
                ui.card_header("Distribución de Capacidad Operativa"),
                output_widget("barras_capacidad")
            )
        )
    ),
    ui.nav_panel(
        "🏨 Directorio Priorizado de Hoteles",
        ui.card(
            ui.card_header("Listado de Establecimientos Segmentados"),
            ui.output_table("tabla_hoteles")
        )
    ),
    title="Plataforma de Segmentación Hotelera y Territorial en Colombia",
    fillable=True
)

# Servidor (Lógica reactiva)
def server(input, output, session):
    
    @render_widget
    def mapa_interactivo():
        # Gráfico inicial de dispersión geográfica en Plotly (o ipyleaflet Map)
        df_dummy = pd.DataFrame({
            "ciudad": ["Bogotá", "Medellín", "Cartagena", "Cali"],
            "lat": [4.7110, 6.2442, 10.3910, 3.4516],
            "lon": [-74.0721, -75.5812, -75.4794, -76.5320],
            "cluster": ["Alta Demanda", "Alta Demanda", "Alta Demanda", "Emergente"],
            "hoteles": [1200, 850, 650, 420]
        })
        fig = px.scatter_geo(
            df_dummy,
            lat="lat",
            lon="lon",
            hover_name="ciudad",
            size="hoteles",
            color="cluster",
            scope="south america",
            title="Municipios y Polos Hoteleros en Colombia"
        )
        fig.update_geos(fitbounds="locations")
        return fig

    @render_widget
    def scatter_oferta_demanda():
        df_dummy = pd.DataFrame({
            "oferta_camas": [1000, 2500, 5000, 8000, 15000, 30000],
            "turistas_extranjeros": [500, 3000, 12000, 25000, 90000, 250000],
            "municipio": ["San Gil", "Villa de Leyva", "Santa Marta", "Cali", "Medellín", "Bogotá"],
            "cluster": ["Emergente", "Emergente", "Consolidado", "Consolidado", "Alta Demanda", "Alta Demanda"]
        })
        fig = px.scatter(
            df_dummy,
            x="oferta_camas",
            y="turistas_extranjeros",
            color="cluster",
            hover_name="municipio",
            log_x=True,
            log_y=True,
            title="Relación Oferta Hotelera vs. Flujo Internacional"
        )
        return fig

    @render_widget
    def barras_capacidad():
        df_dummy = pd.DataFrame({
            "cluster": ["Clúster 0", "Clúster 1", "Clúster 2"],
            "promedio_habitaciones": [18, 55, 140]
        })
        fig = px.bar(
            df_dummy,
            x="cluster",
            y="promedio_habitaciones",
            color="cluster",
            title="Promedio de Habitaciones por Segmento Hotelero"
        )
        return fig

    @render.table
    def tabla_hoteles():
        return pd.DataFrame({
            "Nombre RNT": ["Hotel Ejemplo 1", "Hotel Ejemplo 2", "Hotel Ejemplo 3"],
            "Municipio": ["Cartagena", "Medellín", "Bogotá"],
            "Habitaciones": [45, 120, 210],
            "Camas": [90, 180, 320],
            "Segmento Operativo": ["Escala Media", "Gran Escala", "Cadena Corporativa"]
        })

app = App(app_ui, server)
