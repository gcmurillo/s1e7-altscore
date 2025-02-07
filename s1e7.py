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
