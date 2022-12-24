from marshmallow import Schema
from SchemaInformation import SchemaInformation
from StringCode import StringCode

class CodeGenerator:

    def parse_string_code_declaration_in_line_to_python_format(self, string_code_declaration_in_line):
        string_code = StringCode()
        string_code_formatting = string_code_declaration_in_line
        string_code_formatting = string_code.apply_space(string_code_formatting)
        string_code_formatting = string_code.apply_attributes(string_code_formatting)
        string_code_formatting = string_code.apply_enter(string_code_formatting)
        return string_code_formatting

    def create_model_string(self, model_name: str, model_attributes: dict, python_format: bool = True):
        string_code = StringCode()
        declaration_class = string_code.parse_class_name_to_string_declaration(model_name)
        declaration_class_method_init = string_code.create_class_method_init_to_string_declaration(model_attributes.keys())

        declaration_model_string_in_line = string_code.create_code_string_in_line([
            declaration_class,
            declaration_class_method_init
        ])

        if python_format:
            return self.parse_string_code_declaration_in_line_to_python_format(declaration_model_string_in_line)
        return declaration_model_string_in_line

    def get_model_by_schema(self, schema: Schema):
        schema_information = SchemaInformation(schema)
        model_name = schema_information.get_name_schema()
        model_attributes = schema_information.get_fields_schema()

        return self.create_model_string(model_name, model_attributes)