from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None
    is_active: bool = True
    
# create a user instance
user_data = {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
}

user = User(**user_data)
print(user)
print(user.model_dump())