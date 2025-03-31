from typing import Optional
from fastapi import Depends, HTTPException, status, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import timedelta, datetime
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "a15562c29b56413d12dab4a85835f98445a30aecd9bb85ec3112e63d457c1a28"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINTUES = 15

fake_db = {
    "tim": {
        "username": "tim",
        "age": 16,
        "email": "tim@mail.net",
        "hashed_password": "",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None
    age: Optional[str] = None
    disabled: Optional[bool] = None


class userInDB(User):
    hasehed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_schema = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def verify_password(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)


def generate_hashed_password(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return userInDB(**user_data)


def authenticate_user(db, username: str, pwd: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(pwd, user.hasehed_password):
        return False

    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expires = datetime.now() + expires_delta
    else:
        expires = datetime.now() + timedelta(minutes=15)

    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth_2_schema)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Couldn't validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise credential_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = get_user(db, username=token_data.username)
    if not user:
        raise credential_exception

    return user


async def get_current_active_user(current_user: str = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive User"
        )
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data=OAuth2PasswordRequestForm):
    pass
