from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books.db')
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_book1 = Book(title='1984', author='George', pages=300)
new_book2 = Book(title='hello', author='john', pages=234)
session.add_all([new_book1, new_book2])
session.commit()

books = session.query(Book).all()
for B in books:
    print(B.title, B.author, B.pages)

book = session.query(Book).filter_by(title='1984').first()
print(book.title, book.author, book.pages)
