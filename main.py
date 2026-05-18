from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Habit, get_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def root():
	return {"message": "Habit Tracker with Database"}

@app.get('/habits')
def get_habits(db: Session = Depends(get_db)):
	habits = db.query(Habit).all()
	return habits

@app.post("/habits")
def create_habit(name: str, db: Session = Depends(get_db)):
	new_habit = Habit(name=name, done = False )
	db.add(new_habit)
	db.commit()
	db.refresh(new_habit)
	return new_habit

@app.delete("/habits/{habit_id}")
def delete_habit(habit_id:int, db: Session = Depends(get_db)):
	habit = db.query(Habit).filter(Habit.id == habit_id).first()
	if not habit:
		raise HTTPException(status_code = 404, detail = "Habit not found")
	db.delete(habit)
	db.commit()
	return {"message":"deleted"}

@app.put("/habits/{habit_id}/toggle")
def toggle_habit(habit_id:int, db:Session = Depends(get_db)):
	habit = db.query(Habit).filter(Habit.id == habit_id).first()
	if not habit:
		raise HTTPException(status_code = 404, detail = "Habit not found")
	habit.done = not habit.done
	db.commit()
	return habit