from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List
app = FastAPI()



books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English"

    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Melé",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2020-01-19",
        "page_count": 1023,
        "language": "English"
    },
    {
        "id": 3,
        "title": "Flask Web Development",
        "author": "Miguel Grinberg",
        "publisher": "O'Reilly Media, Inc.",
        "published_date": "2018-03-20",
        "page_count": 256,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Learning JavaScript Design Patterns",
        "author": "Addy Osmani",
        "publisher": "O'Reilly Media, Inc.",
        "published_date": "2012-07-01",
        "page_count": 254,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Eloquent JavaScript",
        "author": "Marijn Haverbeke",
        "publisher": "No Starch Press",
        "published_date": "2018-12-04",
        "page_count": 472,
        "language": "English"
    },
    {
        "id": 6,
        "title": "You Don't Know JS Yet",
        "author": "Kyle Simpson",
        "publisher": "Independently published",
        "published_date": "2020-01-28",
        "page_count": 143,
        "language": "English"
    }, 
    {
        "id": 7,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_count": 544,
        "language": "English"
    },
    {
        "id": 8,
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "published_date": "2019-11-12",
        "page_count": 592,
        "language": "English"
    },
    {
        "id": 9,
        "title": "Effective Python",
        "author": "Brett Slatkin",
        "publisher": "Addison-Wesley Professional",
        "published_date": "2015-03-01",
        "page_count": 256,
        "language": "English"
    },
    {
        "id": 10,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English"
    }
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_books(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return {"message": "Book created successfully", "book": new_book}

@app.get("/books/{book_id}")
async def get_a_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.patch("/books/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language
            return {"message": "Book updated successfully", "book": book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
