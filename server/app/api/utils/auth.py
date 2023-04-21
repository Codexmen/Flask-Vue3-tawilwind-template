import json
from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required, login_manager
from app.models.User import User
from app import db
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/me', methods=['GET', 'POST'])
def user_info():
    if current_user.is_authenticated:
        return jsonify(username=current_user.email)
    else:
        return jsonify(username='')


@auth_bp.route('/register', methods=['POST'])
def register():
    data = json.loads(request.data)
    user = User(email=data.email)
    user.set_password(data.password)
    db.session.add(user)
    db.session.commit()

    return jsonify({}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        return jsonify(
            isAuthenticated=False
        )
    login_user(user)
    return jsonify(
        username=user.email,
        isAuthenticated=True
    )


@login_required
@auth_bp.route('/logout', methods=['POST'])
def loguot():
    logout_user()
    return jsonify()