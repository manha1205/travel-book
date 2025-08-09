#imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///data.db"
db = SQLAlchemy(app)
#create first class, create expense class.

class user(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(10), nullable = False)
    
with app.app_context():
    db.create_all()
# class expenses(db.Model):
    # id
    # payer
    
    

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)