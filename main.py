

from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from pydantic import Field, BaseModel


class Product(BaseModel):
    name:  Annotated[str,  Field(min_length=3, max_length=30)]
    price:  Annotated[float, Field(gt=0)]
    location: Annotated[str, Field(min_length=3)]



app=FastAPI() 
app.mount("/static",StaticFiles(directory="static"), name="static") #il primo parametro è ... il secondo è la cartella dove mettiamo i file ma dentro Staticfiles
templates= Jinja2Templates(directory="templates")#diciamo al motore di templating dove sono i nostri template

product_list=[
    {"nome": "notebook dell", "price": 29999.77,"location":"cagliari"},
    {"nome": " dell", "price": 65.77,"location":"oristano"},
    {"nome": "notebook ", "price": 43.77,"location":"olbia"}
]

@app.get("/", response_class=HTMLResponse)#parameto che specifica in che formato fastapi deve convertire ilr isultato
def home(request:Request):#parametro passato automaticametne da fastapi, request conterrà la richiesta http get che riceve questa funzione(non ci interessa perchè)

    #dizionario che contiene tutte le variabili che voglio passare dal server all'html, devono avere lo stesso nome del template ovvero html
    text = {
        "title": "Home page",
        "content": "Paguri...All'arrembaggioo!!"
        
    }
    dictionary={"key1": "value1","key2":"value2"}
    context = {"text": text, "dictionary": dictionary}#dizionario che ha come chiavi le variabili che vogliamo vedere e come valore i valori effettivi che vederemo

    #metto return perchè la devo restituire
    return templates.TemplateResponse( #funzione che prende 3 parametri, ma ora ci interessano solo 2
        request=request,  #richiesta che riceviamo, ha bisogno di ricevere il pacchetto http che arriva. Va sempre fatta
        name="home.html",  #quale html mostrare, diamo il nome del file che vogliamo mostrare
        context={"text": "Er capobranco"} #passo anche il dizionario context
    )


    
@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="products.html",
        context={"products_list": product_list}
    )


@app.get("/product_form", response_class=HTMLResponse)
def add_product(
    request: Request,
    name: str | None = None,
    price: float | None = None,
    location: str | None = None
):
    if name and price and location:
        new_product = {
            "nome": name,
            "price": price,
            "location": location
        }
        product_list.append(new_product)

    return templates.TemplateResponse(
        request=request,
        name="product_form.html"
    )

#funzione per accettare l'input del form
@app.post("/insert_product")
def insert_product(
    product:Annotated[Product,Form()]
):
   
   
    product_list.append(product.model_dump())
    return "Porduct added successfully"


#x: Annotated[dict[str,int,]] #è come una funzione con tanti parametri

@app.post("/insert_product_json")
def insert_product_json(
    product:Product
):
    print(product)


