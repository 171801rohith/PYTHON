from flask import Flask, request
from flask_pymongo import PyMongo
from flask import render_template

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/FlaskTest"
# app.config["MONGO_URI"] = "mongodb://localhost:27017/Databasename"
db = PyMongo(app).db

class Database:
    def get_last_record():
        last_record = db.inventory.find().sort("ID", -1).limit(1)
        last_record = list(last_record)
        if last_record:
            print(last_record)
            return last_record[0]["ID"]
        return 100

    def increment():
        userid = Database.get_last_record()
        return  userid + 1

    @app.route('/')
    def index():
        return render_template("view_todos.html", title="Flask Test Collection")

    @app.route("/submit", methods=["POST"])
    def submit_data():
        # for i in range(2):
        #     db.inventory.insert_one(
        #         {"a": i, "b": i + 1, "c": i + 2}
        #     )  # Insert a document into the "inventory" collection
        #     # db.collectionName.insert_one({"a": i})
        username = request.form["name"]
        userphone = request.form["phone"]
        useraddress = request.form["address"]
        db.inventory.insert_one({ "ID": Database.increment() , "Name" : username, "Phone": userphone, "Address": useraddress})
        return render_template("view_todos.html", title="Flask Test Submitted")
    
    @app.route("/find", methods=["POST"])
    def find_data():
        name = request.form["name"]
        data = db.inventory.find({})
        # print(type(data))
        for ditem in data:
            if(ditem["Name"] == name):
                print(ditem)

        return "Not Found"

if __name__ == "__main__":
    app.run(debug=True)
