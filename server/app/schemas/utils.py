from marshmallow import Schema, fields


class RegisterUserPayload(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class LoginUserPayload(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

