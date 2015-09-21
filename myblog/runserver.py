import sys
import os
from flask import Flask
from flask import url_for
from flask_migrate import Migrate, MigrateCommand
sys.path.append(os.path.dirname(__file__))
from myblog_main import models as myblog_models
from myblog_main import view as myblog_views
from myblog_main import login_manager
from flask_script import Manager
from ajaxWtforms import InitAjaxWtforms


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
InitAjaxWtforms(app)


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        try:
            url = url_for(rule.endpoint, **options)
            line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        except:
            line = rule.endpoint
        output.append(line)

    for line in sorted(output):
        print line

if __name__ == "__main__":
    # To allow aptana to receive errors, set use_debugger=False
    myblog_models.db.app = app
    myblog_models.db.init_app(app)
    myblog_models.db.create_all()
    migrate = Migrate(app, myblog_models.db)
    login_manager.init_app(app)
    manager.add_command('db', MigrateCommand)

    app.register_blueprint(myblog_views.pages)
    app.secret_key = 'skeislfjdislakdfncmv,xz.hqieo1m4lkaf90lnmzcvlkadf91//a;?KJ./q'

    manager.run()