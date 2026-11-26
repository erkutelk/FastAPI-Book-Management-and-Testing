# engine	    :    Veritabanına bağlantı sağlar.
# SessionLocal	:    Yeni veritabanı oturumu oluşturur.
# add()	        :    Yeni kayıt eklemeye hazırlar.
# commit()	    :    Değişiklikleri kaydeder.
# close()	    :    Oturumu kapatır.
# Depends()	    :    Gerekli oturumu otomatik sağlar.

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL=os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

sesionLocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    db=sesionLocal()
    try:
        yield db
    finally:
        db.close()