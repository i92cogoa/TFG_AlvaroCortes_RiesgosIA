"""
ventana_evaluacion.py

Autor: Álvaro Cortés González  
Universidad: Escuela Politécnica Superior de Córdoba  
Trabajo Fin de Grado - Automatización en la Evaluación de Riesgos en Maquinaria a Partir de Imágenes Mediante Técnicas de IA  
Fecha: Junio 2025

Descripción:
    Este módulo gestiona la ventana de evaluación de imágenes. Permite al usuario
    cargar una imagen desde su equipo, analizarla con el modelo entrenado de IA
    y generar automáticamente un informe en formato DOCX con los resultados detectados.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from utils.logger import logger
from modelo.yolo_modelo_real import analizar_imagen
from generar_informe import generar_informe
from datetime import datetime
import os


def lanzar_ventana_evaluacion(ventana_anterior):
    """
    Cierra la ventana anterior (pantalla principal) y lanza la ventana de evaluación.
    """
    ventana_anterior.destroy()

    app = tk.Tk()
    app.title("Evaluación de Imagen")
    app.geometry("700x550")
    app.resizable(False, False)

    frame = ttk.Frame(app, padding=20)
    frame.pack(expand=True, fill="both")

    etiqueta = ttk.Label(frame, text="Seleccione una imagen para evaluar:", font=("Helvetica", 14))
    etiqueta.pack(pady=10)

    # Área donde se mostrará la imagen cargada
    canvas = tk.Label(frame)
    canvas.pack(pady=10)

    botones_frame = ttk.Frame(frame)
    botones_frame.pack(pady=10)

    # Botones que aparecen tras cargar una imagen
    boton_evaluar = ttk.Button(botones_frame, text="Evaluar", state="disabled")
    boton_cancelar = ttk.Button(botones_frame, text="Cancelar y elegir otra", state="disabled")

    boton_evaluar.grid(row=0, column=0, padx=10)
    boton_cancelar.grid(row=0, column=1, padx=10)

    def cargar_imagen():
        """
        Abre un diálogo para que el usuario seleccione una imagen.
        Muestra la imagen seleccionada en pantalla y habilita los botones de acción.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.jpeg")])
        if not file_path:
            return

        try:
            img = Image.open(file_path)
            img = img.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            canvas.configure(image=img_tk)
            canvas.image = img_tk
            canvas.path_imagen = file_path

            logger.info(f"Imagen cargada: {file_path}")
            boton_evaluar["state"] = "normal"
            boton_evaluar["command"] = evaluar_imagen
            boton_cancelar["state"] = "normal"

        except Exception as e:
            logger.error(f"No se pudo cargar la imagen: {e}")
            messagebox.showerror("Error", "No se pudo abrir la imagen seleccionada.")

    def evaluar_imagen():
        """
        Llama al modelo de IA para analizar la imagen cargada.
        Muestra la imagen marcada con los riesgos detectados y genera un informe DOCX.
        """
        if hasattr(canvas, "path_imagen"):
            resultados, imagen_marcada = analizar_imagen(canvas.path_imagen)

            # Mostrar la imagen con los fallos marcados por IA
            imagen_marcada = imagen_marcada.resize((300, 300))
            img_tk_marcada = ImageTk.PhotoImage(imagen_marcada)
            canvas.configure(image=img_tk_marcada)
            canvas.image = img_tk_marcada

            # Preparar datos para el informe
            nombre_maquina = "Taladro"
            fecha_hora_str = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
            nombre_archivo = f"Informe {nombre_maquina} {fecha_hora_str}.docx"
            ruta_informe = os.path.join("informes", nombre_archivo)
            ruta_imagen_temp = os.path.join("informes", "imagen_temp.jpg")

            try:
                imagen_marcada.save(ruta_imagen_temp)
                generar_informe(nombre_maquina, ruta_imagen_temp, resultados, ruta_informe)
                logger.info(f"Informe generado: {ruta_informe}")
            except Exception as e:
                logger.error(f"No se pudo generar el informe: {e}")
                messagebox.showwarning("Informe no generado", "Ocurrió un error al crear el informe.")
                return

            # Mostrar resumen de resultados en una ventana emergente
            if resultados:
                mensaje = "\n".join(
                    [f"- {r['clase']} ({r['confianza'] * 100:.1f}%)" for r in resultados]
                )
                mensaje_completo = f"Se detectaron:\n{mensaje}\n\nInforme generado en la carpeta 'informes'."
            else:
                mensaje_completo = "No se detectó ningún riesgo.\n\nInforme generado en la carpeta 'informes'."

            messagebox.showinfo("Resultados de la IA", mensaje_completo)

        else:
            messagebox.showwarning("Advertencia", "No se ha cargado ninguna imagen.")

    def cancelar_y_reiniciar():
        """
        Elimina la imagen actual y permite al usuario seleccionar una nueva.
        Restablece los botones a su estado inicial.
        """
        canvas.configure(image="")
        canvas.image = None
        if hasattr(canvas, "path_imagen"):
            del canvas.path_imagen
        boton_evaluar["state"] = "disabled"
        boton_cancelar["state"] = "disabled"
        cargar_imagen()

    def cerrar_ventana():
        """
        Cierra la ventana de evaluación de forma segura.
        """
        logger.info("Ventana de evaluación cerrada por el usuario.")
        app.destroy()

    # Botón para cargar la imagen inicial
    boton_cargar = ttk.Button(frame, text="Subir Imagen", command=cargar_imagen)
    boton_cargar.pack(pady=10)

    # Botón para cerrar la ventana de evaluación
    boton_cerrar = ttk.Button(frame, text="Cerrar ventana", command=cerrar_ventana)
    boton_cerrar.pack(pady=5)

    # Asignar acción al botón de cancelar
    boton_cancelar.config(command=cancelar_y_reiniciar)

    app.mainloop()
