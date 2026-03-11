import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import httpx

# Cargamos las variables del archivo .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = FastAPI()

# Configuramos la carpeta de plantillas HTML
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    """Muestra la página principal con el formulario."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/clima")
async def obtener_clima(request: Request, ciudad: str = Form(...)):
    """Recibe la ciudad seleccionada y busca su clima."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    if response.status_code != 200:
        error_msg = "No se pudo obtener el clima para esa ciudad."
        return templates.TemplateResponse("index.html", {"request": request, "error": error_msg})

    data = response.json()
    
    # Preparamos los datos para enviarlos al HTML
    contexto_clima = {
        "nombre": data["name"],
        "temp": data["main"]["temp"],
        "descripcion": data["weather"][0]["description"].capitalize(),
        "humedad": data["main"]["humidity"],
        "icono": data["weather"][0]["icon"]
    }

    return templates.TemplateResponse("index.html", {"request": request, "clima": contexto_clima})