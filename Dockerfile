# Usa una imagen base oficial de Python (basada en Debian)
FROM python:3.12-slim-bullseye

# Establece el directorio de trabajo en /app
WORKDIR /app

# Establece las variables de entorno para Python
ENV PYTHONUNBUFFERED 1

# Copia los archivos de requerimientos e instala las dependencias
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /app/

# Expone el puerto que usa Django
EXPOSE 8000
