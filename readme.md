# Requisitos del sistema

1. Python > 3.9
2. MySQL > 5.7

# Instalacion del sistema

Como primer paso, debemos crear una base de datos, la cual se creara a partir del archivo db.sql que se encuentra en la raiz de este proyecto.

Es necesario ir al archivo app.py y cambiar las credenciales de conexion a la base de datos de mysql. Se encuentra desde la linea 4 hasta la linea 10.

Es necesario instalar las dependencias que se encuentran en el archivo requirements.txt

Por ultimo, ejecutar el servidor con el comando, el servidor que escuchando en el puerto 5000

```python app.py```