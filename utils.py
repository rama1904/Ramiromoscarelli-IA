import streamlit as pd

def load_tasks(file_path):
    """Carga las tareas desde un archivo CSV."""
    return pd.read_csv(file_path)

def optimize_tasks(tasks):
    """Optimiza las tareas según prioridad y fecha límite."""
    # Ordenar por prioridad y fecha
    return tasks.sort_values(by=['Prioridad', 'Fecha Límite'])