from flask import Flask
from config import Config
# import atexit

from app.extensions import scheduler


# from utils.jobs import clear_uploads_folder


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Flask extensions init
    # scheduler.add_job(func=clear_uploads_folder, trigger="cron", hour='23', id='clear_uploads_folder')
    # scheduler.start()
    #
    # Shut down the scheduler when exiting the app
    # atexit.register(lambda: scheduler.shutdown())

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
