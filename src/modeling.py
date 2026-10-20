"""Modelado no supervisado con K-Means y validación de estabilidad."""
import logging
import numpy as np
import pandas as pd
from typing import Dict, Any, Tuple
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from .config import RANDOM_STATE, K_RANGE

logger = logging.getLogger(__name__)

def evaluate_kmeans_range(
    X_scaled: np.ndarray,
    k_range = K_RANGE
) -> pd.DataFrame:
    """
    Evalúa múltiples valores de k calculando Inercia y Silhouette Score.
    
    Returns:
        pd.DataFrame con columnas ['k', 'inertia', 'silhouette_score']
    """
    results = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
        labels = kmeans.fit_predict(X_scaled)
        sil = silhouette_score(X_scaled, labels)
        results.append({
            "k": k,
            "inertia": kmeans.inertia_,
            "silhouette_score": sil
        })
        logger.info(f"K={k} -> Inercia: {kmeans.inertia_:.2f}, Silhouette: {sil:.4f}")
        
    return pd.DataFrame(results)

def fit_final_kmeans(
    X_scaled: np.ndarray,
    n_clusters: int
) -> Tuple[KMeans, np.ndarray]:
    """Entrena el modelo K-Means final con el k seleccionado."""
    model = KMeans(n_clusters=n_clusters, random_state=RANDOM_STATE, n_init=20)
    labels = model.fit_predict(X_scaled)
    return model, labels

def profile_clusters(df: pd.DataFrame, cluster_col: str, feature_cols: list) -> pd.DataFrame:
    """Calcula estadísticas descriptivas (media, mediana) por clúster."""
    return df.groupby(cluster_col)[feature_cols].agg(["count", "mean", "median"])
