from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

# SQLite INTRO - FILE BASED DB
#
#  You have to manually handle SQLAlchemy without the help of Flask-SQLAlchemy.
# 
# Step-by-Step:
#
# You need to manually create the engine and session.
# Queries are performed using the session object.
# You have to manage the session lifecycle (opening and closing the session).
#
# Key Points:
# 
# Session management: You have to manually open (session = Session()) and 
# close (session.close()) the session.
# Query execution: session.query(User).filter(User.name == 'Alice').all() 
# fetches the data.

app = Flask(__name__)

# Setup SQLAlchemy
engine = create_engine('sqlite:///instance/cafes.db')
Base = declarative_base()

# Define User model
class Cafe(Base):
    __tablename__ = 'cafe'
    id = Column(Integer, primary_key=True)
    location = Column(String)

# Create session factory
Session = scoped_session(sessionmaker(bind=engine))

# Query Example
@app.route('/locations')
def get_locations():
    # Open a session
    session = Session()

    # Query to get all cafes with location 'Peckham'
    cafe_location_peckham = session.query(Cafe).filter(Cafe.location == 'Peckham').all()

    # Close the session
    session.close()

    # Return the result (just as a string for simplicity)
    return ', '.join([cafe.location for cafe in cafe_location_peckham])
    
if __name__ == '__main__':
    app.run(debug=True)
