
from fastapi import FastAPI

app= FastAPI()


@app.get("/")

def home():
    return "Benvenuto nel nostro sito universitario!"


@app.get("/student/{name}")

def studente(name: str):
    return (f"Questa è la pagina dello studente {name}")


@app.get("/student/{name}/exam/{exam_id}")

def studente(name: str,
             exam_id: int,
             passed:bool = False): #è un parametro opzionale dunque si metterà nell'URL con '?'
    return (f"Student {name}, exam {exam_id}, passed: {passed}")


@app.get("/search")

def studente(course: str,
             year: int,
             active:bool = False)->dict[str,str| int|bool]: #il dizionario diz[tipo_delle_chiavi, tipo_dei_valori] accetta solo due tipi
    return{"Corso":course, "anno":year, "attivo" :active}
    #dunque se mi aspetto un dizionario in uscita, allora dovrò formattarlo nel modo {"chiave":valore}