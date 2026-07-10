from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "feature": "",
            "result": ""
        }
    )


@app.post("/qna", response_class=HTMLResponse)
async def qna(request: Request, question: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "feature": "Question Answering",
            "result": answer_question(question)
        }
    )


@app.post("/explain", response_class=HTMLResponse)
async def explain(request: Request, topic: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "feature": "Explanation",
            "result": explain_topic(topic)
        }
    )


@app.post("/quiz", response_class=HTMLResponse)
async def quiz(request: Request, topic: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "feature": "Quiz Generation",
            "result": generate_quiz(topic)
        }
    )


@app.post("/summary", response_class=HTMLResponse)
async def summary(request: Request, text: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "feature": "Summarization",
            "result": summarize_text(text)
        }
    )


@app.post("/recommend", response_class=HTMLResponse)
async def recommend(request: Request, topic: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "feature": "Learning Recommendations",
            "result": recommend_learning(topic)
        }
    )
