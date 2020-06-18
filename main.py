from flask import Flask
from flask_wtf import CSRFProtect
from flask_seeder import FlaskSeeder
import os
import sys
from app.routes import routes 
from app.database import db
from app.setup import recreateTables
from app.setup import seedData

if os.path.exists('config.env'):
    for line in open('config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")

base_dir = os.path.abspath(os.path.dirname(__file__))
app_dir = os.path.join(base_dir, 'app')

template_dir = os.path.join(app_dir, 'views')
seeds_dir    = os.path.join(app_dir, 'seeds')

application = Flask(__name__, template_folder=template_dir)
application.secret_key = os.environ.get('SECRET_KEY')

# Initiate database connection
connection_string = os.environ.get('DB_CONNECTION') + '://' + os.environ.get('DB_USERNAME') + '@' + os.environ.get('DB_PASSWORD') + '/' + os.environ.get('DATABASE_NAME')
application.config['SQLALCHEMY_DATABASE_URI'] = connection_string
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
application.config['SQLALCHEMY_ECHO'] = bool(os.environ.get('SQL_LOG'))
 
# register routes from urls
application.register_blueprint(routes)

csrf = CSRFProtect()
seeder = FlaskSeeder()

db.init_app(application)
seeder.init_app(application, db)

if __name__ == '__main__':

    if os.environ.get('FLASK_ENV') == 'development':
        application.debug = True
    if os.environ.get('RECREATE_TABLES') == 'True':
        recreateTables(application, db)
    if os.environ.get('RECREATE_SEEDS') == 'True':
        seedData(application, db)
    
    application.run()
