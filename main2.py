from fastapi import FastAPI

app = FastAPI()

@app.get("/calcul/{operation}/{a}/{b}")

def calcul_op(operation: str,a: int, b: int ):
    if operation == "add":
        resultat = a+b
    elif operation == "sou":
        resultat = a-b    
    elif operation == "mul":
        resultat = a*b
    elif operation == "div":
        if b==0:
            return {"erreur"}
        resultat = a/b   
    else:
        return{"erreur"}                             
    return{
        "operation": operation,
        "a":a,
        "b":b,
        "calcul": resultat,
    }