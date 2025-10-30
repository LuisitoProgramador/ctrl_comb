# Imagen base
FROM python:3.13.5-slim-bullseye

# setear variables de entorno

ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
# Desactivar la verificación de versión de pip
ENV PYTHONDONTWRITEBYTECODE 1
# Evitar que Python cree archivos .pyc
ENV PYTHONUNBUFFERED 1
# Hacer que la salida de Python sea inmediata

# Crear y establecer el directorio de trabajo
WORKDIR /code

# Instalar dependencias del sistema
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copiar el código de la aplicación
COPY . .


