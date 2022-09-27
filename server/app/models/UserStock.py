from server.app import db


class UserStockMove(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ticker_id = db.Column(db.Integer, db.ForeignKey('ticker.id'))
    # user_id = db.relationship("User", backref="user", lazy='dynamic')
    # ticker_id = db.relationship("Ticker", lazy='dynamic')
    ticker = db.Column(db.String(10))
    buy_price = db.Column(db.Numeric(12, 4))
    sell_price = db.Column(db.Numeric(12, 4))
    amount = db.Column(db.Integer)

    def __repr__(self):
        return '<User stocks {}>'.format(str(self.user_id) + ' ' + self.ticker + ' ' + str(self.buy_price) + ' ' + str(self.amount))
