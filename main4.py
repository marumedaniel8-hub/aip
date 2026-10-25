from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class TacheEntree(BaseModel):
    titre: str
    terminee: bool = False


class Tache(TacheEntree):
    id: int


taches: list[Tache] = []
prochain_id = 1


@app.get("/taches")
def afficher_taches():
    return taches


@app.post("/taches", status_code=201)
def ajouter_tache(tache_entree: TacheEntree):
    global prochain_id

    nouvelle_tache = Tache(
        id=prochain_id,
        titre=tache_entree.titre,
        terminee=tache_entree.terminee
    )

    taches.append(nouvelle_tache)
    prochain_id += 1

    return nouvelle_tache


@app.get("/taches/{id}")
def afficher_tache(id: int):
    for tache in taches:
        if tache.id == id:
            return tache

    raise HTTPException(status_code=404, detail="Tâche introuvable")


@app.put("/taches/{id}")
def modifier_tache(id: int, tache_modifiee: TacheEntree):
    for index, tache in enumerate(taches):
        if tache.id == id:
            taches[index] = Tache(
                id=id,
                titre=tache_modifiee.titre,
                terminee=tache_modifiee.terminee
            )
            return taches[index]

    raise HTTPException(status_code=404, detail="Tâche introuvable")


@app.delete("/taches/{id}")
def supprimer_tache(id: int):
    for index, tache in enumerate(taches):
        if tache.id == id:
            taches.pop(index)
            return {"message": "Tâche supprimée"}

    raise HTTPException(status_code=404, detail="Tâche introuvable")
