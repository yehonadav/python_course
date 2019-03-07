from jinja2 import Template


template = Template("{% for n in range(1,10) %}{{n}} " "{% endfor %}")
print(template.render())
