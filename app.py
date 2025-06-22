from flask import Flask, jsonify, request
from flask_cors import CORS  
from models.book import db, Book  # 👈 importa el modelo aquí

app = Flask(__name__)
CORS(app)

# Configuración de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Ruta raíz
@app.route('/')
def home():
    return "¡Bienvenida a tu API de libros!"

# Ruta REST: obtener todos los libros
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.serialize() for book in books]), 200

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
