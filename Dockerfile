# flask_app/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

# Expone el puerto 5000
EXPOSE 8000

# Comando para correr la app
CMD ["python", "app.py"]