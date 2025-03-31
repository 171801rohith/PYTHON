from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from passlib.context import CryptContext

app = Flask(__name__)
jwt = JWTManager()
app.config["MONGO_URI"] = "mongodb://localhost:27017/FlaskTest"
app.secret_key = "srdtyuiojpkpo65677929-0300hrvhfdsjkaiuvskabh"
db = PyMongo(app).db
pwd_context = CryptContext(schemes=["pbkdfd2_sha256"], deprecated="auto")
jwt.init_app(app)

#Config
JWT_SECRET_KEY =  "srdtyuiojpkpo65677929-0300hrvhfdsjkaiuvskabh"
JWT_TOKEN_LOCATION = ["header"]
JWT_INDENTITY_CLAIM = 'userId' #default is sub