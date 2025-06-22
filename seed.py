from app import app
from models.book import db, Book

libros = [
    Book(
        title="Cien años de soledad",
        author="Gabriel García Márquez",
        genre="Realismo mágico",
        year=1967,
        pages=417,
        language="Español",
        sinopsis="La historia de la familia Buendía en Macondo.",
        isbn="9780307474728"
    ),
    Book(
        title="1984",
        author="George Orwell",
        genre="Distopía",
        year=1949,
        pages=328,
        language="Inglés",
        sinopsis="Un régimen totalitario vigila todos tus movimientos.",
        isbn="9780451524935"
    ),
    Book(
        title="Orgullo y prejuicio",
        author="Jane Austen",
        genre="Romance",
        year=1813,
        pages=279,
        language="Inglés",
        sinopsis="Elizabeth Bennet y el Sr. Darcy luchan contra el orgullo y los prejuicios.",
        isbn="9780141040349"
    )
]

with app.app_context():
    db.session.query(Book).delete()  # Limpia antes de sembrar
    db.session.bulk_save_objects(libros)
    db.session.commit()
    print("📚 Base de datos poblada con libros de ejemplo.")
