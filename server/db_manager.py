from flask_migrate import Migrate
from app import create_app, db
from app.models.User import User
app = create_app('development')
migrate = Migrate(app, db)
print(db)
user = User(first_name='Yura', email='admin@admin.com')
user.reset_password('qwe123')

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add(user)
    db.session.commit()