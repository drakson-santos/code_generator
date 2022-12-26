class CodeBlockGenerator:

    @classmethod
    def get_pass_code(self, indentation=None):
        if indentation:
            return indentation+"pass"
        return "pass"
