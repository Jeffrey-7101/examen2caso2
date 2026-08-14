from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Muestra el ID del contenedor para verificar el balanceo de carga
    container_id = os.uname()[1]
    fecha = os.popen('date').read().strip()
    return f"Hello Jeffrey Pinto, from container {container_id} con fecha {fecha}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)