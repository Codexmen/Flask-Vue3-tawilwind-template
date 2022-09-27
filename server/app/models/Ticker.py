from server.app import db


class Ticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10))
    stock = db.Column(db.String(64))


    def __repr__(self):
        return '<Ticker {}>'.format(self.ticker + ' ' + self.stock)
