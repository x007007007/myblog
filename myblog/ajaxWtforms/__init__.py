from .views import ajax_wtforms_bp
from .forms import AjaxForm
from .validators import ValidatorSchema

def InitAjaxWtforms(app, url_prefix="/ajax_wtforms"):
    app.register_blueprint(ajax_wtforms_bp, url_prefix=url_prefix)