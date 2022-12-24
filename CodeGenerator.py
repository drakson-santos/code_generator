from marshmallow import Schema
from SchemaInformation import SchemaInformation
from StringCode import StringCode

class MethodGenerator():

    def generate_method(self, method_name: str, *args, **kargs,):
        string_code = StringCode()
        declaration_method = string_code.get_method_to_string_declaration(method_name)
        declaration_method = string_code.add_params(declaration_method, args)
        declaration_method = string_code.add_params(declaration_method, kargs)

        return declaration_method

class CodeGenerator(MethodGenerator):

    def create_model(self, model_name: str, model_attributes: dict, python_format: bool = True):
        string_code = StringCode()
        declaration_class = string_code.parse_class_name_to_string_declaration(model_name)
        declaration_class_method_init = string_code.create_class_method_init_in_string_declaration(model_attributes)

        declaration_model_string_in_line = string_code.create_code_string_in_line([
            declaration_class,
            declaration_class_method_init
        ])

        model = declaration_model_string_in_line
        if python_format:
            model = string_code.parse_string_code_declaration_in_line_to_python_format(declaration_model_string_in_line)
        return model

    def get_model_by_schema(self, schema: Schema):
        schema_information = SchemaInformation(schema)
        model_name = schema_information.get_name_schema()
        model_attributes = schema_information.get_fields_schema()
        return self.create_model(model_name, model_attributes)
