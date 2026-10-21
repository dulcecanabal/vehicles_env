# Análisis de Vehículos Usados en Estados Unidos de América 

## Descripción del Proyecto
Esta aplicación web interactiva permite explorar y analizar un conjunto de datos sobre anuncios de venta de vehículos usados en los Estados Unidos. La web está diseñada para facilitar la visualización rápida de variables clave como el kilometraje (*odometer*) y el precio (*price*), lo cual ayuda a identificar patrones y distribuciones en el mercado automotriz.

## Funcionalidades
- Una de las funcionalidades es que permite generar un histograma interactivo del kilometraje (*odometer*) mediante una casilla de verificación para analizar la distribución del uso de los vehículos.
- Contiene la opción de construir un gráfico de dispersión interactivo entre el kilometraje y el precio para observar cómo el recorrido del auto impacta en su valor de venta.
- De igual manera, se presentan filtros dinámicos mediante componentes interactivos de Streamlit y gráficos construidos con Plotly.

## Comandos necesarios para el proyecto:
- python -m venv .venv: Se crea el entorno virtual.
- .venv\Scripts\Activate.ps1: Activa el entorno virtual en Windows PowerShell.
- pip install --upgrade pip: Actualiza el gestor de paquetes de Python.
- pip install -r requirements.txt: Instala las librerías necesarias que contiene el archivo txt.
- streamlit run app.py: Ejecuta la aplicación web.
- git status: Ayuda a verificar el estado de los archivos en el repositorio.
- git add: Agrega todos los archivos modificados al área de preparación.
- git commit -m "Mensaje descriptivo": Guarda los cambios en el historial de Git.
- git push origin main: Sube los commits locales al repositorio remoto en GitHub.
- git pull origin main: Descarga e integra la versión más reciente desde GitHub.

## Paso para crear e instalar el entorno virtual:
- python -m venv .venv
- .venv\Scripts\Activate.ps1
## Actualiza pip y las librerias necesarias:
- pip install --upgrade pip
- pip install -r requirements.txt

## Ejecuta la app
- streamlit run app.py

## Liga de la prueba: 
- https://web-app-vehicles-env.onrender.com/
