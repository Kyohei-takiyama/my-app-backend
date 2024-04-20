from datetime import datetime
from uuid import uuid4

from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from core.config import get_env
from sqlalchemy.dialects.postgresql import UUID


# Engine の作成
Engine = create_engine(get_env().database_url, encoding="utf-8", echo=False)

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "users"
    user_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True,
        unique=True,
        nullable=False,
    )
    name = Column(String(50), nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)  # 追加分
    updated_at = Column(DateTime, default=datetime.now, nullable=False)  # 追加分
