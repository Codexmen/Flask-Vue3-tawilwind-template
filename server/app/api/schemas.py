from marshmallow import Schema, fields


class UserTransactionSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    ticker_id = fields.Integer()
    ticker = fields.String()
    buy_price = fields.Number()
    amount = fields.Number()
