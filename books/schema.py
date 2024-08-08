import graphene

from graphene_django import DjangoObjectType
from .models import *

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)

    def resolve_all_books(root, info):
        return Book.objects.select_related('author').all()
    
    def resolve_all_authors(root, info):
        return Author.objects.prefetch_related('books').all()
    
schema = graphene.Schema(query = Query)

