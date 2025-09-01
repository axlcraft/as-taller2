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
            task = Task(
                title=request.form['title'],
                description=request.form['description'],
                due_date=datetime.strptime(request.form['due_date'].replace(
                    'T', ' '), "%Y-%m-%d %H:%M") if request.form['due_date'] else None
            )
            db.session.add(task)
            db.session.commit()
            db.session.close()
            flash('Tarea creada con éxito', 'success')
            return redirect(url_for('task_list'))
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
            request.form['title'] = task.title
            request.form['description'] = task.description
            request.form['due_date'] = task.due_date.isoformat(
            ) if task.due_date else ''
            db.session.commit()
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
        if not Task.delete_task(task_id):
            flash("Tarea no encontrada", "error")
        else:
            flash("Tarea eliminada con éxito", "success")
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
        pass  # TODO: implementar el método

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
