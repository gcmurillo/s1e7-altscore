from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="SOS - gcmurillo")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/status")
def status():
    return { "damaged_system": "life_support" }

@app.get("/repair-bay", response_class=HTMLResponse)
def repair_bay():
    return """<!DOCTYPE html>
                <html>
                <head>
                    <title>Repair</title>
                </head>
                <body>
                <div class="anchor-point">LIFE-03</div>
                </body>
                </html>"""


@app.post("/teapot")
def teapot():
    return JSONResponse(status_code=418, content={"message": "I'm a teapot"})

def calculate_liquid(pressure):
    return round((pressure + 4.213)/4061.22, 4)

def calculate_vapor(pressure):
    return round((10.0012 - pressure)/0.3317, 4)

## Se agrega el endpoint para la solucion del ejercicio 9
@app.get("/phase-change-diagram")
def phase_change_diagram(pressure: float):
    liquid = calculate_liquid(pressure)
    vapor = calculate_vapor(pressure)
    return { "specific_volume_liquid": liquid, "specific_volume_vapor": vapor }
