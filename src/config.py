"""Configuración global de rutas, parámetros y endpoints SODA."""
from pathlib import Path

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
GEO_DATA_DIR = DATA_DIR / "geo"

# Endpoints SODA (Datos Abiertos Colombia)
API_ENDPOINTS = {
    "rnt": "https://www.datos.gov.co/resource/thwd-ivmp.json",
    "divipola": "https://www.datos.gov.co/resource/gdxc-w37w.json",
    "extranjeros": "https://www.datos.gov.co/resource/7wm8-w5ad.json",
    "transporte_aereo": "https://www.datos.gov.co/resource/gb6w-ynu4.json",
}

# Parámetros por defecto para descarga por API
DEFAULT_LIMIT = 50000
TIMEOUT_SECONDS = 60

# Configuración de modelos K-Means
RANDOM_STATE = 42
K_RANGE = range(2, 9)
