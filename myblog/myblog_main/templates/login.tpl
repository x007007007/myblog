{% extends '_base.tpl' %}
{% block body %}
    {% from "_formhelpers.tpl" import render_field %}
    <form method=post action="#">
      <dl>
        {{ render_field(form.username) }}
        {{ render_field(form.password) }}
        {{ render_field(form.rememberme) }}
      </dl>
      <p><input type=submit value="save">
    </form>
{% endblock %}