import sqlite3
import os
from flask import Flask, render_template, flash, request, g

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'fc3cc2c1df6f31308e1f0acfff869a6306905117'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "flsk.db")))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"}
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
                           title="Главная", menu=menu)


@app.route("/about")
def about():
    return render_template("manual.html",
                           title="О нас", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        # print(request.form)
        # print(request.form['username'])
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно!", category='success')
        else:
            flash("Ошибка отправки", category='error')
    return render_template("contact.html",
                           title="Обратная связь", menu=menu)


@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page404.html",
                           title="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run()