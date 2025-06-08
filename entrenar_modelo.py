"""
entrenar_modelo.py

Autor: Álvaro Cortés González  
Universidad: Escuela Politécnica Superior de Córdoba  
Trabajo Fin de Grado - Automatización en la Evaluación de Riesgos en Maquinaria a Partir de Imágenes Mediante Técnicas de IA  
Fecha: Junio 2025

Descripción:
    Este script se utiliza para entrenar un modelo YOLOv8 utilizando imágenes
    etiquetadas previamente y almacenadas en formato YOLO. Se emplea la librería
    Ultralytics y el archivo 'data.yaml' generado por Roboflow.
"""

from ultralytics import YOLO

# Carga el modelo YOLOv8 base (se puede usar yolov8n.pt, yolov8s.pt, etc.)
# En este caso, se utiliza yolov8n.pt (versión "nano"), por ser la más ligera y rápida
modelo = YOLO("yolov8n.pt")

# Inicia el proceso de entrenamiento del modelo
modelo.train(
    data="C:/Users/alvar/tfg_riesgos_ia/datasets/data.yaml",  # Ruta absoluta al archivo YAML del dataset
    epochs=50,                     # Número de épocas (iteraciones sobre el dataset)
    imgsz=640,                     # Tamaño de las imágenes de entrada
    batch=8,                       # Tamaño del batch (número de imágenes procesadas por paso)
    project="runs_entrenamiento", # Carpeta donde se guardan los resultados
    name="evaluador_riesgos"      # Subcarpeta específica de este entrenamiento
)
