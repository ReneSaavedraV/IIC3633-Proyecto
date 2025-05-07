# IIC3633-Proyecto
Proyecto hecho para el curso Sistemas Recomendadores IIC3633-1-2025.

El proyecto fue realizado con **Python 3.10.12** y requiere las siguientes librerías:
- `pandas`
- `numpy`
- `scikit-learn`
- `scipy`
- `matplotlib`
- `seaborn`
- `prettytable`

El proyecto consiste en los siguientes archivos:
- `proyecto.ipynb`: Notebook que contiene el analisis exploratorio de datos y la implementación de los modelos de recomendación.
- `preprocessFiles.py`: Script que convierte el archivo videogames.json a un archivo CSV y lo limpia. (Con tal de reducir el tamaño del archivo y facilitar su uso). Aunque se mantiene el original por si se utiliza en el futuro.
- `videogame_rating.csv`: Archivo CSV que contiene los datos de videojuegos y sus ratings. Contiene 2.5 millones de filas y 4 columnas. Las columnas son:
    - `userId`: ID del usuario.
    - `itemId`: ID del videojuego.
    - `rating`: Rating del videojuego por parte del usuario.
    - `timestamp`: Timestamp del rating.
- `videogames.csv`: Archivo CSV que contiene los datos de videojuegos.
    - `itemId`: ID del videojuego.
    - `name`: Nombre del videojuego.