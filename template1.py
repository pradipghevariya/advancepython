# from jinja2 import Template


# name = input("Enter name: ")
# tn = Template("hello {{ name }}")
# msg = tn.render(name=name)
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getAge(self):
#         return self.age
#
#     def getName(self):
#         return self.name
#
#
# person = Person('john', 22)
# tn = Template("Name is {{per.getName()}} and age is {{per.getAge()}}")
# msg = tn.render(per=person)
# print(msg)

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')


@app.route('/greet')
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)


if __name__ == '__main__':
    app.run()
