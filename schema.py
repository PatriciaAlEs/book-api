import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.book import Book
from models.book import db  # si tienes la instancia ahí

class BookType(SQLAlchemyObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(parent, info):
        return Book.query.all()

schema = graphene.Schema(query=Query)
