import streamlit as st
from Utils.main import get_productivity_plan # type: ignore

st.title("OptiTime AI")

st.markdown("""
    <hr>
    <h2>Asistente de Productividad con IA</h2>
    <ol>
        <li>Ingresa tus tareas diarias con su fecha límite y nivel de prioridad.</li>
        <li>Haz clic en "Generar Plan de Trabajo" para obtener un cronograma optimizado.</li>
        <li>Sigue las recomendaciones para mejorar tu productividad.</li>
    </ol>
""", unsafe_allow_html=True)

# Input de tareas
tasks_input = st.text_area("Ingresa tus tareas en el siguiente formato: Tarea - Fecha límite (AAAA-MM-DD) - Prioridad (Alta, Media, Baja)",
                           "Preparar informe - 2025-02-15 - Alta\nRevisar correos - 2025-02-12 - Media")

# Disponibilidad diaria
availability = st.slider("Horas disponibles por día para trabajar en tus tareas", min_value=1, max_value=12, value=4)

# Botón para generar el plan de trabajo
if st.button("Generar Plan de Trabajo"):
    full_input = f"Tareas:\n{tasks_input}\nDisponibilidad diaria: {availability} horas"
    productivity_plan = get_productivity_plan(full_input)  # Llamar a la función para generar el plan
    st.write(productivity_plan)
