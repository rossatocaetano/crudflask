class People:
    def __init__ (self, name, gender, document, email, id=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.document = document
        self.email = email

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password