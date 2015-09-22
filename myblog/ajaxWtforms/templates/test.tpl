<html>
<head>
    <script src="{{ url_for('ajax_wtforms.static', filename='jquery-1.11.3.min.js') }}" ></script>
</head>
<body>
    <dl>
    {% for name in fields %}
        <dt>{{ name }}<dt><dd><div>{{ fields[name] }}</div><div class="msg"></div></dd>
    {% endfor %}
    </dl>
</body>
</html>