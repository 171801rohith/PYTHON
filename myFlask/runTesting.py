from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/FlaskTest"
# app.config["MONGO_URI"] = "mongodb://localhost:27017/Databasename"
db = PyMongo(app).db


@app.route("/")
def index():
    for i in range(5):
        db.inventory.insert_one(
            {"a": i, "b": i + 1, "c": i + 2}
        )  # Insert a document into the "inventory" collection
        # db.collectionName.insert_one({"a": i})
    return "Bro this is gonna be fun !!"


if __name__ == "__main__":
    app.run(debug=True)
