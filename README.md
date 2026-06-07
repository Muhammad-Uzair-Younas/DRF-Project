# Bookstore API

A RESTful Book Management API built with Django REST Framework that allows users to create, retrieve, update, delete, and search books.

## Features

* Create new books
* Retrieve all books
* Retrieve a single book by ID
* Update book information
* Partially update book records
* Delete books
* Search books by title or author
* JSON-based REST API
* SQLite database support

---

## Tech Stack

* Python 3.x
* Django
* Django REST Framework
* SQLite

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/bookstore-api.git
cd bookstore-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django djangorestframework
```

or

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Server will start at:

```text
http://127.0.0.1:8000/
```

---

## API Base URL

```text
http://127.0.0.1:8000/bookstore/
```

---

# API Endpoints

## Create Book

```http
POST /bookstore/books/
```

### Request Body

```json
{
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "isbn": "9780132350884",
    "price": 2500,
    "published_date": "2008-08-01"
}
```

### Response

```json
{
    "msg": "Data saved successfully"
}
```

---

## Get All Books

```http
GET /bookstore/books/
```

### Response

```json
[
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "isbn": "9780132350884",
        "price": 2500,
        "published_date": "2008-08-01"
    }
]
```

---

## Search Books

Search by title or author.

```http
GET /bookstore/books/?search=clean
```

Example:

```http
GET /bookstore/books/?search=martin
```

---

## Get Single Book

```http
GET /bookstore/books/1/
```

### Success Response

```json
{
    "id": 1,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "isbn": "9780132350884",
    "price": 2500,
    "published_date": "2008-08-01"
}
```

### Error Response

```json
{
    "error": "Book not found"
}
```

---

## Update Book

```http
PUT /bookstore/books/1/
```

### Request Body

```json
{
    "title": "Clean Code Updated",
    "author": "Robert C. Martin",
    "isbn": "9780132350884",
    "price": 3000,
    "published_date": "2008-08-01"
}
```

### Response

```json
{
    "msg": "Data updated successfully"
}
```

---

## Partial Update Book

```http
PATCH /bookstore/books/1/
```

### Request Body

```json
{
    "price": 3500
}
```

### Response

```json
{
    "msg": "Data updated successfully"
}
```

---

## Delete Book

```http
DELETE /bookstore/books/1/
```

### Response

```json
{
    "msg": "Data Deleted Successfully..."
}
```

---

## HTTP Methods Summary

| Method | Endpoint                         | Description          |
| ------ | -------------------------------- | -------------------- |
| POST   | `/bookstore/books/`              | Create a book        |
| GET    | `/bookstore/books/`              | Retrieve all books   |
| GET    | `/bookstore/books/?search=value` | Search books         |
| GET    | `/bookstore/books/<id>/`         | Retrieve single book |
| PUT    | `/bookstore/books/<id>/`         | Full update          |
| PATCH  | `/bookstore/books/<id>/`         | Partial update       |
| DELETE | `/bookstore/books/<id>/`         | Delete book          |

---

## Testing with Postman

### Create Book

```http
POST http://127.0.0.1:8000/bookstore/books/
```

### Get All Books

```http
GET http://127.0.0.1:8000/bookstore/books/
```

### Search Books

```http
GET http://127.0.0.1:8000/bookstore/books/?search=clean
```

### Get Single Book

```http
GET http://127.0.0.1:8000/bookstore/books/1/
```

### Update Book

```http
PUT http://127.0.0.1:8000/bookstore/books/1/
```

### Partial Update

```http
PATCH http://127.0.0.1:8000/bookstore/books/1/
```

### Delete Book

```http
DELETE http://127.0.0.1:8000/bookstore/books/1/
```

---

## Future Improvements

* JWT Authentication
* Pagination
* Sorting and Filtering
* Swagger/OpenAPI Documentation
* Docker Support
* PostgreSQL Integration
* Unit Testing

---

## Author

Muhammad Uzair Younas

Built using Django REST Framework.
