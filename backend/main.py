import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import httpx

# Cargamos las variables del archivo .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = FastAPI(title="Weather API")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica el dominio del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    """Endpoint de salud."""
    return {"status": "ok", "message": "Weather API is running"}

@app.get("/api/weather")
async def obtener_clima(ciudad: str):
    """Recibe la ciudad seleccionada y busca su clima."""
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API Key no configurada.")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise HTTPException(status_code=404, detail="Ciudad no encontrada.")
            raise HTTPException(status_code=500, detail="Error al conectar con el servicio de clima.")
        except Exception:
            raise HTTPException(status_code=500, detail="Error inesperado.")

    data = response.json()
    
    # Preparamos los datos para enviarlos como JSON
    contexto_clima = {
        "nombre": data["name"],
        "temp": data["main"]["temp"],
        "descripcion": data["weather"][0]["description"].capitalize(),
        "humedad": data["main"]["humidity"],
        "icono": data["weather"][0]["icon"]
    }

    return contexto_clima