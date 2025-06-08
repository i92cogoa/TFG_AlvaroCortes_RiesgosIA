"""
yolo_simulado.py

Autor: Álvaro Cortés González  
Universidad: Escuela Politécnica Superior de Córdoba  
Trabajo Fin de Grado - Automatización en la Evaluación de Riesgos en Maquinaria a Partir de Imágenes Mediante Técnicas de IA  
Fecha: Junio 2025

Descripción:
    Este módulo representa una versión de simulación del sistema de detección.
    Fue utilizado durante las primeras fases de desarrollo del proyecto, antes de
    contar con un modelo de IA entrenado, para probar la lógica y la interfaz gráfica.
"""

from utils.logger import logger
import random


def analizar_imagen(path_imagen):
    """
    Simula el análisis de una imagen, generando una detección aleatoria.

    Parámetros:
    - path_imagen: ruta de la imagen a analizar (no se usa realmente en este modo).

    Retorna:
    - diccionario con:
        - riesgo_detectado: True o False
        - tipo: tipo de fallo aleatorio
        - confianza: valor aleatorio entre 0.70 y 0.99
    """

    logger.info(f"Analizando imagen con modelo simulado: {path_imagen}")

    prediccion = {
        "riesgo_detectado": random.choice([True, False]),
        "tipo": random.choice(["fuga", "desgaste", "oxidación", "ninguno"]),
        "confianza": round(random.uniform(0.7, 0.99), 2)
    }

    logger.info(f"Resultado simulado: {prediccion}")
    return prediccion
