from flask import Flask
from auth import auth_bp
from main import main_bp
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your_secret_key'

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)