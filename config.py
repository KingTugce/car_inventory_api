import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():

    """
                SET Config variables for the flask app.
                Using enviromentt variables where available others
                create the config variable if not done already.

    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or ' You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turn off update messages from sqlalchemy