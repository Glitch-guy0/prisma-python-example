from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
def test_page():
    return {"condition": "working"}

@app.get("/")
def get_items():
    return []


@app.get('/create')
def create_item():
    return {}