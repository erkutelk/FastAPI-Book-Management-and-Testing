from fastapi import FastAPI,Depends
from database import Base, engine
import model
from sqlalchemy.orm import Session
from database import get_db
from schemas import TodoUpdate,TodoCreate


app = FastAPI()
# Base.metadata.create_all(bind=engine)


@app.get('/book/{todo__id}',summary="Kitap bilgisini getir",tags=["Kitap İşlemleri"],description='Veritabanında bulunan bir adet kitabın bilgisini getiriri.')
def book_all(todo__id:int,db:Session = Depends(get_db)):
    books=db.query(model.Todo).filter(model.Todo.id==todo__id).first()
    return books


@app.get("/book-all",summary="Kitapları Listele",description="Veritabanında bulunan tüm kitap kayıtlarını getirir.",tags=["Kitap İşlemleri"])
def get_todos(db:Session = Depends(get_db)):
    todos=db.query(model.Todo).all()
    return todos


@app.post("/book-add",tags=["Kitap İşlemleri"],summary='Kitap ekle',description='Veritabanına yeni bir kitap ekle')
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):

    new_todo = model.Todo(title=todo.title,description=todo.description,completed=todo.completed)

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


@app.patch('/book-update/{todo_id}',tags=["Kitap İşlemleri"],description='Veritabanında bulunan kitabı güncelle',summary='Kitabı güncelle')
def book_update(todo_id:int,todo:TodoUpdate,db:Session=Depends(get_db)):
    book=db.query(model.Todo).filter(model.Todo.id==todo_id).first()

    if book is None:
        return {'massage':'kitap bilgisi bulunamadı'}

    if todo.title is not None:
        book.title=todo.title

    if todo.description is not None:
        book.description=todo.description

    if todo.completed is not None:
        book.completed=todo.completed

    db.commit()
    db.refresh(book)

    return book


@app.delete("/book-delete/{todo_id}",tags=["Kitap İşlemleri"],summary='Kita sil',description='Veritabanında bulunan kitabı sil')
def book_delete(todo_id:int,db:Session=Depends(get_db)):
    book=db.query(model.Todo).filter(model.Todo.id==todo_id).first()

    if book is None:
        return {"message":"Book info not found"}

    db.delete(book)
    db.commit ()
    return {"message":"Book delete successful"}
