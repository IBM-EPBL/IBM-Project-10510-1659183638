Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import flask
>>> flask.__version__
'2.2.2'
>>> from flask import Flask
... 
... app = Flask(__name__)
... 
... @app.route("/")
... def hello_world():
...     return "<p>Hello, World!</p>"
SyntaxError: multiple statements found while compiling a single statement
>>> from flask import Flask
>>> app = Flask(__name__)
>>> @app.route("/")
... def hello_world():
...     return "<p>Hello, World!</p>"
