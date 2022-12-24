def create():
    pass
def create(name, age, cpf='12', sex=True, ):
    pass
class People:

    def __init__(self, name, sex, age=True, cpf='000', ):
        self.name = name
        self.sex = sex
        self.age = age
        self.cpf = cpf