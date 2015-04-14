<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf8" />
    <title>myblog</title>
  </head>
<body>
<ul>
{% for artical in articals %}
<li>{{ artical }}</li>
{% endfor %}
</ul>
<body>
</html>