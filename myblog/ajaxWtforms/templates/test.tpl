<html>
<head>
    <script src="{{ url_for('ajax_wtforms.static', filename='jquery-1.11.3.min.js') }}" ></script>
    <script>
        $(function(){
            $("#fields>dd").each(function(offset, dom){
                var jdom=$(dom),
                    widget=jdom.find("div.widget>*:first-child"),
                    id=widget.attr("id");
                jdom.find("button").on("click", function(){
                    var data={};
                    if(widget.prop("name")){
                        data[widget.prop("name")]=widget.prop("value");
                        $.post("#",
                            data,
                            function(res){
                                var res=JSON.parse(res);
                                if(res.error){
                                    console.log(jdom);
                                    jdom.find("div.msg").text(res.msg[id]);
                                }else{
                                    jdom.find("div.msg").text("");
                                }
                            }
                        ),'json';
                    }

                });
            });
        });
    </script>
</head>
<body>
    <from method="POST">
        <dl id="fields">
        {% for name in fields %}
            <dt>{{ name }}<dt><dd><div class="widget">{{ fields[name] }}</div><button>测试</button><div class="msg"></div></dd>
        {% endfor %}
        </dl>
    </from>
</body>
</html>