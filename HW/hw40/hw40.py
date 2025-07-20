from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sadjkfbaskdgfalsgdksdfs'


menu = [
    {"name": "Главная", "url": "index"},
    {"name": "История", "url": "about"},
    {"name": "Популярность", "url": "top"},
    {"name": "Преимущества", "url": "privilege"},
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
                           title="Немного истории", menu=menu)


@app.route("/top")
def top():
    return render_template("top.html",
                           title="Популярность Python", menu=menu)


@app.route("/privilege")
def privilege():
    return render_template("privilege.html",
                           title="Преимущества Python", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
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
    app.run(debug=True)