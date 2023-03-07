from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.authors import Author
from flask_app.models.books import Book

#______Author Render_____
@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def render_author():
    authors = Author.get_all()
    return render_template('index.html', authors=authors)

@app.route('/authors/create',methods=['POST'])
def create_author():
    data = {
        "name": request.form['name']
    }
    Author.create_author(data)
    return redirect('/authors')








@app.route('/author/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('show_author.html',author=Author.get_by_id(data),unfavorited_books=Book.unfavorited_books(data))

@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")