from fastapi import FastAPI
from typing import Optional ,List
from pydantic import BaseModel , confloat

app = FastAPI()

class Book(BaseModel):
    id:int
    title:str
    author:str
    description:Optional[str] = None
    rating:Optional[confloat(ge=0,le=5)] = None # type: ignore
    price:float

books:List[Book] = [] 


@app.get("/books")
def get_books(author:Optional[str]= None):
    all_Books = []
    if author:
        for i in books:
            if i.author.lower() == author.lower():
                all_Books.append(i)
        if all_Books:        
            return all_Books
        else:
            return {"Message": "No books found of this author"}
    else:
        return books

@app.post("/books")
def post_book(i:Book):
    for k in books:
        if k.id == i.id:
            return {"Message": f"This {k.id} is a duplicate id"}
    books.append(i)
    return{"Message" : "Successfully added a new book",'Book':i}

@app.get("/books/{book_id}")
def bookById(book_id:int):
    for i in books:
        if i.id == book_id:
            return i
    else:
        return {"Message": f"Book with {book_id} id is not found!!"}

@app.put("/books/{book_id}")
def update_book(book_id:int, updated_book:Book):
    for i in range(len(books)):
        if books[i].id == book_id:
            books[i] = updated_book
            return {"message":"Book updated successfully", "Updated Book": updated_book}
    return {"message": f"Book with id {book_id} not found"}

@app.delete("/books/{book_id}")

def delete_book(book_id: int):
    for i in range(len(books)):
        if books[i].id == book_id:
            del books[i]
            return {"Message": "Book deleted successfully"}
    return {"Message": f"Book not found with book id {book_id}"}

