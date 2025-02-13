import streamlit as st  
import pandas as pd # type: ignore
from datetime import datetime

# Función para optimizar las tareas
def optimize_tasks(tasks):
    # Ordenar por prioridad y fecha
    priority_map = {'Alta': 1, 'Media': 2, 'Baja': 3}
    tasks['Prioridad_Num'] = tasks['Prioridad'].map(priority_map)
    return tasks.sort_values(by=['Prioridad_Num', 'Fecha Límite'])

# Título de la aplicación
st.title("Asistente de Productividad con IA")

# Descripción de la aplicación
st.write("""
En la vida cotidiana, muchas personas tienen dificultades para organizar y priorizar sus tareas de manera eficiente. 
Esta aplicación te ayuda a organizar tus actividades diarias, generando un plan de trabajo optimizado.
""")    

# Entrada de datos: lista de tareas
st.header("Ingresa tus tareas")
task_data = st.text_area("Formato: Tarea, Fecha Límite (YYYY-MM-DD), Prioridad (Alta, Media, Baja)")

# Botón de acción
if st.button("Generar Plan de Trabajo"):
    # Procesar las tareas
    tasks = []
    for line in task_data.split('\n'):
        if line.strip():
            try:
                task, deadline, priority = line.split(',')
                tasks.append({
                    'Tarea': task.strip(),
                    'Fecha Límite': datetime.strptime(deadline.strip(), '%Y-%m-%d'),
                    'Prioridad': priority.strip()
                })
            except ValueError:
                st.error("Por favor, asegúrate de que cada línea siga el formato correcto.")
                break
    
    if tasks:
        # Convertir a DataFrame
        df_tasks = pd.DataFrame(tasks)
        
        # Optimizar las tareas
        optimized_tasks = optimize_tasks(df_tasks)
        
        # Mostrar el plan de trabajo
        st.subheader("Plan de Trabajo Optimizado")
        st.table(optimized_tasks[['Tarea', 'Fecha Límite', 'Prioridad']])

# Sección "Cómo Funciona"
st.header("Cómo Funciona")
st.write("""
- **Optimización Automática**: La aplicación organiza tus tareas según prioridad y fecha límite.
- **Recomendaciones Personalizadas**: Recibe consejos para mejorar tu gestión del tiempo.
- **Interfaz Intuitiva**: Fácil de usar, solo ingresa tus tareas y genera el plan.
""")