from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    Text,
    DateTime,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import get_env
from sqlalchemy.dialects.postgresql import UUID


database_url: str = get_env().DATABASE_URL
if database_url is None:
    raise ValueError("DATABASE_URL is not set.")
# Engine の作成
Engine = create_engine(database_url, echo=False)

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
    # ユーザーに関連するTodoアイテムへのリレーションシップ
    todos = relationship("Todo", back_populates="user")


class Todo(BaseModel):
    __tablename__ = "todos"
    todo_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True,
        unique=True,
        nullable=False,
    )
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=False, default="")
    status = Column(Text, nullable=False, default="incomplete")
    due_date = Column(DateTime, nullable=False)
    priority = Column(Integer, nullable=False, default=0)
    tags = Column(Text, nullable=False, default="")
    is_archived = Column(Boolean, nullable=False, default=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)
    # Userオブジェクトへの参照
    user = relationship("User", back_populates="todos")
