


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
 


app=FastAPI() 
templates= Jinja2Templates(directory="templates")#diciamo al motore di templating dove sono i nostri template



@app.get("/", response_class=HTMLResponse)#parameto che specifica in che formato fastapi deve convertire ilr isultato
def home(request:Request):#parametro passato automaticametne da fastapi, request conterrà la richiesta http get che riceve questa funzione(non ci interessa perchè)

    #dizionario che contiene tutte le variabili che voglio passare dal server all'html, devono avere lo stesso nome del template ovvero html
    text = {
        "title": "Home page",
        "content": "Welcome to the home page"
        
    }
    context = {"text": text, "sequence": ["a","b","c"]}
    #metto return perchè la devo restituire
    return templates.TemplateResponse( #funzione che prende 3 parametri, ma ora ci interessano solo 2
        request=request,  #richiesta che riceviamo, ha bisogno di ricevere il pacchetto http che arriva. Va sempre fatta
        name="home.html",  #quale html mostrare, diamo il nome del file che vogliamo mostrare
        context=context #passo anche il dizionario context
    )

    




