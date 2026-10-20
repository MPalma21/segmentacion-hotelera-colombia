"""Funciones para la extracción y descarga de datos desde APIs SODA."""
import logging
import requests
import pandas as pd
from typing import Optional, Dict, Any
from .config import API_ENDPOINTS, DEFAULT_LIMIT, TIMEOUT_SECONDS, RAW_DATA_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def fetch_soda_dataset(
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    limit: int = DEFAULT_LIMIT,
    max_records: Optional[int] = None,
    app_token: Optional[str] = None
) -> pd.DataFrame:
    """
    Descarga registros desde una API SODA de Socrata gestionando paginación.
    
    Args:
        endpoint: URL del endpoint JSON SODA.
        params: Parámetros opcionales para la consulta ($where, $select, etc.).
        limit: Tamaño de página por solicitud.
        max_records: Máximo número total de registros a descargar (None para todos).
        app_token: Token de aplicación opcional de datos.gov.co.
        
    Returns:
        pd.DataFrame con los registros descargados.
    """
    headers = {}
    if app_token:
        headers["X-App-Token"] = app_token

    base_params = params.copy() if params else {}
    base_params["$limit"] = limit
    
    offset = 0
    all_chunks = []
    
    logger.info(f"Iniciando descarga desde endpoint: {endpoint}")
    
    while True:
        base_params["$offset"] = offset
        try:
            response = requests.get(endpoint, params=base_params, headers=headers, timeout=TIMEOUT_SECONDS)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            logger.error(f"Error consultando endpoint en offset {offset}: {e}")
            raise
        
        if not data:
            break
            
        chunk_df = pd.DataFrame(data)
        all_chunks.append(chunk_df)
        records_fetched = len(chunk_df)
        logger.info(f"Descargados {records_fetched} registros (offset={offset}).")
        
        offset += records_fetched
        
        if records_fetched < limit:
            break
        if max_records and offset >= max_records:
            break
            
    if not all_chunks:
        return pd.DataFrame()
        
    df = pd.concat(all_chunks, ignore_index=True)
    logger.info(f"Descarga finalizada. Total registros: {len(df)}")
    return df

def save_raw_dataset(df: pd.DataFrame, filename: str) -> None:
    """Guarda dataset crudo en formato Parquet."""
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RAW_DATA_DIR / filename
    df.to_parquet(output_path, index=False)
    logger.info(f"Dataset guardado en {output_path}")
