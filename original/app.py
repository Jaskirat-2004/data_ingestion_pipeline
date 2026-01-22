from fastapi import FastAPI , Request , Form , UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from enum import Enum
import pandas as pd 

from fastapi.staticfiles import StaticFiles

# Enumerator class creates objects
class Fruits(str,Enum):
    apple = "apple"
    banana = "banana"
    orange = "orange"

#create fastapi instance
app = FastAPI()

# create jinja instance
templates = Jinja2Templates(directory="templates")

#connect static files like templates directory
app.mount("/static",StaticFiles(directory="static"),name="static")


@app.get("/")
def root():
    return {"message":"Hello World",
            "NAME":"JASKIRAT"}

@app.get("/id/me")
async def display():
    return {
        "id":0000,
        "user":"CURRENTLY RUNNING"
    }

# parameters
@app.get("/id/{emp_id}")
async def display(emp_id:int):
    if emp_id == 2004:
        return {
            "id":emp_id,
            "message":"HELLO MASTER"
        }
    else:
        return {
            "id":emp_id,
            "message":"HELLO USER"
        }
    
l1 = [1,2,3,4,5,6,7]
# querry paramerters
@app.get("/query")
def read_l1(start:int,end:int):
    return l1[start:end]

# enumerators as params thus can select only them
@app.get("/fruit/{fruit_name}")
async def display(fruit_name:Fruits):
    if fruit_name is Fruits.apple:
        return {"name":fruit_name,"message":"i wanna eat apples"}
    if fruit_name.value=="banana":
        return {"name":fruit_name,"message":"i wanna eat bananas"}
    return {"name":fruit_name,"message":"i wanna eat oranges"}

# This is for displaying the html pages 
@app.get("/upload",response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request":request}
    )

# Post methid thus only opens when data is submitted from previous
@app.post("/data",response_class=HTMLResponse)
def show_name(request: Request,username: str = Form(...),age:int | None = Form(None),file: UploadFile = File(...)) :

    if file.filename.endswith((".xlsx",".csv")):
        if file.filename.endswith(".xlsx"):
            df = pd.read_excel(file.file)
        else:
            df = pd.read_csv(file.file)
        print(df.head())
        return templates.TemplateResponse(
            "result.html",
            {
                "request":request,
                "username":username,
                "age":age,
                "filename": file.filename,
                "content_type": file.content_type,
                "error": None
            }
        )
    else:
        return templates.TemplateResponse(
            "result.html",
            {
                "request":request,
                "username":username,
                "age":age,
                "filename": None,
                "content_type": file.content_type,
                "error": "Only EXCEL FILES ARE ALLOWED"
            }
        )


