from flask import render_template, request, redirect, url_for, flash
from models import People
from dao import PeopleDAO, UserDAO
from main import db, app


people_dao = PeopleDAO(db)
user_dao = UserDAO(db)


# --- READ ---
# 1- Recupera os registros do banco de dados e retorna a página "index.html"
@app.route('/')
def index():
    people_list = people_dao.listar()
    return render_template('index.html', people=people_list)


# --- CREATE ---
# 1- Retorna a página "newregister.html"
@app.route('/newregister')
def newregister():
    return render_template('newregister.html')


# 2- Seleciona os dados inseridos no forumário da página "newregister.html" pelo usuário e registra no banco de dados
@app.route('/createnewregister', methods = ['POST',])
def create_new_register():
    name = request.form['name']
    gender = request.form['gender']
    document = request.form['document']
    email = request.form['email']
    new_person = People(name, gender, document, email, id=None)
    people_dao.salvar(people = new_person)
    flash('Register created!!!')
    return redirect(url_for('index'))


# --- UPDATE ---
# 1- Seleciona o registro que o usuário deseja editar pelo id e retorna a página "edit.html"
@app.route('/edit/<int:id>')
def edit(id):
    update_person = people_dao.busca_por_id(id)
    return render_template('edit.html', people=update_person)


# 2- Seleciona os dados inseridos no formulário da página "edit.html" e realiza a atualização do registro no banco de dados 
@app.route('/update', methods=['POST',])
def update():
    name = request.form['name']
    gender = request.form['gender']
    document = request.form['document']
    email = request.form['email']
    update_person = People(name, gender, document, email, id=request.form['id'])
    people_dao.salvar(update_person)
    flash('Register updated!!!')
    return redirect(url_for('index'))


# --- DELETE ---
# 1- Seleciona o registro que o usuário deseja deletar na página "index.html" pelo id e redireciona para mesma página
@app.route('/delete/<int:id>')
def delete(id):
    people_dao.deletar(id)
    flash('Register deleted!!!')
    return redirect(url_for('index'))