# 📚 Book API

Una API construida con Flask, SQLAlchemy y GraphQL para gestionar una colección de libros. Permite consultar, añadir, modificar y eliminar libros desde una base de datos SQLite a través de un endpoint GraphQL.

---

## 🚀 Tecnologías usadas

- Python 3.10
- Flask 3.1.1
- SQLAlchemy 2.0
- Graphene 2.1.9
- Flask-GraphQL 2.0.1
- SQLite (por defecto, puedes migrar a PostgreSQL)

---

## 🧩 Modelo de datos

```python
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(200), nullable=False)
    sinopsis = db.Column(db.Text, nullable=True)
    isbn = db.Column(db.String(50), unique=True, nullable=False)



 📦 Cómo ejecutar el proyecto

# Clonar el repositorio
git clone https://github.com/PatriciaAlEs/book-api.git

# Entrar al proyecto
cd book-api

# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la app
python app.py



✨ Próximamente -----> ✨

Endpoints REST completos

Filtro por género, autor y año

Guardar libros favoritos

Conexión con OpenLibrary API (maybe)



🖤 Desarrollado por
Patricia Álvarez — @PatriciaAlEs