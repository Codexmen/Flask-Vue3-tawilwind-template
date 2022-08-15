import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app('develop')

if __name__ == '__main__':
    app.run(host='0.0.0.0')