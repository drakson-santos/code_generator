from marshmallow import Schema
from marshmallow.fields import Field

class SchemaInformation:

    def __init__(self, schema: Schema):
        self.schema: Schema = schema

    def get_name_schema(self):
        return self.schema.__name__

    def get_fields_schema(self):
        return self.schema._declared_fields

    def get_field_default_value(self, field: Field):
        return field.default

    def field_is_required(self, field: Field):
        return field.required