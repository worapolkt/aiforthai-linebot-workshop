from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  app import service_main # main service router
from app import service_nlp # NLP service router
from fastapi.staticfiles import StaticFiles # For Vaja9

app = FastAPI(
    title="aiforthai-line-chatbot",
    description="AIFORTHAI LINE CHATBOT WORKSHOP",
    version="1.0.0",
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(service_main.router)

# Serve static files at the /static endpoint
app.mount("/static/", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    return "AIFORTHAI LINE CHATBOT WORKSHOP"
