"""
logger.py

Autor: Álvaro Cortés González  
Universidad: Escuela Politécnica Superior de Córdoba  
Trabajo Fin de Grado - Automatización en la Evaluación de Riesgos en Maquinaria a Partir de Imágenes Mediante Técnicas de IA  
Fecha: Junio 2025

Descripción:
    Este módulo configura un sistema de logging unificado para toda la aplicación.
    Permite registrar eventos, errores y acciones relevantes tanto en consola como
    en un archivo externo llamado 'registro.log'.
"""

import logging

# Configuración básica del logger
logging.basicConfig(
    level=logging.INFO,  # Nivel mínimo de mensajes registrados (puede ser cambiado a DEBUG, WARNING, etc.)
    format='%(asctime)s [%(levelname)s] %(message)s',  # Formato del mensaje de log
    handlers=[
        logging.FileHandler("registro.log", encoding="utf-8"),  # Guarda los logs en un archivo
        logging.StreamHandler()  # También muestra los logs en la consola
    ]
)

# Instancia reutilizable del logger para otros módulos
logger = logging.getLogger(__name__)
