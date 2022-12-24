from marshmallow import Schema, fields
from SchemaInformation import SchemaInformation
from CodeGenerator import CodeGenerator

class People(Schema):
    name = fields.Str()
    sex = fields.Bool()
    age = fields.Bool(default=True)
    cpf = fields.Bool(required=True, default="000")

# class People:

#     def __init__(self, name, sex, age=True, cpf=1):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.cpf = cpf

def create_code_python(string):
    f = open("result.py", "w")
    f.write(string)
    f.close()

code_generator = CodeGenerator()
print(code_generator.generate_method("create", "name", "age"))
print(code_generator.generate_method("create", cpf="12", sex=True))
print(code_generator.generate_method("create", "name", "age", cpf="12", sex=True))
print(code_generator.get_model_by_schema(People))
# create_code_python(code_generator.generate_method("create"))
