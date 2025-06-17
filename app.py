import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import openai
import os
import json
from dotenv import load_dotenv

# Configuración inicial
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
st.set_page_config(page_title="Análisis de Pingüinos con IA", layout="wide")

# Título y descripción
st.title("🐧 Análisis de Pingüinos Enriquecido con IA")
st.write("Explora datos de pingüinos con ayuda de inteligencia artificial generativa")

# Función para consultar a la API de OpenAI
def consultar_openai(prompt, temperatura=0.7, max_tokens=250):
    """Realiza una consulta a la API de OpenAI"""
    try:
        if not openai.api_key:
            return "⚠️ API key no configurada. Verifica tu archivo .env"
            
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperatura,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error al consultar la API: {str(e)}"

# Función para generar descripción de una especie
def generar_descripcion_especie(especie):
    prompt = f"""
    Genera una descripción detallada del pingüino {especie} que incluya:
    1. Características físicas principales
    2. Hábitat y distribución geográfica
    3. Comportamiento y alimentación
    4. Estado de conservación
    
    Formato: párrafo conciso de 100-150 palabras.
    """
    return consultar_openai(prompt)

# Función para extraer insights
def extraer_insights(datos_filtrados):
    # Preparamos un resumen de los datos para el prompt
    resumen = datos_filtrados.describe().round(2)
    conteo_especies = datos_filtrados['species'].value_counts()
    
    # Calculamos correlaciones si hay suficientes datos
    correlaciones = ""
    if len(datos_filtrados) > 5:
        correlaciones = datos_filtrados.corr().round(2).to_string()
    
    prompt = f"""
    Analiza estos datos de pingüinos y proporciona 3 insights interesantes:
    
    Conteo de especies:
    {conteo_especies.to_string()}
    
    Estadísticas descriptivas:
    {resumen.to_string()}
    
    {correlaciones}
    
    Proporciona exactamente 3 insights breves y específicos basados en estos datos.
    """
    
    respuesta = consultar_openai(prompt)
    
    # Dividimos la respuesta en insights individuales
    insights = []
    for linea in respuesta.split('\n'):
        if linea.strip() and not linea.startswith('Insight'):
            insights.append(linea.strip())
    
    # Aseguramos que haya al menos un insight
    if not insights:
        insights = ["No se pudieron generar insights con los datos filtrados."]
    
    return insights[:3]  # Limitamos a 3 insights

# Función para responder preguntas
def responder_pregunta(pregunta, datos_filtrados):
    # Preparamos un resumen de los datos para el contexto
    resumen = datos_filtrados.describe().round(2)
    conteo_especies = datos_filtrados['species'].value_counts()
    
    prompt = f"""
    Basado en estos datos de pingüinos:
    
    Conteo de especies:
    {conteo_especies.to_string()}
    
    Estadísticas descriptivas:
    {resumen.to_string()}
    
    Responde la siguiente pregunta de manera breve y clara:
    {pregunta}
    """
    
    return consultar_openai(prompt, temperatura=0.2)

# Cargamos datos
@st.cache_data
def cargar_datos():
    return sns.load_dataset("penguins")

penguins = cargar_datos()
penguins_clean = penguins.dropna().reset_index(drop=True)

# Sidebar para filtros
st.sidebar.header("Filtros")
selected_species = st.sidebar.multiselect(
    "Especies", 
    penguins_clean['species'].unique(), 
    default=penguins_clean['species'].unique()
)
selected_island = st.sidebar.multiselect(
    "Islas", 
    penguins_clean['island'].unique(), 
    default=penguins_clean['island'].unique()
)

# Verificamos que haya selecciones válidas
if not selected_species:
    selected_species = penguins_clean['species'].unique()
if not selected_island:
    selected_island = penguins_clean['island'].unique()

# Filtramos datos
filtered_data = penguins_clean[
    penguins_clean['species'].isin(selected_species) &
    penguins_clean['island'].isin(selected_island)
]

# Columnas principales
col1, col2 = st.columns([3, 2])

with col1:
    st.header("Visualización de Datos")
    
    # Selector de visualización
    chart_type = st.selectbox(
        "Selecciona tipo de gráfico", 
        ["Scatter Plot", "Box Plot", "Violin Plot", "Pair Plot"]
    )
    
    # Mostramos número de pingüinos filtrados
    st.write(f"Mostrando datos de {len(filtered_data)} pingüinos")
    
    # Generamos el gráfico seleccionado
    try:
        if chart_type == "Scatter Plot":
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.scatterplot(
                x='flipper_length_mm', 
                y='body_mass_g', 
                hue='species', 
                size='bill_length_mm',
                sizes=(20, 200), 
                alpha=0.8, 
                data=filtered_data, 
                ax=ax
            )
            plt.title('Relación entre Longitud de Aleta y Masa Corporal')
            st.pyplot(fig)
            
        elif chart_type == "Box Plot":
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(x='species', y='body_mass_g', data=filtered_data, ax=ax)
            plt.title('Distribución de Masa Corporal por Especie')
            st.pyplot(fig)
            
        elif chart_type == "Violin Plot":
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.violinplot(x='species', y='flipper_length_mm', data=filtered_data, ax=ax)
            plt.title('Distribución de Longitud de Aleta por Especie')
            st.pyplot(fig)
            
        elif chart_type == "Pair Plot":
            if len(filtered_data) > 0:
                fig = sns.pairplot(filtered_data, hue='species', height=2.5)
                plt.suptitle('Relaciones entre Variables por Especie', y=1.02)
                st.pyplot(fig)
            else:
                st.warning("No hay suficientes datos para generar un Pair Plot.")
                
    except Exception as e:
        st.error(f"Error al generar el gráfico: {str(e)}")

with col2:
    st.header("Análisis con IA")
    
    # Advertencia sobre API key
    if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY") == "tu_api_key_aqui":
        st.warning("⚠️ API key no configurada. Las funciones de IA no estarán disponibles.")
    
    # Si el usuario selecciona una sola especie, mostramos su descripción
    if len(selected_species) == 1:
        st.subheader(f"Sobre los pingüinos {selected_species[0]}")
        
        # Utilizamos la session_state para guardar en caché las descripciones
        if "descripciones" not in st.session_state:
            st.session_state.descripciones = {}
            
        if selected_species[0] not in st.session_state.descripciones and os.getenv("OPENAI_API_KEY") and os.getenv("OPENAI_API_KEY") != "tu_api_key_aqui":
            with st.spinner("Generando descripción con IA..."):
                descripcion = generar_descripcion_especie(selected_species[0])
                st.session_state.descripciones[selected_species[0]] = descripcion
        
        if selected_species[0] in st.session_state.descripciones:
            st.write(st.session_state.descripciones[selected_species[0]])
        else:
            st.info("Configura tu API key de OpenAI en el archivo .env para ver la descripción generada por IA.")
    
    # Botón para generar insights sobre los datos filtrados
    if os.getenv("OPENAI_API_KEY") and os.getenv("OPENAI_API_KEY") != "tu_api_key_aqui":
        if st.button("Generar insights con IA"):
            if len(filtered_data) > 0:
                with st.spinner("El modelo está analizando los datos..."):
                    insights = extraer_insights(filtered_data)
                    
                    for insight in insights:
                        st.info(insight)
            else:
                st.warning("No hay datos suficientes para generar insights.")
    
    # Cuadro de texto para preguntas del usuario
    st.subheader("Pregunta sobre los datos")
    user_question = st.text_input("Haz una pregunta sobre los pingüinos:")
    
    if user_question and os.getenv("OPENAI_API_KEY") and os.getenv("OPENAI_API_KEY") != "tu_api_key_aqui":
        if len(filtered_data) > 0:
            with st.spinner("Procesando tu pregunta..."):
                response = responder_pregunta(user_question, filtered_data)
                st.success(response)
        else:
            st.warning("No hay datos suficientes para responder preguntas.")
    elif user_question:
        st.info("Configura tu API key de OpenAI en el archivo .env para usar esta función.")
        
    # Mostramos una tabla con los datos filtrados
    st.subheader("Datos Filtrados")
    st.dataframe(filtered_data.head(10) if len(filtered_data) > 10 else filtered_data)