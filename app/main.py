from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# ==================================
# DATOS EN MEMORIA
# ==================================

datos_sensor = {
    "temperatura": 0,
    "temperatura_horno": 0,
    "humedad_grano": 0,
    "extractor": "OFF",
    "calefactor": "OFF"
}

# ==================================
# PAGINA PRINCIPAL
# ==================================

@app.get("/")
async def home():

    with open("app/templates/index.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    return HTMLResponse(content=html_content)

# ==================================
# RECIBE DATOS DESDE ESP32
# ==================================

@app.post("/api/datos")
async def recibir_datos(request: Request):

    global datos_sensor

    datos_sensor = await request.json()

    print("\n========== DATOS RECIBIDOS ==========")
    print(datos_sensor)

    return {"estado": "ok"}

# ==================================
# ENVIA DATOS AL NAVEGADOR
# ==================================

@app.get("/api/datos")
async def obtener_datos():

    return datos_sensor