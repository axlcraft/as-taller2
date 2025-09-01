"""
Script de inicialización de la base de datos con datos de prueba
"""

from app import create_app, db
from models.task import Task
from datetime import datetime

# Crear la app con contexto
app = create_app()

with app.app_context():
    # 🔄 Opcional: limpiar y recrear las tablas
    db.drop_all()
    db.create_all()

    tasks_data = [
        ("Comprar leche y huevos", "Asegurarse de que sea leche deslactosada. Comprar una docena de huevos.", "2025-08-08 18:00:00"),
        ("Pagar la factura de Internet", "Vence este viernes 9 de agosto. Usar la aplicación del banco.", "2025-08-09 17:00:00"),
        ("Preparar presentación para el cliente A", "Revisar las diapositivas y los datos del último trimestre. Practicar la exposición.", "2025-08-12 10:00:00"),
        ("Llevar el coche al taller", "Hacer el cambio de aceite y la revisión de frenos.", "2025-08-01 10:00:00"),
        ("Llamar a María", "Preguntarle sobre el proyecto de la semana pasada.", "2025-08-06 14:30:00"),
        ("Limpiar la casa", "Aspirar, trapear y limpiar los baños.", "2025-08-04 12:00:00"),
        ("Estudiar para el examen de historia", "Capítulos 3 y 4. Enfocarse en la Revolución Industrial.", "2025-08-15 19:00:00"),
        ("Completar el informe mensual", "Recopilar todos los datos de ventas de julio y analizar los resultados.", "2025-08-10 16:00:00"),
        ("Planificar las vacaciones", "Buscar vuelos a la playa y opciones de hotel.", "2025-08-20 23:59:59"),
        ("Hacer ejercicio 30 minutos", "Correr en la caminadora o salir a trotar.", "2025-08-05 08:00:00"),
        ("Lavar la ropa", "Separar la ropa por colores y poner la lavadora.", "2025-08-07 09:00:00"),
        ("Revisar correo electrónico", "Borrar spam y responder los mensajes importantes.", "2025-08-03 10:00:00"),
        ("Comprar regalo para el cumpleaños de Ana", "Averiguar qué le gustaría a Ana para su cumpleaños.", "2025-08-18 10:00:00"),
        ("Leer 20 páginas del libro", "Continuar con el libro que empecé la semana pasada.", "2025-08-08 22:00:00"),
        ("Programar la publicación en redes sociales", "Crear un calendario de contenido para Instagram y Facebook.", "2025-08-11 12:00:00"),
        ("Actualizar mi CV", "Agregar los últimos proyectos y experiencia laboral.", "2025-07-30 15:00:00"),
        ("Organizar el escritorio", "Guardar papeles, limpiar la pantalla y ordenar cables.", "2025-08-07 15:00:00"),
        ("Investigar sobre nuevas tecnologías", "Leer artículos sobre IA y aprendizaje automático.", "2025-08-14 18:00:00"),
        ("Cenar con la familia", "Reservar en el restaurante italiano para el sábado.", "2025-08-09 20:00:00"),
        ("Configurar el nuevo software", "Instalar y configurar el software de diseño gráfico.", "2025-08-13 11:00:00"),
        ("Tarea de prueba #21", "Esta es una tarea de prueba adicional, sin descripción detallada.", "2025-08-08 10:00:00"),
        ("Tarea de prueba #22 (Vencida)", "Una tarea simple que debería aparecer como vencida.", "2025-08-01 10:00:00"),
        ("Tarea de prueba #23 (Completada)", "Una tarea que ya ha sido marcada como hecha.", "2025-07-28 12:00:00"),
        ("Tarea de prueba #24", "Otra tarea para llenar la base de datos.", "2025-08-16 14:00:00"),
        ("Tarea de prueba #25 (Vencida y Completa)", "Esta tarea ya pasó su fecha de vencimiento pero se completó.", "2025-08-02 18:00:00"),
    ]

    now = datetime.now()
    for title, desc, due_str in tasks_data:
        task = Task(
            title=title,
            description=desc,
            due_date=datetime.strptime(due_str, "%Y-%m-%d %H:%M:%S"),
        )
        db.session.add(task)

    db.session.commit()
    db.session.close()

    print("✅ Datos insertados correctamente en tasks.db")