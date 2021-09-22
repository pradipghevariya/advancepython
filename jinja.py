from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "andre", "age": 22},
    {"name": "john", "age": 20}
]

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)
template = env.get_template('show.txt')

output = template.render(persons=persons)
print(output)
