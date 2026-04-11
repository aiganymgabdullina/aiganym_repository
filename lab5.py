from fastapi import FastAPI, HTTPException

app = FastAPI()
#1 esep
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        self._name = name.strip().title()
        email = email.lower()
        if "@" not in email:
            raise ValueError("Email must contain @")
        self._email = email

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

    def to_dict(self):
        return {"id": self._id, "name": self._name, "email": self._email}

    def __del__(self):
        print(f"User {self._name} deleted")


@app.get("/")
def home():
    return "Добро пожаловать в магазин!"


@app.get("/user/test")
def test_user():
    try:
        u = User(1, " john doe ", "John@Example.COM")
        return { "as_string": str(u),
            "as_json": u.to_dict() }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))