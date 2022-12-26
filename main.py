from marshmallow import Schema, fields
from SchemaInformation import SchemaInformation
from CodeGenerator import CodeGenerator

def create_code_python(string):
    f = open("result.py", "w")
    f.write(string)
    f.close()

class PeopleSchema(Schema):
    name = fields.Str()
    sex = fields.Bool()
    age = fields.Bool(default=True)
    cpf = fields.Bool(required=True, default="000")

code_generator = CodeGenerator()
# create_code_python(code_generator.generate_method("create", "name", "age"))
# create_code_python(code_generator.generate_method("create", cpf="12", sex=True))
# create_code_python(code_generator.generate_function("create", "name", "age", cpf="12", sex=True))
create_code_python(code_generator.get_model_by_schema(PeopleSchema))
# create_code_python(code_generator.generate_method("create"))
