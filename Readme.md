# Proyecto Maní

Plataforma IoT para monitoreo agroindustrial aplicada al almacenamiento y conservación de maní.

## Descripción

Proyecto desarrollado en el Instituto Superior Politécnico Córdoba (ISPC) dentro del espacio curricular Proyecto Integrador.

La solución integra sensores IoT, procesamiento de datos y visualización web para monitorear variables críticas durante el almacenamiento y secado de granos.

## Tecnologías utilizadas

* ESP32
* FastAPI
* HTML
* CSS
* JavaScript
* MQTT
* Docker
* InfluxDB
* Grafana
* Webots
* Imágenes Satelitales

## Funcionalidades

* Monitoreo de temperatura ambiente
* Monitoreo de temperatura de horno
* Monitoreo de humedad del grano
* Visualización en tiempo real
* Dashboard de análisis
* Automatización de extractor y calefactor
* Acceso a documentación mediante código QR

## Equipo

* Juan Canales
* Walter Nieto
* Agustín Corzo
* Ivi Monsalvo
* Maxi Altamirano
* Fabiana Fontana

## Institución

Instituto Superior Politécnico Córdoba (ISPC)

Tecnicatura Superior en Nuevas Tecnologías Aplicadas al Agro

Espacio Curricular: Proyecto Integrador

Docente: Miguel Ángel Rodríguez Maiztegui

## Ejecución local

Instalar dependencias:

pip install -r requirements.txt

Iniciar servidor:

uvicorn app.main:app --reload

Acceder desde navegador:

http://localhost:8000

