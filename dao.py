from models import People, User


SQL_DELETE_PERSON = 'delete from people where id = %s'
SQL_PERSON_BY_ID = 'SELECT id, name, gender, document, email from people where id = %s'
SQL_USER_BY_ID = 'SELECT id, nome, senha from user where id = %s'
SQL_UPDATE_PERSON = 'UPDATE people SET name=%s, gender=%s, document=%s, email=%s where id = %s'
SQL_SEARCH_PERSON = 'SELECT id, name, gender, document, email from people'
SQL_CREATE_PERSON = 'INSERT into people (name, gender, document, email) values (%s, %s, %s, %s)'


class PeopleDAO:
    def __init__(self, db):
        self.__db = db

    def salvar(self, people):
        cursor = self.__db.connection.cursor()

        if (people.id):
            cursor.execute(SQL_UPDATE_PERSON, (people.name, people.gender, people.document, people.email, people.id))
        else:
            cursor.execute(SQL_CREATE_PERSON, (people.name, people.gender, people.document, people.email))
            people.id = cursor.lastrowid
        self.__db.connection.commit()
        return people

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SEARCH_PERSON)
        people = translate_people(cursor.fetchall())
        return people

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PERSON_BY_ID, (id,))
        tuple = cursor.fetchone()
        return People(tuple[1], tuple[2], tuple[3], tuple[4], id=tuple[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETE_PERSON, (id, ))
        self.__db.connection.commit()


class UserDAO:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USER_BY_ID, (id,))
        dados = cursor.fetchone()
        user = translate_user(dados) if dados else None
        return user


def translate_people(people):
    def create_person_with_tuple(tuple):
        return People(tuple[1], tuple[2], tuple[3], tuple[4], id=tuple[0])
    return list(map(create_person_with_tuple, people))


def translate_user(tuple):
    return User(tuple[0], tuple[1], tuple[2])
