from sqlalchemy import Column, BigInteger, String, Boolean, Integer, DateTime
from datetime import datetime
from app.core.database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(50))
    first_name = Column(String(100))
    is_vip = Column(Boolean, default=False)
    level = Column(Integer, default=1)
    points = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.utcnow)