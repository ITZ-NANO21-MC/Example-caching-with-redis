from flask import Flask, render_template, request, jsonify
from pymemcache.client import base
import os
import time
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configurar cliente de Memcached
MEMCACHED_HOST = os.getenv('MEMCACHED_HOST', 'localhost')
MEMCACHED_PORT = int(os.getenv('MEMCACHED_PORT', 11211))
cache = base.Client((MEMCACHED_HOST, MEMCACHED_PORT))

# Función simulada de base de datos (lenta)
def get_data_from_db(query):
    time.sleep(3)  # Simular retardo de 3 segundos
    return f"Resultados para: {query}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify(error="Query vacía"), 400
    
    # Intentar obtener datos del caché
    cached_data = cache.get(query)
    
    if cached_data:
        return jsonify(
            data=cached_data.decode('utf-8'),
            source="Memcached (Caché)"
        )
    
    # Obtener datos de la "base de datos"
    db_data = get_data_from_db(query)
    
    # Almacenar en caché (expira en 60 segundos)
    cache.set(query, db_data, expire=60)
    
    return jsonify(
        data=db_data,
        source="Base de Datos"
    )

if __name__ == '__main__':
    app.run(debug=True)