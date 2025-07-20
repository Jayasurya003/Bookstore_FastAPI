
# 📚 FastAPI Bookstore API

A simple REST API built with **FastAPI** to manage a bookstore. This project includes full CRUD functionality and demonstrates use of path/query parameters, Pydantic validation, and Pipenv for dependency management.

---

## 🚀 Features

- ✅ Get all books with optional author filtering
- ✅ Get a book by its ID
- ✅ Add a new book (with duplicate ID prevention)
- ✅ Update an existing book
- ✅ Delete a book
- ✅ Validation for rating (must be between 0 and 5)
- ✅ Price field included
- ✅ Built using Pipenv for clean dependency management

---

## 📦 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) (for development server)
- [Pipenv](https://pipenv.pypa.io/en/latest/) (for environment management)

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jayasurya003/Bookstore_FastAPI.git
cd Bookstore_FastAPI
````

### 2. Install dependencies using Pipenv

```bash
pipenv install
```

### 3. Activate the virtual environment

```bash
pipenv shell
```

---

## ▶️ Running the App

```bash
uvicorn main:app --reload
```

* Go to: `http://127.0.0.1:8000`
* Use the interactive docs: `http://127.0.0.1:8000/docs`

---

## 📬 API Endpoints

| Method | Endpoint           | Description                                 |
| ------ | ------------------ | ------------------------------------------- |
| GET    | `/books`           | Get all books (with optional author filter) |
| GET    | `/books/{book_id}` | Get one book by its ID                      |
| POST   | `/books`           | Add a new book                              |
| PUT    | `/books/{book_id}` | Update an existing book                     |
| DELETE | `/books/{book_id}` | Delete a book                               |

---

## 📌 Notes

* `rating` must be a float between `0` and `5` (validated with `confloat`)
* Prevents adding books with duplicate `id`
* Uses `Optional` fields like `description` and `rating` for flexibility

---

## 🧪 Future Improvements

* Add persistence (e.g., database integration)
* Add authentication
* Add pagination or search filtering

---
