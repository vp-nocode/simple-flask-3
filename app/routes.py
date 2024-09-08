from flask import render_template, request, redirect, url_for
from app import app


# posts = []
questionnaires = []

@app.route("/", methods=["GET", "POST"])
def index():
    # использует метод POST, так как информация будет отправляться.
    # Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
    # функция request.form извлекает значение из соответствующих полей
        # title = request.form.get('title')
        # content = request.form.get('content')
        user_name = request.form.get('user_name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        # создаёт условие для проверки наличия данных в полях title и content
        # if title and content:
        #    posts.append({'title': title, 'content': content})
        if user_name and age and city and hobby:
            questionnaires.append({'user_name': user_name, 'age': age, 'city': city, 'hobby': hobby})
        #использует для обновления страницы и предотвращения повторной отправки формы.
        return redirect(url_for('index'))
        # возвращает отрендеренный шаблон с переданными данными постов
    else:
        # return render_template('blog.html', posts=posts)
        return render_template('blog.html', questionnaires=questionnaires)