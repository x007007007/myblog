{% extends '_base.tpl' %}
{% block body %}
<body>
<ul>
{% for artical in articals %}
<li><h3>{{ artical.title }}</h3><p>{{ artical.text }}</p></li>
{% endfor %}
</ul>
<body>
{% endblock %}