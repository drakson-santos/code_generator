from marshmallow import Schema, fields
from SchemaInformation import SchemaInformation
from CodeGenerator import CodeGenerator

def create_code_python(string):
    f = open("result.py", "a")
    f.write(string)
    f.close()

class People(Schema):
    name = fields.Str()
    sex = fields.Bool()
    age = fields.Bool(default=True)
    cpf = fields.Bool(required=True, default="000")

code_generator = CodeGenerator()
create_code_python(code_generator.generate_method("create"))
create_code_python(code_generator.generate_method("create", "name", "age", cpf="12", sex=True))
create_code_python(code_generator.get_model_by_schema(People))
