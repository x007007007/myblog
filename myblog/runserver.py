import sys
import os
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
sys.path.append(os.path.dirname(__file__))
from myblog_main import models as myblog_models
from myblog_main import view as myblog_views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/myblog.db"
app.debug = True


if __name__ == "__main__":
    # To allow aptana to receive errors, set use_debugger=False
    myblog_models.db.app = app
    myblog_models.db.init_app(app)
    myblog_models.db.create_all()
    migrate = Migrate(app, myblog_models.db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    app.register_blueprint(myblog_views.pages)

    app.run(host='0.0.0.0', port=5001)