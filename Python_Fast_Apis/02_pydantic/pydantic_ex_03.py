from pydantic import BaseModel, EmailStr, validator, ValidationError
from typing import List


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]
    
@validator("name")
def validate_name(cls, v):
    if len(v) < 3:
        raise ValueError("Name must be at least 3 characters long")
    return v

# Test with invalid data
try:
    invalid_user = UserWithAddress(
        id=3,
        name="A",  # Too short
        email="charlie@example.com",
        addresses=[{"street": "789 Pine Rd", "city": "Chicago", "zip_code": "60601"}],
    )
except ValidationError as e:
    print(e)