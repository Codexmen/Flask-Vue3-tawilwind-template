import json
from sqlalchemy.exc import IntegrityError

from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required, login_manager
from marshmallow import ValidationError

from app.models.User import User
from app import db
from app.schemas.utils import RegisterUserPayload
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/me', methods=['GET', 'POST'])
def user_info():
    if current_user.is_authenticated:
        return jsonify(username=current_user.email)
    else:
        return jsonify(username='')


@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        user_payload = RegisterUserPayload().load(request.json)
        user = User(email=user_payload['email'])
        user.reset_password(user_payload['password'])
        db.session.add(user)
        db.session.commit()
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    except IntegrityError as e:
        return jsonify({'error': "user exist", "code": 501}), 400

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
        email=user.email,
        isAuthenticated=True
    )


@login_required
@auth_bp.route('/logout', methods=['POST'])
def loguot():
    logout_user()
    return jsonify()