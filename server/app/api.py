from flask import Blueprint, jsonify
bp = Blueprint('ping', __name__, url_prefix='/api/ping')

@bp.route('/', methods=('GET', 'POST'))
def ping():
    return jsonify({"data": 'pong'})