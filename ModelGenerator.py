from StringCode import StringCode

class ModelGenerator():

    def generate_model(self,  model_name: str, model_attributes: dict, python_format: bool = True):
        string_code = StringCode()
        declaration_class = string_code.parse_class_name_to_string_declaration(model_name)
        declaration_class_method_init = string_code.create_class_method_in_string_declaration(model_attributes)

        declaration_model_string_in_line = string_code.create_code_string_in_line([
            declaration_class,
            declaration_class_method_init
        ])

        model = declaration_model_string_in_line
        if python_format:
            model = string_code.parse_string_code_declaration_in_line_to_python_format(declaration_model_string_in_line)
        return model