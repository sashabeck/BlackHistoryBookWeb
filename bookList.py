import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


books = [
    {'id': 0,
     'genre': 'Young Adult',
     'length': 444,
     'title': 'The Hate You Give',
     'author': 'Angie Thomas',
     'year_published': '2017',
     'summary': 'Sixteen-year-old Starr Carter moves between two worlds: the poor neighborhood where she lives and the fancy suburban prep school she attends. The uneasy balance between these worlds is shattered when Starr witnesses the fatal shooting of her childhood best friend Khalil at the hands of a police officer. Khalil was unarmed.'},

    {'id': 1,
     'genre': 'Romance',
     'length': 300,
     'title': 'Americanah',
     'author': 'Chimamanda Ngozi Adichie'
    },
    {'id': 2,
     'genre': 'Historical Fiction',
     'length': 305,
     'title': 'Homegoing',
     'author': 'Yaa Gyasi'},

     {'id': 3,
     'genre': 'Historical Fiction',
     'length': 343,
     'title': 'The Vanishing Half',
     'author': 'Brit Bennett'},

     {'id': 4,
     'genre': 'Fantasy',
     'length': 544,
     'title': 'Children of Blood and Bone',
     'author': 'Tomi Adeyemi'},

     {'id': 5,
     'genre': 'Nonfiction',
     'length': 426,
     'title': 'Becoming',
     'author': 'Michelle Obama'},

     {'id': 6,
     'genre': 'Contemporary',
     'length': 310,
     'title': 'Such a Fun Age',
     'author': 'Kiley Reid'},

     {'id': 7,
     'genre': 'Classic',
     'length': 304,
     'title': 'The Color Purple',
     'author': 'Alice Walker',
     'img_url' : 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1572261616l/52892857._SX318_SY475_.jpg'}


]
            