
from pydantic import BaseModel
class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool = False
    # ------ Kullanıcının apiye verileri gönderirken nasıl olması gerektiğini söylüyor

class TodoUpdate(BaseModel):
    title: str | None=None
    description:str | None=None
    completed:bool |None=None
