from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "EduGenie",
        "message": "Welcome to EduGenie FastAPI!"
    }

@app.get("/ask")
def ask(question: str):
    return {
        "question": question,
        "answer": "This is a sample answer from EduGenie."
    }

@app.get("/summary")
def summary(text: str):
    return {
        "summary": text[:100]
    }

@app.get("/quiz")
def quiz(topic: str):
    return {
        "topic": topic,
        "question": f"What is {topic}?"
    }

@app.get("/recommend")
def recommend(topic: str):
    return {
        "recommendation": f"Learn the basics of {topic} and practice daily."
    }