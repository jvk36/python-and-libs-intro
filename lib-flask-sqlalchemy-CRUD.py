from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# *****************************************************************************
# The program assumes lib-flask-sqlalchemy-create-schema.py was run first to
# create the new-books-collection.db. That program also inserts one row into
# the books table.
# *****************************************************************************

# *****************************************************************************
# Steps:
# 1. Create a new row. 
# 2. Read all the records. Use result.scalars for multiple rows.
# 3. Read a single record. Use result.scalar for single row.
# 4. 
#
# NOTE 1: When creating new rows, the PRIMARY KEY field is optional. The id 
#         field is auto-generated, if not supplied.
# NOTE 2: Flask-SQLAlchemy also has some handy extra query methods like 
#         get_or_404() that we can use. Since Flask-SQLAlchemy version 3.0 the 
#         previous query methods like Book.query.get() have been deprecated.
# NOTE 3: The table definition is the same as in lib-flask-sqlalchemy-create-schema.py
#         Importing will not work as it executes the whole file which is not what
#         we want.
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

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    # add a new row
    new_book = Book(title="Profiting from Hedge Funds", author="John Vincent", rating=9.8)
    db.session.add(new_book)
    db.session.commit()
    # read all rows
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    # read a single row
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    # update a row by query
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit() 
    # update a row by PRIMARY KEY
    book_id = 1
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()  
    # delete a row using PRIMARY KEY
    book_id=2
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()


