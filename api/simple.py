from fastapi import FastAPI, Query, Request


app = FastAPI()


@app.get('/')
def root():
    params = {
        "greeting": """
    Hello,
    Welcome to your To do list for your trip in XMas"""
    }
    return params.get("greeting")
