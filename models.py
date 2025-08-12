#imports
import uuid
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///data.db"
db = SQLAlchemy(app)
#create first class, create expense class.

class User(db.Model):
    ___tablename__ = "user"
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(10), nullable = False)
    sign_in_code = db.Column(db.String(4), unique = True, nullable = False, default= lambda: str(uuid.uuid4()))
    
#create a new table that allows for the sorting of participants based on the trip they're a part of. This way they can be part of multiple.
trip_participants = db.Table("trip_participants", db.Column('trip_id', db.Integer, db.ForeignKey('trip.id') ), db.Column('user_id', db.Integer, db.ForeignKey('user.id')))


class Trip(db.Model):
    ___tablename__ = "trip"
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(30), nullable = False)
    participants = db.relationship('User', secondary = trip_participants, backref= "trips")
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    join_code = db.Column(db.String(7), unique = True, nullable = False, default= lambda: str(uuid.uuid4()) )
    
    
    
class Expense(db.Model):
    ___tablename__ = 'expense'
    id = db.Column(db.Integer,primary_key= True)
    amount = db.Column(db.Float, nullable = False)
    description = db.Column(db.String(100))
    
    payer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))
    payer= db.relationship('User', backref= "expenses_paid")
    trip = db.relationship('Trip', backref= "expenses")
    

# @app.route("/")
# def index():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5001)