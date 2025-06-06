# IIC3633-Proyecto

Proyecto hecho para el curso Sistemas Recomendadores IIC3633-1-2025.

El proyecto fue realizado con **Python 3.11.9** (recomendado utilizar CUDA o un entorno en Colab) y requiere las siguientes librerías:

- `pandas`
- `numpy`
- `scikit-learn`
- `scipy`
- `matplotlib`
- `seaborn`
- `prettytable`
- `tqdm`
- `torch`
- `torch-geometric`

El proyecto consiste en los siguientes archivos:

- `proyecto.ipynb`: Notebook que contiene el avance de proyecto del código del proyecto. Contiene 4 secciones principales:

  1. **Introducción**: Descripción del cuaderno
  2. **Pasos preliminares**: Instalación de dependencias, carga de datos, preprocesamiento y análisis de datos.
  3. **Modelos**: Se crean las clases y funciones necesarias para los modelos de recomendación (Random, Popular, DeepFM, Content Based y LightGCN)
  4. **Evaluación**: Donde se evalúa el modelo.
- `data/`: Carpeta que contiene los datos utilizados en el proyecto. (Deben ser descargados desde [aquí](https://amazon-reviews-2023.github.iot) en la sección de **Video_Games -> review, meta**.
