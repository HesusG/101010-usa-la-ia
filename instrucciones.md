# Instrucciones para configurar el ambiente y ejecutar la aplicación

Sigue estos pasos para configurar tu entorno y ejecutar la aplicación de análisis de pingüinos con IA:

## 1. Crear y activar un ambiente virtual

```bash
# Crear el ambiente virtual
python -m venv venv

# Activar el ambiente virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

## 2. Instalar dependencias

```bash
# Instalar las dependencias principales
pip install numpy pandas matplotlib seaborn scikit-learn streamlit
pip install openai python-dotenv

# Alternativamente, puedes instalar todas las dependencias desde requirements.txt
pip install -r requirements.txt
```

## 3. Configurar la API key de OpenAI

1. Crea un archivo `.env` en el directorio raíz basado en `.env.example`:
   ```bash
   cp .env.example .env
   ```

2. Edita el archivo `.env` y reemplaza `tu_api_key_aqui` con tu API key real de OpenAI:
   ```
   OPENAI_API_KEY=tu_api_key_aqui
   ```

## 4. Ejecutar la aplicación Streamlit

```bash
# Ejecutar la aplicación
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador web. Si no se abre, puedes acceder manualmente en la URL que aparece en la terminal (generalmente http://localhost:8501).

## 5. Explorar los Jupyter Notebooks

También puedes explorar los notebooks para aprender más sobre IA clásica y moderna:

```bash
# Iniciar Jupyter Notebook
jupyter notebook
```

Navega a la carpeta `/notebooks` y abre los notebooks en orden numérico:
1. `1_ia_clasica.ipynb`: Regresión logística y visualización con scikit-learn
2. `2_openai_python.ipynb`: Uso de la API de OpenAI desde Python
3. `3_enriquecimiento_ia.ipynb`: Enriquecimiento de datos con IA

## Solución de problemas

Si encuentras errores al instalar las dependencias o ejecutar la aplicación:

1. **Problemas con la instalación de paquetes**:
   ```bash
   # Intenta actualizar pip primero
   pip install --upgrade pip
   
   # Luego instala las dependencias
   pip install -r requirements.txt
   ```

2. **Error con OpenAI API key**:
   - Verifica que el archivo `.env` esté correctamente configurado
   - Asegúrate de que tu API key sea válida

3. **Problemas con Streamlit**:
   - Intenta instalar Streamlit por separado: `pip install streamlit`
   - Ejecuta `streamlit hello` para verificar que Streamlit funciona correctamente

Para obtener más información, consulta la documentación en la carpeta `/docs`.