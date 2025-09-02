"""
Controlador de Tareas - Maneja la lógica de negocio de las tareas

Este archivo contiene todas las rutas y lógica relacionada con las tareas.
Representa la capa "Controlador" en la arquitectura MVC.
"""

from flask import render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
from models.task import Task
from extensions import db


def register_routes(app):
    """
    Registra todas las rutas del controlador de tareas en la aplicación Flask

    Args:
        app (Flask): Instancia de la aplicación Flask
    """

    @app.route('/')
    def index():
        """
        Ruta principal - Redirige a la lista de tareas

        Returns:
            Response: Redirección a la lista de tareas
        """
        return redirect(url_for('task_list'))

    @app.route('/tasks')
    def task_list():
        """
        Muestra la lista de todas las tareas

        Query Parameters:
            filter (str): Filtro para mostrar tareas ('all', 'pending', 'completed')
            sort (str): Ordenamiento ('date', 'title', 'created')

        Returns:
            str: HTML renderizado con la lista de tareas
        """
        # Obtener parámetros de filtro y ordenamiento
        filter_type = request.args.get('filter', 'all')
        sort_by = request.args.get('sort', 'created')

        tasks = filter_tasks(filter_type)
        tasks = sort_tasks(sort_by, tasks)


        # Datos para pasar a la plantilla
        context = {
            'tasks': tasks,
            'filter_type': filter_type,
            'sort_by': sort_by,
            'total_tasks': len(tasks),
            'pending_count': len(Task.get_pending_tasks()),
            'completed_count': len(Task.get_completed_tasks())
        }

        return render_template('task_list.html', **context)

    def validate_task_form(form_data):
        errors = []

        # Validar título
        title = form_data.get("title", "").strip()
        if not title:
            errors.append("El título es obligatorio.")
        elif len(title) > 200:
            errors.append("El título no puede superar los 200 caracteres.")

        # Validar fecha (si se proporciona)
        due_date_str = form_data.get("due_date")
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.fromisoformat(due_date_str)
            except ValueError:
                errors.append("La fecha de vencimiento no es válida.")

        return errors, title, form_data.get("description", ""), due_date

    @app.route('/tasks/new', methods=['GET', 'POST'])
    def task_create():
        """
        Crea una nueva tarea

        GET: Muestra el formulario de creación
        POST: Procesa los datos del formulario y crea la tarea

        Returns:
            str: HTML del formulario o redirección tras crear la tarea
        """
        if request.method == 'POST':
            form_data = request.form
            errors, title, description, due_date = validate_task_form(form_data)
            if errors:
                for err in errors:
                    flash(err, "error")
                return render_template("task_form.html", task=None)

            new_task = Task(title=title, description=description, due_date=due_date)
            Task.save(new_task)
            flash("Tarea creada con éxito", "success")
            return redirect(url_for("task_list"))
        elif request.method == 'GET':
            return render_template('task_form.html', action='Crear')

    @app.route('/tasks/<int:task_id>', methods=['GET', 'POST'])
    def task_detail(task_id):
        """
        Muestra los detalles de una tarea específica

        Args:
            task_id (int): ID de la tarea a mostrar

        Returns:
            str: HTML con los detalles de la tarea
        """
        task = Task.get_task(task_id)
        if not task:
            flash('Tarea no encontrada', 'error')
            return redirect(url_for('task_list'))
        return render_template('task-detail.html', task=task)

    @app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
    def task_edit(task_id):
        """
        Edita una tarea existente

        Args:
            task_id (int): ID de la tarea a editar

        GET: Muestra el formulario de edición con datos actuales
        POST: Procesa los cambios y actualiza la tarea

        Returns:
            str: HTML del formulario o redirección tras editar
        """
        task = Task.get_task(task_id)
        if not task:
            flash('Tarea no encontrada', 'error')
            return redirect(url_for('task_list'))

        if request.method == 'POST':
            if request.method == 'POST':
                form_data = request.form.to_dict()

                # Asignar los valores del form al objeto
                task.title = form_data.get('title', task.title)
                task.description = form_data.get(
                    'description', task.description)
                task.due_date = format_date(form_data.get(
                    'due_date')) if form_data.get('due_date') else None
                task.completed = False if 'completed' not in form_data else True

                Task.update_task(task)
                flash('Tarea actualizada con éxito', 'success')
                return redirect(url_for('task_detail', task_id=task.id))
        elif request.method == 'GET':
            return render_template('task_form.html', action='Editar', task=task)

    @app.route('/tasks/<int:task_id>/delete', methods=['POST'])
    def task_delete(task_id):
        """
        Elimina una tarea

        Args:
            task_id (int): ID de la tarea a eliminar

        Returns:
            Response: Redirección a la lista de tareas
        """
        Task.delete_task(task_id)
        return redirect(url_for('task_list'))

    @app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
    def task_toggle(task_id):
        """
        Cambia el estado de completado de una tarea

        Args:
            task_id (int): ID de la tarea a cambiar

        Returns:
            Response: Redirección a la lista de tareas
        """
        task = Task.get_task(task_id)
        if task:
            if task.completed:
                Task.mark_pending(task)
            else:
                Task.mark_completed(task)
        return redirect(url_for('task_list'))

    # Rutas adicionales para versiones futuras

    @app.route('/api/tasks', methods=['GET'])
    def api_tasks():
        """
        API endpoint para obtener tareas en formato JSON
        (Para versiones futuras con JavaScript)

        Returns:
            json: Lista de tareas en formato JSON
        """
        # TODO: para versiones futuras
        return jsonify({
            'tasks': [],
            'message': 'API en desarrollo - Implementar en versiones futuras'
        })

    @app.errorhandler(404)
    def not_found_error(error):
        """Maneja errores 404 - Página no encontrada"""
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Maneja errores 500 - Error interno del servidor"""
        db.session.rollback()
        return render_template('500.html'), 500


def filter_tasks(filter_type):
    """
    Filtra la lista de tareas según el tipo de filtro.

    Args:
        filter_type (str): Tipo de filtro ('pending', 'completed', 'overdue', 'all').

    Returns:
        list: Lista de tareas filtradas.
    """
    if filter_type == 'pending':
        return Task.get_pending_tasks()
    elif filter_type == 'completed':
        return Task.get_completed_tasks()
    elif filter_type == 'overdue':
        return Task.get_overdue_tasks()
    return Task.get_all_tasks()


def format_date(date):
    """
    Formatea una fecha en un string legible.

    Args:
        date (datetime): Fecha a formatear.

    Returns:
        str: Fecha formateada.
    """
    if date:
        return datetime.fromisoformat(date.replace('T', ' '))
    return None

def sort_tasks(sort_type, tasks):
    """
    Ordena una lista de tareas según el tipo de ordenamiento.

    Args:
        tasks (list): Lista de tareas a ordenar.
    """
    if sort_type == 'date':
        return Task.sort_tasks_by_due_date(tasks)
    elif sort_type == 'title':
        return Task.sort_tasks_by_title(tasks)
    elif sort_type == 'created_at':
        return Task.sort_tasks_by_creation_date(tasks)
    return tasks
