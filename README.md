# README: Sistema de Caché con Flask y Memcached

## Descripción

Este proyecto implementa un sistema de caché utilizando Flask como framework web y Memcached para almacenamiento temporal de datos. La aplicación simula una base de datos lenta y demuestra cómo el uso de Memcached puede mejorar significativamente el rendimiento al almacenar en caché los resultados de las consultas.

## Características

- Interfaz web simple para realizar búsquedas
- Sistema de caché con Memcached para almacenar resultados
- Simulación de base de datos con retardo artificial
- Indicación clara de la fuente de los datos (caché o base de datos)
- Configuración mediante variables de entorno

## Requisitos Previos

- Python 3.7+
- Memcached instalado y ejecutándose
- pip (gestor de paquetes de Python)

## Instalación

1. Clona o descarga este proyecto
2. Instala las dependencias:
```bash
pip install flask pymemcache python-dotenv
```

3. Asegúrate de que Memcached esté ejecutándose:
```bash
# En Ubuntu/Debian
sudo apt-get install memcached
sudo service memcached start

# En macOS con Homebrew
brew install memcached
brew services start memcached

# En Windows
# Descargar e instalar desde: https://memcached.org/downloads
```

## Configuración

El proyecto utiliza un archivo `.env` para configuración (opcional). Crea un archivo `.env` en la raíz del proyecto con:

```
MEMCACHED_HOST=localhost
MEMCACHED_PORT=11211
```

## Ejecución

1. Inicia la aplicación Flask:
```bash
python app.py
```

2. Abre tu navegador y ve a: http://localhost:5000

## Uso

1. Escribe una consulta en el campo de texto
2. Haz clic en "Buscar"
3. La primera vez que busques un término, tomará aproximadamente 3 segundos (simulando una base de datos lenta)
4. Las búsquedas posteriores del mismo término serán instantáneas (servidas desde la caché)
5. Los resultados se almacenan en caché durante 60 segundos

## Estructura del Proyecto

```
proyecto-cache/
├── app.py              # Aplicación Flask principal
├── index.html          # Plantilla HTML para la interfaz
├── .env               # Variables de entorno (opcional)
└── README.md          # Este archivo
```

## Personalización

- Modifica el tiempo de expiración de la caché cambiando el valor `expire=60` en `app.py`
- Ajusta el retardo de la base de datos simulada modificando `time.sleep(3)` en `app.py`
- Cambia la configuración de Memcached mediante las variables de entorno

## Solución de Problemas

- Si la aplicación no se conecta a Memcached, verifica que el servicio esté ejecutándose
- Asegúrate de que los puertos no estén siendo utilizados por otras aplicaciones
- Verifica que todas las dependencias estén instaladas correctamente

## Tecnologías Utilizadas

- Flask - Framework web de Python
- PyMemcache - Cliente Python para Memcached
- Memcached - Sistema de almacenamiento en caché de memoria distribuida
- HTML/JavaScript - Interfaz de usuario frontend
