from flask import Flask

from todo.config import configs
from todo.extensions import db
from todo.blueprints.todo import todos


def create_app(env="dev"):
    app = Flask(__name__)
    app.config.from_object(configs[env])

    db.init_app(app)

    app.register_blueprint(todos, url_prefix="/todos")

    return app
