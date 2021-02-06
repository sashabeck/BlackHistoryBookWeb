from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

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



if __name__ == "__main__":
    app.run()

# Everything below is reference -----------------------------

'''
# enter anything into the url after /, it will repeat itself
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# calls the user function, passes in an argument for the parameter, <name>
@app.route('/admin')
def admin():
    return redirect(url_for("user", name="Admin!"))


# redirects back to the home page
@app.route("/admin")
def admin():
    return redirect(url_for("home"))
'''