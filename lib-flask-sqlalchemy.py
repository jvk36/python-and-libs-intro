from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLite INTRO - FILE BASED DB
#
# Compared to sqlalchemy, Flask-SQLAlchemy handles much of the setup for you, 
# including session management, so you can focus more on writing queries and 
# less on configuring things manually.
# 
# Step-by-Step:
#
# Flask-SQLAlchemy automatically handles session lifecycle and integrates with 
# Flask’s application context.
# You can write queries using the db.session provided by Flask-SQLAlchemy.
# Less boilerplate code is required.
#
# KEY POINTS - comparison to sqlalchemy lower level library:
# 
# No need to manually handle sessions: Flask-SQLAlchemy automatically provides 
# db.session and handles session lifecycle.
# Simpler query syntax: User.query.filter_by(name='Alice').all() is more concise 
# than session.query(User).filter(User.name == 'Alice').all().
# Session management is implicit: You don’t need to manually open or close the 
# session, as Flask-SQLAlchemy does it for you within the Flask request context.
# 
# Session Management - comparison to sqlalchemy lower level library:
#
# SQLAlchemy Direct: You need to manually manage the session (open, use, and close).
# Flask-SQLAlchemy: Session management is automatic, tied to the Flask app's context.
# 
# Querying Style:
#
# SQLAlchemy Direct: session.query(User) is the common way to start a query.
# Flask-SQLAlchemy: You can use User.query directly without needing to access a 
# session explicitly, simplifying the code.
#
# Boilerplate:
#
# SQLAlchemy Direct: Requires more setup code (creating engine, session, Base, etc.).
# Flask-SQLAlchemy: More concise and integrates seamlessly with Flask.

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'

# Setup Flask-SQLAlchemy
db = SQLAlchemy(app)

# Define Cafe model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80))

# Query Example
@app.route('/locations')
def get_locations():
    # Query to get all locations 'Peckham'
    cafe_location_peckham = Cafe.query.filter_by(location='Peckham').all()

    # Return the result (just as a string for simplicity)
    return ', '.join([cafe.location for cafe in cafe_location_peckham])

if __name__ == '__main__':
    app.run(debug=True)
