from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>AI Career Guide</h1>

    <p>Welcome to our project!</p>

    <p>
        This application helps students
        find suitable career paths.
    </p>
    """

