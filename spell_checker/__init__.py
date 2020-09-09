from flask import Flask
from flask_redis import FlaskRedis


# Instantiate redis client
redis_client = FlaskRedis(decode_responses=True)


def create_app():
    """Flask application factory."""
    # Create the application instance
    app = Flask(__name__)

    # Load extra config variables
    app.config.from_object('config.Config')

    # Associate redis
    redis_client.init_app(app)

    # Register blueprint(s)
    from . import spellcheck
    app.register_blueprint(spellcheck.bp)

    # Return the application
    return app
