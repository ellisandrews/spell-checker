from flask import Flask


def create_app():
    """Application factory."""
    # Create and configure the app
    app = Flask(__name__)

    from . import spellcheck
    app.register_blueprint(spellcheck.bp)

    return app
