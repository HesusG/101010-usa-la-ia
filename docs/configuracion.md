# 🔧 Configuración del Entorno

## Requisitos Previos

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)

## Instalación de Dependencias

Ejecuta el siguiente comando para instalar todas las bibliotecas necesarias:

```bash
pip install scikit-learn pandas matplotlib seaborn openai python-dotenv jupyter
```

## Configuración de la API de OpenAI

1. Crea una cuenta en [OpenAI](https://platform.openai.com/)
2. Genera una API key en la sección de [API Keys](https://platform.openai.com/account/api-keys)
3. Copia el archivo `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
4. Edita el archivo `.env` y reemplaza `tu_api_key_aqui` con tu API key real

## Ejecutando los Notebooks

1. Inicia Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Navega hasta la carpeta `/notebooks`
3. Abre los notebooks en orden numérico para seguir el curso completo