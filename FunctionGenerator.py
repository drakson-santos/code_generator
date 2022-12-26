from StringCode import StringCode
from CodeBlockGenerator import CodeBlockGenerator

class FunctionGenerator():

    def generate_function(self, method_name: str, *args, **kargs):
        string_code = StringCode()
        declaration_method = string_code.create_function_in_string_declaration(
            method_name,
            required_params=args,
            options_params=kargs
        )
        declaration_method = string_code.add_code_block_in_method(declaration_method, CodeBlockGenerator.get_pass_code())
        return string_code.parse_string_code_declaration_in_line_to_python_format(declaration_method)

