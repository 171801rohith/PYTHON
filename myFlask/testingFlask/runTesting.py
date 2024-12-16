from flask import Flask, request, flash, redirect, url_for
from flask_pymongo import PyMongo
from flask import render_template

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/FlaskTest"
# app.config["MONGO_URI"] = "mongodb://localhost:27017/Databasename"
db = PyMongo(app).db
app.secret_key = "Rohith_171801"


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
        return userid + 1

    @app.route("/")
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
        userid = Database.increment()
        db.inventory.insert_one(
            {
                "ID": userid,
                "Name": username,
                "Phone": userphone,
                "Address": useraddress,
            }
        )
        flash(f"Successfully submitted. Your UserID is {userid}. Remember it! :)")
        return redirect(url_for("index"))

    @app.route("/find", methods=["POST"])
    def find_data():
        name = request.form["name"]
        data = db.inventory.find_one({"Name": name})
        if data:
            return f"ID : {data["ID"]}, NAME: {data["Name"]}, PHONE: {data["Phone"]}, Address: {data["Address"]}"

        # print(type(data))
        # for ditem in data:
        #     if ditem["Name"] == name:
        #         return f"ID : {ditem["ID"]}, NAME: {ditem["Name"]}, PHONE: {ditem["Phone"]}, Address: {ditem["Address"]}"

        return "Not Found"

    @app.route("/delete", methods=["POST"])
    def delete_data():
        name = request.form["name"]
        data = db.inventory.find({})
        # print(type(data))
        for ditem in data:
            if ditem["Name"] == name:
                item = ditem
                db.inventory.delete_one(ditem)
                return f"ID : {item["ID"]}, NAME: {item["Name"]}, PHONE: {item["Phone"]}, Address: {item["Address"]} has been deleted"

        return "Not Found"

    @app.route("/update", methods=["POST"])
    def update_data():
        item = 0
        updateItem = 0
        id = int(request.form["id"])
        name = request.form["name"]
        phone = request.form["phone"]
        address = request.form["address"]
        data = db.inventory.find({})
        # print(type(data))
        for ditem in data:
            if ditem.get("ID") == id:
                item = ditem
                db.inventory.update_one(
                    {"ID": id},
                    {"$set": {"Name": name, "Phone": phone, "Address": address}},
                    upsert=False,
                )

        updateItem = db.inventory.find_one({"ID": id})
        if updateItem:
            return f"ID : {item["ID"]}, NAME: {item["Name"]}, PHONE: {item["Phone"]}, Address: {item["Address"]} has been updated to ID : {updateItem["ID"]}, NAME: {updateItem["Name"]}, PHONE: {updateItem["Phone"]}, Address: {updateItem["Address"]}"

        return "Not Found"

    @app.route("/flashy")
    def pop_up():
        flash("Bro this is flashy flash!")
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
