from fastapi import FastAPI

app = FastAPI()


@app.get("/parite/{nombre}")
def calculer_parite(nombre: int):
    if nombre % 2 == 0:
        parite = "paire"
    else:
        parite = "impaire"

    return {
        "nombre": nombre,
        "parite": parite
    }