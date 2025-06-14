# TFG_AlvaroCortes_RiesgosIA

**Autor**: Álvaro Cortés González  
**Universidad**: Escuela Politécnica Superior de Córdoba  
**Título**: Automatización en la Evaluación de Riesgos en Maquinaria a Partir de Imágenes Mediante Técnicas de IA

## 📁 Estructura del Proyecto

```
TFG_AlvaroCortes_RiesgosIA/
├── config.py
├── entrenar_modelo.py
├── generar_informe.py
├── main.py
├── registro.log
├── yolov8n.pt
├── datasets/
│   ├── data.yaml
│   ├── train/
│   └── valid/
├── imagenes/
│   ├── preprocesadas/
│   └── sin_etiquetar/
├── informes/
├── modelo/
│   ├── yolo_modelo_real.py
│   ├── yolo_simulado.py
│   └── pesos_entrenados.pt
├── preprocesado/
│   └── preprocesador.py
├── resultados/
│   └── predicciones.json
├── runs_entrenamiento/
│   └── evaluador_riesgos/
│       ├── weights/
│       └── resultados, gráficos, métricas
├── ui/
│   ├── pantalla_principal.py
│   └── ventana_evaluacion.py
├── utils/
│   └── logger.py
```

## ▶️ ¿Qué hace esta aplicación?

Esta aplicación permite cargar imágenes de maquinaria y detectar riesgos de seguridad mediante un modelo entrenado con YOLOv8. Muestra visualmente los riesgos detectados y genera un informe automático con las observaciones y medidas correctoras.

## ⚙️ Requisitos

- Python 3.11
- Entorno virtual activo (recomendado)

### 📦 Instalación de dependencias

Instala todas las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt
```

Este archivo incluye todas las bibliotecas necesarias como:
- `ultralytics`
- `opencv-python`
- `python-docx`
- `Pillow`

## 🚀 Cómo ejecutar

1. Activa el entorno virtual:

```bash
cd TFG_AlvaroCortes_RiesgosIA
.\yolovenv\Scripts\activate
```

2. Ejecuta la aplicación:

```bash
python main.py
```

## 📄 Informes

Los informes se guardan automáticamente en la carpeta `informes/` tras cada evaluación.

#   T F G _ A l v a r o C o r t e s _ R i e s g o s I A 
 
 
