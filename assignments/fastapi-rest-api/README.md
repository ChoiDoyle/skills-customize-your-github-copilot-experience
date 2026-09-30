# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage a collection of books. Practice defining HTTP endpoints, working with JSON data, validating request bodies with Pydantic, and returning appropriate status codes.

## 📝 Tasks

### 🛠️ Create the API and List Books

#### Description
Set up the FastAPI application and implement endpoints that confirm the service is running and return the available books.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn with `pip install fastapi uvicorn`.
- Start the application with `uvicorn main:app --reload`.
- Return a JSON response from `GET /` that confirms the API is running.
- Return the collection of books as JSON from `GET /books`.
- Open the interactive API documentation at `/docs` and use it to test both endpoints.

### 🛠️ Add and Retrieve Books

#### Description
Implement endpoints for retrieving one book by its ID and adding a new book to the collection. Use a Pydantic model to validate each book's title and author.

#### Requirements
Completed program should:

- Return the requested book from `GET /books/{book_id}`.
- Return an HTTP `404` response when the requested book ID does not exist.
- Create a book with `POST /books` using a JSON request body containing a title and author.
- Return the created book and an HTTP `201` response.
- Assign each new book a unique ID.

### 🛠️ Update and Delete Books

#### Description
Complete the book API by allowing an existing book to be updated or removed.

#### Requirements
Completed program should:

- Update a book with `PUT /books/{book_id}` using a JSON request body containing a title and author.
- Delete a book with `DELETE /books/{book_id}`.
- Return HTTP `404` when an update or delete request targets a book ID that does not exist.
- Verify successful and unsuccessful requests using `/docs` and the expected HTTP status codes.
