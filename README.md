# Weather App Pro 🌤️

Esta es una versión refactorizada de la aplicación de clima, ahora con una arquitectura desacoplada: un **Backend en FastAPI** y un **Frontend en React**.

## 🚀 Características
- **Backend**: API REST moderna con FastAPI.
- **Frontend**: Dashboard premium con diseño **Glassmorphism**.
- **Reactivo**: Actualizaciones instantáneas y estados de carga fluidos.
- **Limpio**: Separación de responsabilidades para facilitar el escalado.

---

## 🛠️ Requisitos Previos
1. **Python 3.10+** instalado.
2. Una **API Key** de [OpenWeatherMap](https://openweathermap.org/api).

---

## 📂 Estructura del Proyecto
```text
01_weater_cli/
├── backend/            # Servidor FastAPI (Python)
│   ├── .env            # Variables de entorno (API Key)
│   ├── main.py         # Lógica de la API
│   └── requirements.txt
└── frontend/           # Interfaz de Usuario (React)
    ├── index.html      # Punto de entrada
    └── style.css       # Estilos Premium
```

---

## ⚙️ Configuración e Inicio

### 1. Configurar el Backend
Entra en la carpeta del backend y prepara el entorno:

```bash
cd backend
# (Opcional) Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

#### Configurar la API Key
Crea un archivo `.env` en la carpeta `backend/` (puedes usar `.envTEMPLATE` como base):
```env
OPENWEATHER_API_KEY=tu_api_key_aqui
```

#### Iniciar Servidor
```bash
uvicorn main:app --reload
```
El backend estará disponible en `http://localhost:8000`.

### 2. Iniciar el Frontend
El frontend está diseñado para ser ligero y no requiere instalación de dependencias locales.

1. Navega a la carpeta `frontend/`.
2. Abre el archivo `index.html` en tu navegador favorito.
3. ¡Busca cualquier ciudad y disfruta del diseño!

---

## 📈 Próximos Pasos
- Agregar historial de búsquedas.
- Implementar pronóstico de 5 días.
- Cambiar el fondo dinámicamente según el clima de la ciudad.

---
Hecho con con fines educativos para el Python Roadmap.