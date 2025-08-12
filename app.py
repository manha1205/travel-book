from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

from models import * 

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        
    app.run(debug=True, host="0.0.0.0", port=5001)