📦 Instalación y Configuración
Sigue estos pasos en tu terminal de Ubuntu (WSL2):

1. Clonar o crear la carpeta del proyecto
Bash
mkdir weather-app && cd weather-app
2. Configurar el entorno virtual
Bash
python3 -m venv venv
source venv/bin/activate
3. Instalar dependencias
Bash
pip install fastapi uvicorn httpx python-dotenv jinja2 python-multipart

Asegúrate de que tu entorno virtual esté activo: source venv/bin/activate.

Inicia el servidor con Uvicorn:

Bash: uvicorn main:app --reload
Abre tu navegador favorito y accede a