from marshmallow import Schema
from SchemaInformation import SchemaInformation
from FunctionGenerator import FunctionGenerator
from ModelGenerator import ModelGenerator

class CodeGenerator(
    FunctionGenerator,
    ModelGenerator
):

    def get_model_by_schema(self, schema: Schema):
        schema_information = SchemaInformation(schema)
        model_name = schema_information.get_name_schema()

        if "Schema" in model_name:
            model_name = model_name.replace("Schema", "Model")
        else:
            model_name += "Model"

        model_attributes = schema_information.get_fields_schema()
        return self.generate_model(model_name, model_attributes)
