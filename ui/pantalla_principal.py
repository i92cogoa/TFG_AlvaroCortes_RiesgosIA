"""
pantalla_principal.py

Autor: Álvaro Cortés González  
Universidad: Escuela Politécnica Superior de Córdoba  
Trabajo Fin de Grado - Automatización en la Evaluación de Riesgos en Maquinaria a Partir de Imágenes Mediante Técnicas de IA  
Fecha: Junio 2025

Descripción:
    Este módulo gestiona la ventana principal de la aplicación. Carga el modelo
    entrenado de IA, muestra una barra de progreso animada y habilita el acceso
    a la ventana de evaluación una vez el modelo ha sido localizado correctamente.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from config import NOMBRE_APLICACION
from utils.logger import logger
import os

from ui.ventana_evaluacion import lanzar_ventana_evaluacion

# Ruta al archivo de pesos del modelo entrenado
MODELO_PATH = "modelo/pesos_entrenados.pt"


def mostrar_titulo():
    """
    Crea y muestra la ventana principal de la aplicación.
    Inicia una animación de carga simulada y comprueba la existencia del modelo.
    """

    def iniciar_carga_modelo():
        """
        Simula el proceso de carga del modelo mediante una barra de progreso.
        Una vez completa, ejecuta la comprobación real del archivo del modelo.
        """
        progreso_actual = 0

        def avanzar_barra():
            nonlocal progreso_actual
            if progreso_actual < 100:
                progreso_actual += 5
                barra_progreso["value"] = progreso_actual
                root.after(30, avanzar_barra)
            else:
                comprobar_existencia_modelo()

        avanzar_barra()

    def comprobar_existencia_modelo():
        """
        Verifica que el archivo del modelo exista en la ruta especificada.
        En caso afirmativo, habilita el botón para abrir la ventana de evaluación.
        En caso negativo, muestra un mensaje de error y desactiva el botón.
        """
        if os.path.exists(MODELO_PATH):
            logger.info("Modelo cargado correctamente.")
            etiqueta_estado.config(text="Modelo cargado con éxito ✅", foreground="green")
            boton_iniciar["state"] = "normal"
            boton_iniciar["command"] = lambda: lanzar_ventana_evaluacion(root)
        else:
            logger.error(f"No se encontró el modelo en: {MODELO_PATH}")
            etiqueta_estado.config(text="Error al cargar el modelo", foreground="red")
            messagebox.showerror(
                "Error de carga",
                f"No se ha podido cargar el modelo.\nArchivo no encontrado:\n{MODELO_PATH}"
            )
            boton_iniciar["state"] = "disabled"

    # === Interfaz de la ventana principal ===
    global root, barra_progreso
    root = tk.Tk()
    root.title(NOMBRE_APLICACION)
    root.geometry("600x300")
    root.resizable(False, False)

    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(expand=True, fill="both")

    # Título principal
    ttk.Label(main_frame, text=NOMBRE_APLICACION, font=("Helvetica", 20, "bold")).pack(pady=(10, 5))

    # Estado del modelo
    etiqueta_estado = ttk.Label(
        main_frame, text="Cargando modelo...", font=("Helvetica", 11), foreground="gray"
    )
    etiqueta_estado.pack(pady=(0, 20))

    # Barra de progreso
    barra_progreso = ttk.Progressbar(main_frame, length=400, mode="determinate")
    barra_progreso.pack(pady=10)

    # Botón para iniciar la evaluación (desactivado hasta cargar modelo)
    boton_iniciar = ttk.Button(main_frame, text="Iniciar evaluación", state="disabled")
    boton_iniciar.pack(pady=(20, 0))

    # Iniciar la animación de carga tras un breve retardo
    root.after(100, iniciar_carga_modelo)

    logger.info("Ventana principal cargada correctamente.")
    root.mainloop()
