from flask import Flask
from config import Config
from extension import db
from routes import register_book

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

register_book(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    
    app.run(debug=True)