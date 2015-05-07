{% extends '_base.tpl' %}
{% block body %}
<body>
<ul>
{% for artical in articals %}
<li><h3>{{ artical.title }}</h3><a href={{  }}>删除</a></li>
{% endfor %}
</ul>
<body>
{% endblock %}