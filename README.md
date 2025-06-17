# 🚀 Usa la IA: Guía Práctica para No-Técnicos

Este repositorio es un recurso educativo para personas no técnicas que desean aprender a utilizar la Inteligencia Artificial clásica y moderna (OpenAI) de forma práctica y sencilla.

## 🎯 Objetivos

- Explicar conceptos de IA de forma clara y visual
- Mostrar ejemplos prácticos de IA clásica con scikit-learn
- Enseñar cómo utilizar la API de OpenAI desde Python
- Demostrar aplicaciones prácticas para enriquecer datos con IA

## 📁 Estructura del Repositorio

- `/notebooks`: Jupyter Notebooks con ejemplos prácticos y explicaciones
  - `1_ia_clasica.ipynb`: Ejemplos de regresión logística y visualización
  - `2_openai_python.ipynb`: Cómo conectarse y usar la API de OpenAI
  - `3_enriquecimiento_ia.ipynb`: Ejemplos de enriquecimiento de datos con IA

- `/docs`: Documentación adicional y guías
  - `configuracion.md`: Guía para configurar tu entorno
  - `recursos_adicionales.md`: Referencias y recursos para aprender más
  - `ejecutar_streamlit.md`: Instrucciones para ejecutar el dashboard interactivo

- `app.py`: Aplicación Streamlit para análisis interactivo de pingüinos con IA
- `.env.example`: Plantilla para configurar tus credenciales de API

## 🚀 Cómo Empezar

1. Clona este repositorio
2. Copia `.env.example` a `.env` y añade tu API key de OpenAI
3. Instala las dependencias con `pip install -r requirements.txt`
4. Explora los notebooks en orden numérico
5. Ejecuta el dashboard interactivo con `streamlit run app.py`

## 📊 Dashboard Interactivo

Este repositorio incluye una aplicación Streamlit que te permite:
- Explorar visualmente los datos de pingüinos
- Filtrar por especies e islas
- Generar descripciones de especies con IA
- Obtener insights automáticos sobre los datos
- Hacer preguntas en lenguaje natural sobre los pingüinos

Para ejecutar el dashboard, sigue las instrucciones en `docs/ejecutar_streamlit.md`.

## 📚 Requisitos

- Python 3.8+
- Jupyter Notebook o JupyterLab
- Paquetes Python: scikit-learn, pandas, matplotlib, seaborn, openai, python-dotenv, streamlit

---

Desarrollado con ❤️ para hacer la IA accesible a todos.