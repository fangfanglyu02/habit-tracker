from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
	return {"message": "Habit Tracker is running"}

@app.get('/hello')
def say_hello():
	return {"text": "Hi, SWE"}
