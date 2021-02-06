from flask import Flask, redirect, url_for, render_template, request
import requests
import json
app = Flask(__name__)
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=search+terms")
print(response.json())

# book_data is a list of data
book_data = json.loads(response.content)


@app.route('/', methods=['POST','GET'])
def home():
    return render_template("index.html")

@app.route('/result/<genre>/<length>')
def success(genre, length):
    return render_template("submit.html", genre=genre, length=length)

@app.route('/submitted',methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        genre = request.form["genreDropdown"]
        length = request.form["lengthDropdown"]
        return redirect(url_for("success", genre=genre, length=length))

@app.route('/recommendations')
def recommendations():
    return render_template("recommendations.html")

@app.route('/my_list')
def my_list():
    return render_template("my_list.html")

@app.route('/movies')
def movies():
    return render_template("movies.html")

@app.route('/author_picks')
def author_picks():
    return render_template("author_picks.html")

