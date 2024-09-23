# app.py

# Importar las bibliotecas necesarias
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template
import os

# Conexión a la base de datos MySQL
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',       
    password='',
    database='dashboard_db'
)

# Crear un cursor para ejecutar consultas
cursor = db_connection.cursor()

# Ejecutar la consulta SQL para obtener todos los registros de la tabla 'empleados'
query = "SELECT * FROM empleados"
cursor.execute(query)

# Obtener los datos y convertirlos en un DataFrame de pandas
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(rows, columns=columns)

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
db_connection.close()

# Verificar si la carpeta 'static' existe, si no, crearla
if not os.path.exists('static'):
    os.makedirs('static')

# Generar el gráfico de barras (Edad vs Salario promedio)
plt.figure(figsize=(10,6))

# Agrupar por edad y calcular el salario promedio y el conteo de personas
edad_salario = df.groupby('edad')['salario'].mean()
edad_conteo = df.groupby('edad')['salario'].count()

# Generar el gráfico de barras (Edad vs Salario promedio)
plt.figure(figsize=(10,6))

# Agrupar por edad y calcular el salario promedio y el conteo de personas
edad_salario = df.groupby('edad')['salario'].mean()
edad_conteo = df.groupby('edad')['salario'].count()

# Crear el gráfico de barras
bars = plt.bar(edad_salario.index, edad_salario.values, color='skyblue')

# Establecer los límites del eje y para incluir el salario máximo
plt.ylim(0, max(edad_salario.values) + 5000)

# Agregar etiquetas encima de cada barra, con un color distinto
for idx, bar in enumerate(bars):
    edad = edad_salario.index[idx]
    conteo = edad_conteo[edad]
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500, 
             f"{conteo}", ha='center', va='bottom', color='red', fontsize=12)

# Agregar leyenda para explicar los números en rojo
plt.text(0.5, max(edad_salario.values) + 10000, 'Números en rojo = Cantidad de personas por edad', 
         color='red', ha='center', fontsize=12)

# Configurar el gráfico
plt.xlabel('Edad')
plt.ylabel('Salario Promedio')
plt.title('Relación entre Edad y Salario (Número de Personas por Edad)')
plt.xticks(edad_salario.index)
plt.savefig('static/edad_vs_salario.png')
plt.close()



# Generar el gráfico circular (Cantidad de personas por ciudad)
ciudades = df['ciudad'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(ciudades, labels=ciudades.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Personas por Ciudad')
plt.savefig('static/personas_ciudad.png')
plt.close()

# Inicializar la aplicación Flask
app = Flask(__name__)

# Definir la ruta principal
@app.route('/')
def index():
    # Convertir el DataFrame en una tabla HTML
    tabla_html = df.to_html(classes='', index=False)
    # Renderizar la plantilla 'index.html' pasando la tabla HTML
    return render_template('index.html', tabla=tabla_html)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
