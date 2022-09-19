import json
from flask import Blueprint, jsonify, request, flash
from flask_login import current_user, login_user
from ..models import User
bp = Blueprint('ping', __name__, url_prefix='/api/auth')


@bp.route('/me', methods=['GET', 'POST'])
def user_info():
    print(current_user)
    if current_user.is_authenticated:
        return jsonify(username=current_user.email)
    else:
        return jsonify(username='')

@bp.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    username = data['login']
    password = data['password']
    user = User.User.query.filter_by(email=username).first()
    if user is None or not user.check_password(password):
        return jsonify(
            isAuthenticated=False
        )
    login_user(user)
    return jsonify(
        username='email',
        isAuthenticated=True
    )