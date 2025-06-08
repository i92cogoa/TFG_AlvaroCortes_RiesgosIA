"""
preprocesador.py

Autor: Álvaro Cortés González  
Universidad: Escuela Politécnica Superior de Córdoba  
Trabajo Fin de Grado - Automatización en la Evaluación de Riesgos en Maquinaria a Partir de Imágenes Mediante Técnicas de IA  
Fecha: Junio 2025

Descripción:
    Este módulo contiene la función de preprocesado de imágenes antes de su
    análisis por parte del modelo de IA. Actualmente funciona como una función
    simulada, lista para ser ampliada con operaciones reales como redimensionado
    o normalización.
"""

from utils.logger import logger


def preprocesar_imagen(path_imagen):
    """
    Simula el preprocesado de una imagen.
    
    Parámetros:
    - path_imagen: ruta del archivo de imagen a procesar.

    Retorna:
    - La misma ruta sin modificaciones (simulación).
    """
    logger.info(f"Preprocesando imagen: {path_imagen}")
    
    # En una versión futura, aquí se aplicaría redimensionado, normalización, etc.
    return path_imagen
