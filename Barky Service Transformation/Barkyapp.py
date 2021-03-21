import os

from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy



'''
setting up database file and the full path. and telling SQLAlchemy the database engine been used.
'''
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookmarkdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)



# add GET and POST methode to route decorator

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        table = tablename(tablename=request.form.get("tablename"))
        db.session.add(bookmark)
        db.session.commit()
       # bookmarks = bookmark.query.all()
    return render_template("home.html")

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)



