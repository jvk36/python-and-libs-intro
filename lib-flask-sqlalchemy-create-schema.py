from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# *****************************************************************************
# Steps:
# 1. Create a sqlite database new-books-collection.db in the instance
#    subdirectory. 
# 2. Create a table in the database calls books.
# 3. The books table should contain 4 fields: id, title, author and rating. The 
#    fields should have the same limitations as before 
#    e.g. INTEGER/FLOAT/VARCHAR/UNIQUE/NOT NULL etc.
# 4. Provide the Flask "app context" and create the schema in the database.
# 5. With the flask app context, add a new row in the books table
#
# NOTE 1: You can always check the database using DB Browser Windows 
#         Application.
# NOTE 2: The URL for the database is "sqlite:///new-books-collection.db"
# NOTE 3: If you run the file more than once, it will cause an integrity error
#         as id is a PRIMARY KEY. 
# NOTE 4: create_all does not update tables if they are already in the 
#         database. If you change a model’s columns, use a migration library 
#         like Alembic with Flask-Alembic or Flask-Migrate to generate 
#         migrations that update the database schema. 
# *****************************************************************************

app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
