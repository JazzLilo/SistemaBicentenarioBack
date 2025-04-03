from pydantic import BaseModel

class UserLoginDTO(BaseModel):
    email: str
    password: str

class UserLogOutDTO(BaseModel):
    email: str
    
class UserUpdatePasswordDTO(BaseModel):
    old_password: str
    new_password: str
    
class UserResetPasswordDTO(BaseModel):
    new_password: str
    
class UserCodeDTO(BaseModel):
    code: str
    email: str
    
class UserDeactivateDTO(BaseModel):
    id: str