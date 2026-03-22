
from fastapi import FastAPI

app = FastAPI() #creo l'oggetto fastAPI

@app.get("/") #metodo get per la richiesta, mettiamo / che signifca la radice ovvero l'home page. Se aggiungo hello e non metto solo /
#allora dovrò cercare il sito http://localhost:8000/hello e non http://localhost:8000/ 
def hello_world(q: str, 
                sort:bool =False #mi dovrebbe dare errore perchè qui sort è bool ma nel dizionario è str dunque non va bene 
                )->dict [str,str | bool]: #dico che il return è un dizionario con chiave str e valore str o bool dunque così non genera errore
    #perchè se avessi lasciato ->dict [str,str] allora mi avrebbe dato errore perchè avrei inserito un bool ma il dizionario si aspetta una str
    return {"q":q, "sort":sort} #il return è convertito direttamente in json

@app.get("/home")
def homepage():
    return "This is the home page"


#anche qui obbiamo usare il typing
@app.get("/{username}")
def username_webpage(username:str):
    return f"This in the webpage of user {username}"

@app.get("/{username}/orders/{order_id}") #immaginiamo di essere in un negozio

def repository_webpage(username:str,
                       order_id:int,
                       sort: bool = False):
    return f"Order {order_id} for user {username}, Sorted:{sort}"





