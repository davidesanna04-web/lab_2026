


from fastapi import FastAPI
from fastapi.responses import HTMLResponse
 
app=FastAPI()

@app.get("/", response_class=HTMLResponse)#parameto che specifica in che formato fastapi deve convertire ilr isultato
def home():



    html="""
    <!DOCTYPE html>
    <html>
        <body>
            <h1> Hello world! </h1>
            <p> This is a simple FastAPI app.</p>
        </body>
    </html>
    """
    
    return html 





