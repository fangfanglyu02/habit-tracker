# Habit Tracker - Full Stack Application / 习惯追踪器

>A full-stack habit tracking web app with creating new habit, habit toggle, and persistent storage.  
>一个用于培养习惯的Web应用， 支持习惯的创建、完成打卡、可持续储存。

## Screenshot / 界面预览

(add a screen shot later)

# Feature / 功能 
### English
- Create/ delete habits
- Mark habit as completed today
- Data persists across server restarts (SQLite)

### 中文
- 创建/删除习惯
- 标记今日完成
- 数据持久化储存 (SQLite)


# Upcoming Features
### English
- Undo Today's completion
- Total Completion count (never decreases)
- Last completed data tracking
- automatically resets `done` status each day

### 中文
- 撤销今日完成
- 累计完成次数 （只增不减）
- 记录最后完成日期
- 每日自动重置 `done` 状态

---
## Tech Stack/ 技术栈

| Layer | Technology |
|------|-----------|
| Backend | FastAPI with SQLAlchemy ORM, SQLite database |
| Frontend | HTML/CSS/Vanilla JS, RESTful API integration |
| API | RESTful, JSON |
|Deployment | (to be added) |

## Run Locally
>\'\'\'bash
git clone https://github.com/fangfanglyu02/habit-tracker.git <br>
cd habit-tracker <br>
python -m venv venv <br>
source venv/bin/activate        #Mac/Linux <br>
\# venv\Scripts\activate       # Windows <br>
pip install fastapi uvicorn sqlalchemy <br>
uvicorn main:app --reload
\'\'\'

Open browser:
http://localhost:8000/static

# API Endpoints / 接口文档
FastAPI auto-generated docs: http://localhost:8000/docs

| Method | Endpoint | Description|说明|
|----|---|---|---|
|GET|/habits|Get all habits|获取所有习惯｜
|POST|/habits?name=|Create a new habit |创建新习惯|
|PUT|/habits/{id}/toggle|Toggle completion status| 切换完成状态|
|DELETE|/habits/{id}|Delete a habit| 删除习惯|



# Future Improvements / 后续计划

# Author / 作者

Fangfang Lyu (Daisy) <br>
<a href = "https://github.com/fangfanglyu02"> Github </a>

