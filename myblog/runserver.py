import sys
import os
from flask import Flask
from flask import url_for
from flask_migrate import Migrate, MigrateCommand
sys.path.append(os.path.dirname(__file__))
from myblog_main import models as myblog_models
from myblog_main import view as myblog_views
from flask_login import LoginManager
from flask_script import Manager


loginmanager = LoginManager()
from threading import Thread
import thread
import gc
import sys
import time
#gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/myblog.db"
app.debug = True

manager = Manager(app)

@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        print rule.endpoint, options
        url = url_for(rule.endpoint, **options)
        print url
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line

if __name__ == "__main__":
    # To allow aptana to receive errors, set use_debugger=False
    myblog_models.db.app = app
    myblog_models.db.init_app(app)
    myblog_models.db.create_all()
    migrate = Migrate(app, myblog_models.db)


    manager.add_command('db', MigrateCommand)

    app.register_blueprint(myblog_views.pages)
    app.secret_key = 'skeislfjdislakdfncmv,xz.hqieo1m4lkaf90lnmzcvlkadf91//a;?KJ./q'

    manager.run()