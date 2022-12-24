class StringCode:

    def apply_indentation(self, string: str):
        return string.replace("#", "    ")

    def apply_space(self, string: str, apply_indentation: bool = True):
        string_with_spaces = string.replace("-", " ")
        if apply_indentation:
            return self.apply_indentation(string_with_spaces)
        return string_with_spaces

    def apply_enter(self, string: str, apply_indentation: bool = True):
        string_with_enter = string.replace("|", "\n")
        if apply_indentation:
            return self.apply_indentation(string_with_enter)
        return string_with_enter

    def apply_attributes(self, string: str, apply_indentation: bool = True):
        string_with_attributes = string.replace("$", "##self.")
        if apply_indentation:
            return self.apply_indentation(string_with_attributes)
        return string_with_attributes

    def create_code_string_in_line(self, code_strings: list):
        return "".join([line for line in code_strings])

    def parse_class_name_to_string_declaration(self, class_name: str):
        return f"class-{class_name}:||"

    def create_class_method_init_to_string_declaration(self, attributes):

        def add_params(string_method: str, params: list):
            string_params = ", ".join([param for param in params])
            return string_method.replace("):|", f"{string_params}):|")

        def add_attributes(string_method: str, attributes):
            def mount_string_code_receive_variable(name, value):
                return f"{name} = {value}|"

            string_attributes = "$".join([
                mount_string_code_receive_variable(attribute, attribute) for attribute in attributes
            ])
            return string_method + f"${string_attributes}"

        string_method_init = "#def-__init__(self):|"
        if attributes:
            string_method_init = string_method_init.replace("):", ", ):") # TO DO: TEMP
            string_method_init = add_params(string_method_init, attributes)
            string_method_init = add_attributes(string_method_init, attributes)

        return string_method_init
