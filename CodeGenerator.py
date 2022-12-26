from marshmallow import Schema
from SchemaInformation import SchemaInformation
from FunctionGenerator import FunctionGenerator
from ModelGenerator import ModelGenerator

from StringCode import StringCode
from CodeBlockGenerator import CodeBlockGenerator

class ControllerGenerator():

    def generate_controller(self, controller_name: str):
        def create_controller_method(method_name):
            declaration_method = string_code.create_function_in_string_declaration(
                method_name,
                is_class_method=True
            )
            declaration_method = string_code.add_code_block_in_method(declaration_method, CodeBlockGenerator.get_pass_code(indentation="#"))
            return declaration_method

        string_code = StringCode()
        declaration_class = string_code.parse_class_name_to_string_declaration(controller_name)





        declaration_controller_string_in_line = string_code.create_code_string_in_line([
            declaration_class,
            create_controller_method("get") + "|",
            "|" + create_controller_method("save") + "|",
            "|" + create_controller_method("update") + "|",
            "|" + create_controller_method("delete") + "|",
        ])

        return string_code.parse_string_code_declaration_in_line_to_python_format(declaration_controller_string_in_line)


class CodeGenerator(
    FunctionGenerator,
    ModelGenerator,
    ControllerGenerator
):

    def get_controller_by_model(self, model):
        class_name = model.split(":")
        controller_name = class_name[0].split(" ")[1]

        if "Model" in controller_name:
            controller_name = controller_name.replace("Model", "Controller")
        else:
            controller_name += "Controller"

        return self.generate_controller(controller_name)

    def get_model_by_schema(self, schema: Schema):
        schema_information = SchemaInformation(schema)
        model_name = schema_information.get_name_schema()

        if "Schema" in model_name:
            model_name = model_name.replace("Schema", "Model")
        else:
            model_name += "Model"

        model_attributes = schema_information.get_fields_schema()
        return self.generate_model(model_name, model_attributes)
