import json
from server.app import db
from flask import Blueprint, jsonify, request
from flask_login import current_user
from server.app.models import UserStockMove
from server.app.api.schemas import UserTransactionSchema
bp = Blueprint('tokens', __name__, url_prefix='/api/tokens')
list = []

@bp.route('/', methods=['POST'])
def add_token():
    data = json.loads(request.data)
    user_coins_move = UserStockMove(**data, user_id=current_user.get_id())
    db.session.add(user_coins_move)
    db.session.commit()
    return jsonify(data)


@bp.route('/', methods=['GET'])
def tokens():
    stocks = db.session.query(UserStockMove).filter_by(user_id=current_user.get_id()).all()
    user_transactions = UserTransactionSchema()
    return jsonify(user_transactions.dump(stocks, many=True))

