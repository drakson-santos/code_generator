from marshmallow import Schema, fields
from SchemaInformation import SchemaInformation
from CodeGenerator import CodeGenerator

class People(Schema):
    name = fields.Str()
    age = fields.Bool(default=True)
    sex = fields.Bool(required=False)
    cpf = fields.Bool(required=True, default="000")

def create_code_python(string):
    f = open("result.py", "w")
    f.write(string)
    f.close()

code_generator = CodeGenerator()
create_code_python(code_generator.get_model_by_schema(People))
