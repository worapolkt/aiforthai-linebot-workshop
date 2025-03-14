from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  app import service_main # main service router

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


@app.get("/")
def index():
    return "AIFORTHAI LINE CHATBOT WORKSHOP"
