"""
config.py

Autor: Álvaro Cortés González  
Universidad: Escuela Politécnica Superior de Córdoba  
Trabajo Fin de Grado - Automatización en la Evaluación de Riesgos en Maquinaria a Partir de Imágenes Mediante Técnicas de IA  
Fecha: Junio 2025

Descripción:
    Archivo de configuración global del sistema. Define rutas clave utilizadas por
    todos los módulos, así como parámetros de ejecución como el modo de simulación.
"""

import os

# === RUTAS DEL SISTEMA ===

# Ruta base del proyecto (directorio donde se encuentra este archivo)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta a la carpeta que contiene las imágenes de entrada
IMAGENES_DIR = os.path.join(BASE_DIR, "imagenes")

# Subcarpeta donde se colocan las imágenes que aún no han sido analizadas
SIN_ETIQUETAR_DIR = os.path.join(IMAGENES_DIR, "sin_etiquetar")

# Subcarpeta para imágenes modificadas o preprocesadas
PREPROCESADAS_DIR = os.path.join(IMAGENES_DIR, "preprocesadas")

# Ruta a la carpeta donde se guardan los resultados del análisis
RESULTADOS_DIR = os.path.join(BASE_DIR, "resultados")

# Archivo donde opcionalmente se pueden guardar predicciones en formato JSON
PREDICCIONES_JSON = os.path.join(RESULTADOS_DIR, "predicciones.json")

# Carpeta de informes generados en formato DOCX
INFORMES_DIR = os.path.join(BASE_DIR, "informes")

# (Obsoleto) Archivo de informe en formato texto simple
INFORME_TXT = os.path.join(INFORMES_DIR, "informe.txt")

# === OTROS PARÁMETROS ===

# Modo simulación: si está activado, usa el modelo simulado en lugar del real
MODO_SIMULACION = True

# Nombre general de la aplicación (para interfaces u otras etiquetas)
NOMBRE_APLICACION = "Evaluador de Riesgos con IA"
