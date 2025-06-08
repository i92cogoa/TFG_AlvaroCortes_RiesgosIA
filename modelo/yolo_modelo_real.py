"""
yolo_modelo_real.py

Autor: Álvaro Cortés González  
Universidad: Escuela Politécnica Superior de Córdoba  
Trabajo Fin de Grado - Automatización en la Evaluación de Riesgos en Maquinaria a Partir de Imágenes Mediante Técnicas de IA  
Fecha: Junio 2025

Descripción:
    Este módulo carga el modelo YOLOv8 previamente entrenado y permite analizar
    imágenes para detectar fallos de seguridad. Devuelve tanto las detecciones 
    estructuradas como la imagen marcada con bounding boxes.
"""

from ultralytics import YOLO
from utils.logger import logger
import cv2
from PIL import Image
import numpy as np

# Cargar el modelo entrenado desde la ruta definida
modelo = YOLO("modelo/pesos_entrenados.pt")


def analizar_imagen(path_imagen):
    """
    Analiza una imagen con el modelo YOLOv8 cargado.

    Parámetros:
    - path_imagen: ruta del archivo de imagen a analizar.

    Retorna:
    - detecciones: lista de diccionarios con clase, confianza y bounding box.
    - imagen_pil: imagen en formato PIL marcada con las detecciones.
    """

    logger.info(f"Analizando imagen: {path_imagen}")
    
    # Realiza la inferencia sobre la imagen
    resultados = modelo(path_imagen)
    detecciones = []

    for r in resultados:
        for caja in r.boxes:
            clase_id = int(caja.cls[0])                # ID de la clase detectada
            confianza = float(caja.conf[0])            # Confianza del modelo en la predicción
            bbox = caja.xyxy[0].tolist()               # Coordenadas de la caja en formato [x1, y1, x2, y2]
            nombre_clase = modelo.names[clase_id]      # Nombre de la clase a partir del ID
            detecciones.append({
                "clase": nombre_clase,
                "confianza": round(confianza, 2),
                "bbox": bbox
            })

    # Generar imagen marcada (NumPy BGR → RGB → PIL)
    imagen_marcada_cv2 = resultados[0].plot()
    imagen_marcada_rgb = cv2.cvtColor(imagen_marcada_cv2, cv2.COLOR_BGR2RGB)
    imagen_pil = Image.fromarray(imagen_marcada_rgb)

    logger.info(f"Detecciones encontradas: {detecciones}")
    return detecciones, imagen_pil
