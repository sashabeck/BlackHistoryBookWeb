from flask import Flask, redirect, url_for, render_template, request
from bookList import books
import requests
import json
import csv

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    return render_template("index.html")

@app.route('/result/<genre>/<length>/<book>')
def success(genre, length, book):
    try:
        return render_template("submit.html", genre=genre, length=length, book=book)
    except:
        return "Failed while trying to render submit.html"

@app.route('/submitted',methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        genre = request.form["genreDropdown"]
        length = request.form["lengthDropdown"]
        chosenBooks = set()

        # find a random book that matches genre and length
        # go through the list of books, find books that match criteria, add to a set
        try:
            for book in books:
                try:
                    if (book['genre'] == genre):
                        if (length == 'Short' and book['length'] < 200):
                            chosenBooks.add(book['title'])
                        elif (length == 'Medium' and book['length'] >= 200 and book['length'] < 400):
                            chosenBooks.add(book['title'])
                        elif (length == 'Long' and book['length'] >= 400):
                            chosenBooks.add(book['title'])
                except:
                    return redirect(url_for("seterror", msg="Failed going into if"))
        except:
            return redirect(url_for("seterror", msg="Failed for and if"))
        try:
            boook = chosenBooks.pop()
            return redirect(url_for("success", genre=genre, length=length, book=boook))
        except:
            return "submit not working"

@app.route('/recommendations')
def recommendations():
    return render_template("recommendations.html")

@app.route('/lengtherror')
def lengtherror():
    return render_template("lengtherror.html")

@app.route('/seterror/<msg>')
def seterror(msg):
    return render_template("seterror.html", msg=msg)

@app.route('/my_list')
def my_list():
    return render_template("my_list.html")

@app.route('/movies')
def movies():
    return render_template("movies.html")

@app.route('/author_picks')
def author_picks():
    return render_template("author_picks.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/about')
def about():
    return render_template("about.html")