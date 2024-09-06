from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# PostgreSQL INTRO - Relational DB
# 
# This intro queries the cafes db in a local postgresql instance.
# The table (see instance/cafes.db) was exported from SQLite as a 
# CSV file and imported into postgresql. Make sure you have created
# a cafes database in the postgresql and has created the 'cafe' table 
# manually using pgAdmin using the information from SQLite.

app = Flask(__name__)

# Configure PostgreSQL database URI (server-based)
# Example URI: 'postgresql://username:password@localhost:5432/cafes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pwd37assor@localhost:5433/cafes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a Cafe model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80), nullable=False)

@app.route('/locations')
def get_locations():
    # Query all Cafes
    cafes = Cafe.query.all()
    return ', '.join([cafe.location for cafe in cafes])

if __name__ == '__main__':
    app.run(debug=True)
