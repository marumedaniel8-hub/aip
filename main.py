from fastapi import FastAPI

app = FastAPI()

@app.get("/doubles/{nombres}")

def calculer_sec(nombres: int):
    return {
        "nombres": nombres,
        "doubles": nombres * 2
    }
