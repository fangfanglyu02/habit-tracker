from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from datetime import date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./habits.db"
engine = create_engine(DATABASE_URL,
					   connect_args = {"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Habit(Base):
	__tablename__ = "habits"
	id = Column(Integer, primary_key=True) 
	name = Column(String, nullable=False)
	done = Column(Boolean, default=False)
	completion_counts = Column(Integer, default=0)
	last_completed_date = Column(Date, nullable=True)  # 最后完成日期
	previous_completed_date = Column(Date, nullable=True)
	created_at = Column(Date, default=date.today)   # 创建日期（可选）

	def __repr__(self):
			"""重载打印方法，用于调试"""
			return (f"<Habit(id={self.id}, name='{self.name}', done={self.done}, "
					f"completion_counts={self.completion_counts}, "
					f"last_completed_date={self.last_completed_date}, "
					f"previous_completed_date={self.previous_completed_date}, "
					f"created_at={self.created_at})>")

Base.metadata.create_all(bind=engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
