from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    title: str
    author: str


books: dict[int, Book] = {
    1: Book(title="The Hobbit", author="J.R.R. Tolkien"),
}
next_book_id = 2


@app.get("/")
def read_root():
    return {"message": "Book API is running"}


@app.get("/books", response_model=list[Book])
def list_books():
    return list(books.values())


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the book, or raise HTTP 404 if it does not exist.
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    # TODO: Assign a unique ID, store the book, and return it.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    # TODO: Replace the book, or raise HTTP 404 if it does not exist.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete the book, or raise HTTP 404 if it does not exist.
    raise NotImplementedError
