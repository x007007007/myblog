{% extends '_base.tpl' %}
{% block body %}
    {% from "_formhelpers.tpl" import render_field %}
    <form method=post action="/post">
      <dl>
        {{ render_field(form.title) }}
        {{ render_field(form.text) }}
      </dl>
      <p><input type=submit value="save">
    </form>
{% endblock %}
