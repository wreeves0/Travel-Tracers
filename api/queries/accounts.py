from pydantic import BaseModel
from jwtdown_fastapi.authentication import Token


class DuplicateAccountError(ValueError):
    pass

class AccountIn(BaseModel):
    email:str
    password:str
    full_name:str

class AccountOut(BaseModel):
    id: str
    email: str
    full_name:str

class AccountToken(Token):
    account: AccountOut

class AccountOutWithPassword(AccountOut):
    hashed_password: str

class Queries:
    def get(self, email:str) -> AccountOutWithPassword:
        pass


    def create(self, info:AccountIn, hashed_password:str) -> AccountOutWithPassword:
        pass
