from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar el directorio estático
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta para servir el archivo HTML
@app.get("/", response_class=HTMLResponse)
async def read_html():
    with open("index.html") as f:
        return f.read()

@app.get("/nombres")
async def obtener_nombres():
    return {"nombres": ["Juan", "María", "Pedro"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
