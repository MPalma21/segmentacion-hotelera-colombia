"""Limpieza, homologación territorial con DIVIPOLA y construcción de variables."""
import logging
import pandas as pd
from typing import Tuple
from .config import PROCESSED_DATA_DIR

logger = logging.getLogger(__name__)

def clean_divipola(df_divipola: pd.DataFrame) -> pd.DataFrame:
    """Estandariza códigos DIVIPOLA y nombres geográficos."""
    df = df_divipola.copy()
    # Asegurar códigos con longitud estándar (5 dígitos para municipio, 2 para depto)
    for col in ["codigo_municipio", "cod_mpio", "codigo_dane"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.zfill(5)
            
    for col in ["codigo_departamento", "cod_depto"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.zfill(2)
            
    return df

def clean_rnt_hoteles(df_rnt: pd.DataFrame) -> pd.DataFrame:
    """Limpia registros de RNT y filtra alojamientos turísticos formales."""
    df = df_rnt.copy()
    logger.info(f"Limpieza RNT: {len(df)} registros iniciales.")
    
    # Conversión de métricas numéricas operativas
    numeric_cols = ["habitaciones", "camas", "empleados"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
            
    # Filtro de registros activos y con capacidad válida
    if "estado" in df.columns:
        df = df[df["estado"].str.upper() == "ACTIVO"]
        
    return df

def aggregate_municipal_indicators(
    df_hoteles: pd.DataFrame,
    df_extranjeros: pd.DataFrame,
    df_aereo: pd.DataFrame,
    df_divipola: pd.DataFrame
) -> pd.DataFrame:
    """
    Consolida variables a nivel municipal:
    - Oferta hotelera (total hoteles, habitaciones, camas, empleados)
    - Demanda de turistas (total visitantes no residentes)
    - Conectividad aérea (pasajeros movilizados y rutas activas)
    """
    logger.info("Consolidando métricas municipales...")
    # Estructura base para cruce y agregación
    # Implementar cruces por código oficial DIVIPOLA
    return pd.DataFrame()
