from StringCodeActionEnum import StringCodeActionEnum
from SchemaInformation import SchemaInformation
from marshmallow.fields import Field
class StringCode:

    def apply_indentation(self, string: str):
        return string.replace(StringCodeActionEnum.INDENTATION.value, "    ")

    def apply_space(self, string: str, apply_indentation: bool = True):
        string_with_spaces = string.replace(StringCodeActionEnum.SPACE.value, " ")
        if apply_indentation:
            return self.apply_indentation(string_with_spaces)
        return string_with_spaces

    def apply_enter(self, string: str, apply_indentation: bool = True):
        string_with_enter = string.replace(StringCodeActionEnum.ENTER.value, "\n")
        if apply_indentation:
            return self.apply_indentation(string_with_enter)
        return string_with_enter

    def apply_attributes(self, string: str, apply_indentation: bool = True):
        string_with_attributes = string.replace(StringCodeActionEnum.CLASS_ATTRIBUTE.value, "##self.")
        if apply_indentation:
            return self.apply_indentation(string_with_attributes)
        return string_with_attributes

    def add_attributes(self, string_method: str, attributes):
        def mount_string_code_receive_variable(name, value):
            return f"{name} = {value}{StringCodeActionEnum.ENTER.value}"

        string_attributes = StringCodeActionEnum.CLASS_ATTRIBUTE.value.join([
            mount_string_code_receive_variable(attribute, attribute) for attribute in attributes
        ])
        return string_method + f"{StringCodeActionEnum.CLASS_ATTRIBUTE.value}{string_attributes}"

    def add_params(self, string_method: str, params, is_schema = False):
        def get_string_param(param_name):
            param_string = f"{param_name}"

            if type(params) == dict:
                if is_schema:
                    param_default_value = SchemaInformation.get_field_default_value(params[param_name])
                else:
                    param_default_value = params[param_name]

                if param_default_value:
                    if type(param_default_value) == str:
                        param_default_value = f"'{param_default_value}'"
                    param_string += f"={param_default_value}"

            return param_string

        string_params = ", ".join([
            get_string_param(param_name)
            for param_name in params
        ])

        if string_params:
            string_params += ", "

        END_METHOD_DECLARATION = f"):{StringCodeActionEnum.ENTER.value}"
        return string_method.replace(END_METHOD_DECLARATION, f"{string_params}{END_METHOD_DECLARATION}")

    def get_method_to_string_declaration(self, method_name="__init__", indent_method=True):
        string_declaration = "def{}{}(self):{}".format(
            StringCodeActionEnum.SPACE.value,
            method_name,
            StringCodeActionEnum.ENTER.value,
        )
        if indent_method:
            string_declaration = f"{StringCodeActionEnum.INDENTATION.value}" + string_declaration
        if method_name != "__init__":
            string_declaration = string_declaration.replace("self):", "):")

        return string_declaration

    def create_code_string_in_line(self, code_strings: list):
        return "".join([line for line in code_strings])

    def parse_class_name_to_string_declaration(self, class_name: str):
        return "class{}{}:{}".format(
            StringCodeActionEnum.SPACE.value,
            class_name,
            StringCodeActionEnum.ENTER.value * 2
        )

    def parse_string_code_declaration_in_line_to_python_format(self, string_code_declaration_in_line):
        string_code_formatting = string_code_declaration_in_line
        string_code_formatting = self.apply_space(string_code_formatting)
        string_code_formatting = self.apply_attributes(string_code_formatting)
        string_code_formatting = self.apply_enter(string_code_formatting)
        return string_code_formatting + "\n"

    def create_class_method_init_in_string_declaration(self, attributes):
        string_method_init = self.get_method_to_string_declaration()
        if attributes:
            string_method_init = string_method_init.replace("):", ", ):")
            string_method_init = self.add_params(string_method_init, attributes, is_schema = True)
            string_method_init = self.add_attributes(string_method_init, attributes.keys())
        return string_method_init

    def create_method_string_declaration():
        pass