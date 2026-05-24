from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Habit, get_db
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from datetime import date, timedelta

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def root():
	return FileResponse('static/index.html')

@app.get('/habits')
def get_habits(db: Session = Depends(get_db)):
    habits = db.query(Habit).all()
    return habits

@app.post("/habits")
def create_habit(name: str, db: Session = Depends(get_db)):

	new_habit = Habit(
        name=name,  # 这个有值
        done=False,  # 明确设置，不要依赖默认值
        completion_counts=0,  # 明确设置
        last_completed_date=None,
        previous_completed_date=None,
        created_at=date.today()  # 明确设置今天日期
    )
	
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
	today = date.today()
	completed_today = habit.last_completed_date == today
	if(completed_today):
		#habit.done = False
		habit.last_completed_date = habit.previous_completed_date
		habit.completion_counts = max(0, habit.completion_counts-1)
	else:
		#habit.done = True
		habit.last_completed_date = today
		habit.completion_counts+=1

	db.commit()
	db.refresh(habit)
	return habit