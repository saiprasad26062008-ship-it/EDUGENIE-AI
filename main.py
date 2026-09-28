from dotenv import load_dotenv

# Load .env BEFORE importing other project modules
load_dotenv()

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations

load_dotenv()


app = FastAPI(
    title="EduGenie AI Learning Assistant"
)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


templates = Jinja2Templates(
    directory="templates"
)


class TextRequest(BaseModel):

    text: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/api/ask")
async def ask(data: TextRequest):

    return {
        "answer":
        answer_question(data.text)
    }


@app.post("/api/explain")
async def explain(data: TextRequest):

    return {
        "explanation":
        explain_topic(data.text)
    }


@app.post("/api/summarize")
async def summarize(data: TextRequest):

    return {
        "summary":
        summarize_text(data.text)
    }


@app.post("/api/quiz")
async def quiz(data: TextRequest):

    return {
        "quiz":
        generate_quiz(data.text)
    }


@app.post("/api/learning")
async def learning(data: TextRequest):

    return {
        "recommendations":
        get_learning_recommendations(data.text)
    }


@app.get("/health")
async def health():

    return {
        "status": "OK"
    }