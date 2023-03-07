from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.authors import Author
from flask_app.models.books import Book


@app.route('/books')
def render_book():
    books = Book.get_all()
    return render_template('books.html', books=books)


@app.route('/books/create', methods=['post'])
def create_book():
    Book.create(request.form)
    return redirect('/books')



@app.route('/book/<int:id>')
def show_book(id):
    data = {
        "id":id
    }
    return render_template('show_book.html',book=Book.get_by_id2(data),unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")



