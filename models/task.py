"""
Modelo Task - Representa una tarea en la base de datos

Este archivo contiene la definición del modelo Task usando SQLAlchemy ORM.
"""

from datetime import datetime
from extensions import db
from sqlalchemy import and_


class Task(db.Model):
    """
    Modelo para representar una tarea en la aplicación To-Do
    """

    # Nombre de la tabla en la base de datos
    __tablename__ = 'tasks'

    # Definición de columnas
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="tasks")

    def __init__(self, title, description=None, due_date=None, user_id=None):
        """
        Constructor del modelo Task

        Args:
            title (str): Título de la tarea
            description (str, optional): Descripción de la tarea
            due_date (datetime, optional): Fecha de vencimiento
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.user_id = user_id

    def __repr__(self):
        """Representación en string del objeto Task"""
        return f'<Task {self.id}: {self.title}>'

    def to_dict(self):
        """
        Convierte el objeto Task a un diccionario

        Returns:
            dict: Diccionario con los datos de la tarea
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def is_overdue(self):
        """
        Verifica si la tarea está vencida

        Returns:
            bool: True si la tarea está vencida, False en caso contrario
        """
        if self.due_date and not self.completed:
            return self.due_date < datetime.utcnow()
        return False

    @staticmethod
    def mark_completed(task):
        """Marca la tarea como completada"""
        task.completed = True
        task.updated_at = datetime.utcnow()
        Task.update_task(task)

    @staticmethod
    def mark_pending(task):
        """Marca la tarea como pendiente"""
        task.completed = False
        task.updated_at = datetime.utcnow()
        Task.update_task(task)

    @staticmethod
    def get_all_tasks(user_id):
        return Task.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_pending_tasks(user_id):
        return Task.query.filter_by(completed=False, user_id=user_id).all()

    @staticmethod
    def get_completed_tasks(user_id):
        return Task.query.filter_by(completed=True, user_id=user_id).all()

    @staticmethod
    def get_overdue_tasks(user_id):
        return Task.query.filter(
            and_(
                Task.due_date != None,                 # Verifica que due_date no sea NULL
                Task.due_date < datetime.utcnow(),     # Compara solo si tiene fecha
                Task.completed == False,               # completed debe estar en False
                Task.user_id == user_id                # Solo tareas del usuario
            )
        ).all()

    @staticmethod
    def sort_tasks_by_due_date(tasks):
        """
        Ordena una lista de tareas por fecha de vencimiento.

        Args:
            tasks (list): Lista de tareas a ordenar.

        Returns:
            list: Lista de tareas ordenadas por fecha de vencimiento.
        """
        return sorted(tasks, key=lambda x: x.due_date or datetime.min)

    @staticmethod
    def sort_tasks_by_title(tasks):
        """
        Ordena una lista de tareas por título.

        Args:
            tasks (list): Lista de tareas a ordenar.

        Returns:
            list: Lista de tareas ordenadas por nombre.
        """
        return sorted(tasks, key=lambda x: x.title)

    @staticmethod
    def sort_tasks_by_creation_date(tasks):
        """
        Ordena una lista de tareas por fecha de creación.

        Args:
            tasks (list): Lista de tareas a ordenar.

        Returns:
            list: Lista de tareas ordenadas por fecha de creación.
        """
        return sorted(tasks, key=lambda x: x.created_at)

    @staticmethod
    def get_task(task_id):
        """Obtiene una tarea por su ID"""
        return Task.query.get(task_id)

    @staticmethod
    def save(task):
        """Guarda la tarea en la base de datos"""
        db.session.add(task)
        db.session.commit()
        db.session.refresh(task)

    @staticmethod
    def delete_task(task_id):
        """Elimina la tarea de la base de datos"""
        task = Task.get_task(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
        return task

    @staticmethod
    def update_task(task):
        """Actualiza la tarea en la base de datos"""
        db.session.commit()
        db.session.refresh(task)
