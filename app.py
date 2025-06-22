from flask import Flask
from models.book import db
from flask_cors import CORS  # Por si usas frontend luego

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return "¡Bienvenida a tu API de libros!"

if __name__ == '__main__':
    app.run(debug=True)
