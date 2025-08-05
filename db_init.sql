-- Base de datos: SQLite
-- Script para crear la tabla 'tasks' y poblarla con datos de prueba

-- Parte 1: Crear la tabla `tasks`
CREATE TABLE tasks (
    id INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL,
    due_date DATETIME,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (id),
    CHECK (completed IN (0, 1))
);

-- Parte 2: Insertar tareas de prueba
INSERT INTO tasks (title, description, completed, due_date, created_at, updated_at) VALUES
('Comprar leche y huevos', 'Asegurarse de que sea leche deslactosada. Comprar una docena de huevos.', 0, '2025-08-08 18:00:00', datetime('now', '-3 days'), datetime('now', '-1 day')),
('Pagar la factura de Internet', 'Vence este viernes 9 de agosto. Usar la aplicación del banco.', 0, '2025-08-09 17:00:00', datetime('now', '-2 days'), datetime('now', '-1 day')),
('Preparar presentación para el cliente A', 'Revisar las diapositivas y los datos del último trimestre. Practicar la exposición.', 0, '2025-08-12 10:00:00', datetime('now', '-1 day'), datetime('now', '-1 day')),
('Llevar el coche al taller', 'Hacer el cambio de aceite y la revisión de frenos.', 1, '2025-08-01 10:00:00', datetime('now', '-10 days'), datetime('now', '-8 days')),
('Llamar a María', 'Preguntarle sobre el proyecto de la semana pasada.', 0, '2025-08-06 14:30:00', datetime('now', '-1 day'), datetime('now', '-1 day')),
('Limpiar la casa', 'Aspirar, trapear y limpiar los baños.', 1, '2025-08-04 12:00:00', datetime('now', '-5 days'), datetime('now', '-5 days')),
('Estudiar para el examen de historia', 'Capítulos 3 y 4. Enfocarse en la Revolución Industrial.', 0, '2025-08-15 19:00:00', datetime('now', '-2 days'), datetime('now', '-2 days')),
('Completar el informe mensual', 'Recopilar todos los datos de ventas de julio y analizar los resultados.', 0, '2025-08-10 16:00:00', datetime('now', '-2 days'), datetime('now', '-2 days')),
('Planificar las vacaciones', 'Buscar vuelos a la playa y opciones de hotel.', 0, '2025-08-20 23:59:59', datetime('now', '-4 days'), datetime('now', '-4 days')),
('Hacer ejercicio 30 minutos', 'Correr en la caminadora o salir a trotar.', 1, '2025-08-05 08:00:00', datetime('now', '-6 days'), datetime('now', '-6 days')),
('Lavar la ropa', 'Separar la ropa por colores y poner la lavadora.', 0, '2025-08-07 09:00:00', datetime('now', '-1 day'), datetime('now', '-1 day')),
('Revisar correo electrónico', 'Borrar spam y responder los mensajes importantes.', 1, '2025-08-03 10:00:00', datetime('now', '-7 days'), datetime('now', '-7 days')),
('Comprar regalo para el cumpleaños de Ana', 'Averiguar qué le gustaría a Ana para su cumpleaños.', 0, '2025-08-18 10:00:00', datetime('now', '-3 days'), datetime('now', '-3 days')),
('Leer 20 páginas del libro', 'Continuar con el libro que empecé la semana pasada.', 0, '2025-08-08 22:00:00', datetime('now', '-4 days'), datetime('now', '-4 days')),
('Programar la publicación en redes sociales', 'Crear un calendario de contenido para Instagram y Facebook.', 0, '2025-08-11 12:00:00', datetime('now', '-2 days'), datetime('now', '-2 days')),
('Actualizar mi CV', 'Agregar los últimos proyectos y experiencia laboral.', 1, '2025-07-30 15:00:00', datetime('now', '-12 days'), datetime('now', '-12 days')),
('Organizar el escritorio', 'Guardar papeles, limpiar la pantalla y ordenar cables.', 0, '2025-08-07 15:00:00', datetime('now', '-1 day'), datetime('now', '-1 day')),
('Investigar sobre nuevas tecnologías', 'Leer artículos sobre IA y aprendizaje automático.', 0, '2025-08-14 18:00:00', datetime('now', '-3 days'), datetime('now', '-3 days')),
('Cenar con la familia', 'Reservar en el restaurante italiano para el sábado.', 0, '2025-08-09 20:00:00', datetime('now', '-1 day'), datetime('now', '-1 day')),
('Configurar el nuevo software', 'Instalar y configurar el software de diseño gráfico.', 0, '2025-08-13 11:00:00', datetime('now', '-2 days'), datetime('now', '-2 days')),
('Tarea de prueba #21', 'Esta es una tarea de prueba adicional, sin descripción detallada.', 0, '2025-08-08 10:00:00', datetime('now', '-2 days'), datetime('now', '-2 days')),
('Tarea de prueba #22 (Vencida)', 'Una tarea simple que debería aparecer como vencida.', 0, '2025-08-01 10:00:00', datetime('now', '-15 days'), datetime('now', '-15 days')),
('Tarea de prueba #23 (Completada)', 'Una tarea que ya ha sido marcada como hecha.', 1, '2025-07-28 12:00:00', datetime('now', '-20 days'), datetime('now', '-20 days')),
('Tarea de prueba #24', 'Otra tarea para llenar la base de datos.', 0, '2025-08-16 14:00:00', datetime('now', '-1 day'), datetime('now', '-1 day')),
('Tarea de prueba #25 (Vencida y Completa)', 'Esta tarea ya pasó su fecha de vencimiento pero se completó.', 1, '2025-08-02 18:00:00', datetime('now', '-10 days'), datetime('now', '-5 days'));

