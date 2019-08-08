import yaml


document = """
  name: Martin
  job: Developer
  skill: Ellite
  employed: True
  education:
"""


obj = yaml.dump(yaml.load(document, Loader=yaml.Loader))
print(type(obj))
with open('my.yaml', 'w') as f:
    f.write(obj)

with open('my.yaml', 'rb') as f:
    document = yaml.load(stream=f.read(), Loader=yaml.Loader)
print(document)

print(yaml.dump(document))
