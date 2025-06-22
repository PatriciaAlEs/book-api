from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'year': self.year,
            'pages': self.pages,
            'language': self.language,
            'sinopsis': self.sinopsis,
            'isbn': self.isbn
        }