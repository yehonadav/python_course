from jinja2 import Template


message = input('enter message:')
template = Template("{{ message }}")
print(template.render(message=message))
