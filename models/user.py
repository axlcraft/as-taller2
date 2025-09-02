from __future__ import annotations  # 👈 habilita anotaciones diferidas
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:  # solo se evalúa en chequeo de tipos, no en runtime
    from models.task import Task
class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)

    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="user")

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

    def set_password(self, password: str) -> None:
        """Genera el hash de la contraseña antes de guardar"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verifica si la contraseña coincide con el hash almacenado"""
        return check_password_hash(self.password_hash, password)
