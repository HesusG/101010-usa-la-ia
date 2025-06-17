# 🚀 Ejecutando el Dashboard con Streamlit

Este documento explica cómo ejecutar el dashboard interactivo de análisis de pingüinos con IA.

## Requisitos Previos

Asegúrate de haber configurado tu entorno siguiendo las instrucciones en `configuracion.md`. En resumen:

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Configura tu API key de OpenAI:
   - Crea un archivo `.env` a partir de `.env.example`
   - Añade tu API key de OpenAI

## Instalar Streamlit

Si aún no has instalado Streamlit (no viene incluido en requirements.txt), puedes hacerlo con:

```bash
pip install streamlit
```

## Ejecutar la Aplicación

1. Navega a la carpeta raíz del proyecto:
   ```bash
   cd ruta/a/101010-usa-la-ia
   ```

2. Ejecuta la aplicación con el siguiente comando:
   ```bash
   streamlit run app.py
   ```

3. La aplicación se abrirá automáticamente en tu navegador predeterminado. Si no se abre, puedes acceder manualmente en la URL que aparece en la terminal (generalmente http://localhost:8501).

## Funcionalidades del Dashboard

El dashboard ofrece las siguientes características:

### 🔍 Filtros
- Selecciona especies específicas de pingüinos
- Filtra por islas

### 📊 Visualizaciones
- **Scatter Plot**: Muestra la relación entre longitud de aleta y masa corporal
- **Box Plot**: Visualiza la distribución de masa corporal por especie
- **Violin Plot**: Compara la distribución de longitud de aleta entre especies
- **Pair Plot**: Visualiza las relaciones entre todas las variables numéricas

### 🤖 Análisis con IA
- **Descripción de Especies**: Obtén información detallada sobre cada especie de pingüino
- **Generación de Insights**: Analiza automáticamente los datos filtrados para descubrir patrones interesantes
- **Preguntas sobre Datos**: Haz preguntas en lenguaje natural sobre los pingüinos

## Solución de Problemas

### API Key no configurada
Si ves mensajes de error relacionados con la API key:
1. Verifica que hayas creado correctamente el archivo `.env`
2. Asegúrate de haber copiado correctamente tu API key de OpenAI
3. Reinicia la aplicación después de configurar la API key

### Errores de importación
Si encuentras errores de importación de módulos:
1. Verifica que todas las dependencias estén instaladas:
   ```bash
   pip install -r requirements.txt
   ```
2. Asegúrate de estar usando la misma versión de Python con la que instalaste las dependencias

### Problemas de visualización
Si los gráficos no se muestran correctamente:
1. Intenta con un conjunto de datos diferente (cambiando los filtros)
2. Verifica que matplotlib y seaborn estén correctamente instalados