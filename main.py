from fastapi import FastAPI

app = FastAPI() #creo l'oggetto fastAPI

@app.get("/hello") #metodo get per la richiesta, mettiamo / che signifca la radice ovvero l'home page. Se aggiungo hello e non metto solo /
#allora dovrò cercare il sito http://localhost:8000/hello e non http://localhost:8000/ 
def hello_world():
    return "Hello World!"  #il return è convertito direttamente in json









