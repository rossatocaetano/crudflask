from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from models import People
from dao import PeopleDAO, UserDAO


app = Flask(__name__)
app.config.from_pyfile('config.py')


db= MySQL(app)


people_dao = PeopleDAO(db)
user_dao = UserDAO(db)


@app.route('/')
def index():
    people_list = people_dao.listar()
    return render_template('index.html', people=people_list)


@app.route('/newregister')
def newregister():
    return render_template('newregister.html')


@app.route('/createnewregister', methods = ['POST',])
def create_new_register():
    name = request.form['name']
    gender = request.form['gender']
    document = request.form['document']
    email = request.form['email']

    new_person = People(name, gender, document, email, id=None)
    people_dao.salvar(people = new_person)

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)