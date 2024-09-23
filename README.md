
# Flask Dashboard con Conexión a MySQL

Este proyecto es un pequeño dashboard desarrollado en Python que realiza una conexión a una base de datos MySQL y visualiza los datos a través de gráficos. Los gráficos incluyen una barra que muestra la relación entre edad y salario, y un gráfico circular que representa la cantidad de personas por ciudad. Además, se despliega una tabla con los registros de la base de datos en formato HTML.

## Requisitos

- Python 3.x
- MySQL
- Virtualenv (opcional, pero recomendado)

## Instalación

1. Clona el repositorio o descarga el código fuente.

2. Crea un entorno virtual (opcional, pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias necesarias utilizando el archivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu base de datos MySQL:

   - Crea la base de datos y la tabla ejecutando el siguiente SQL en tu servidor MySQL:

     ```sql
     CREATE DATABASE dashboard_db;
     USE dashboard_db;

     CREATE TABLE empleados (
       id INT PRIMARY KEY AUTO_INCREMENT,
       nombre VARCHAR(100),
       edad INT,
       ciudad VARCHAR(100),
       salario DECIMAL(10,2)
     );
     
     INSERT INTO empleados (nombre, edad, ciudad, salario) VALUES
       ('Juan Pérez', 30, 'Ciudad de México', 50000.00),
       ('María Gómez', 25, 'Guadalajara', 45000.00),
       ('Carlos Sánchez', 35, 'Monterrey', 55000.00),
       ('Laura Martínez', 28, 'Puebla', 48000.00),
       ('José Hernández', 40, 'Ciudad de México', 60000.00),
       ('Ana López', 30, 'Guadalajara', 47000.00),
       ('Luis García', 28, 'Puebla', 49000.00),
       ('Sofía Ramírez', 25, 'Monterrey', 46000.00),
       ('Miguel Torres', 35, 'Ciudad de México', 52000.00),
       ('Elena Cruz', 40, 'Puebla', 55000.00);
     ```

5. Configura la conexión a MySQL en el archivo Python (`app.py`), cambiando los parámetros de conexión como `host`, `user`, y `password` según tu configuración de MySQL.

6. Ejecuta la aplicación Flask en el directorio principal del proyecto:

   ```bash
   python app.py
   ```

7. Abre tu navegador web y visita `http://127.0.0.1:5000` para ver el dashboard.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask.
- `static/`: Carpeta donde se guardan las imágenes generadas por los gráficos.
- `templates/`: Carpeta que contiene las plantillas HTML.
- `requirements.txt`: Archivo que contiene las dependencias necesarias para el proyecto.

## Notas

- Asegúrate de que MySQL esté corriendo y la base de datos esté configurada correctamente antes de ejecutar la aplicación.
- Este proyecto usa Matplotlib para generar los gráficos, se puede modificar el código para usar Plotly u otra biblioteca de visualización si se desea.

## imagenes

![image](https://github.com/user-attachments/assets/2a353e7a-9eab-4cda-8277-35c53b345ea1)
![image](https://github.com/user-attachments/assets/6e4c01b2-4604-4e28-8ad6-14464c045695)
![image](https://github.com/user-attachments/assets/dda13b2b-0d74-4c3b-a080-cc77d3161663)



