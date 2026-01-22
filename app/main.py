from fastapi import FastAPI , Request , Form , UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from services.ingest import read_clean

from db.schema import create_table
from db.push import push_to_db

import pandas as pd

#create fastapi instance
app = FastAPI()

# create jinja instance
templates = Jinja2Templates(directory="templates")

#connect static files like templates directory
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.on_event("startup")
def startup():
    create_table()

@app.get("/")
def root():
    return {"user":"JASKIRAT",
            "message":"THIS IS MY PROJECT"}

# This is for displaying the html pages 
@app.get("/upload",response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request":request}
    )

# Post methid thus only opens when data is submitted from previous
@app.post("/uploaded",response_class=HTMLResponse)
def show_name(request: Request,file: UploadFile = File(...)) :

    df,errors = read_clean(file.file,file.filename)

    if errors:
         return templates.TemplateResponse(
            "result.html",
            {
                "request":request,
                "filename": None,
                "content_type": file.content_type,
                "error": errors
            }
        )
    
    else:

        try:
            push_to_db(df)
            length = len(df)
            cols = df.columns.to_list()
        except Exception as e:
            errors = str(e)

        return templates.TemplateResponse(
            "result.html",
            {
                "request":request,
                "filename": file.filename,
                "l":length,
                "cols":cols,
                "content_type": file.content_type,
                "error": errors
            }
        )

       