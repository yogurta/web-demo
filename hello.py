from flask import Flask, url_for, render_template
#from jinja2 import Markup
app = Flask(__name__)

@app.template_filter('cap')# tohle je šablona
def capitalize(word):
    return word[0].upper() + word[1:]

@app.route('/')# dekorátor z funkce udělá routu (pohledovou funkci)
# když někdo přidá požadavek
def index(): # pohledová funkce neboli view - obhospodařovává konktrétní požadavky
    return 'Ahoj Pyladies!'

@app.route('/url/')
def url():
    return url_for('hello',name = 'Kata', count=123,_external=True) # když to napisu na strance, tak me to nasmeruje


@app.route('/hello/')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:count>/')
def hello(name='world', count=1):
    #if name is None:
        #return "Hello"
    #return 'Hello, {}!'.format(name) * count
    return render_template('hello.html', name=name) #name=name.capitalize())

#http://127.0.0.1:5000/hello/katka/5/

#V příkazové řádce!!!
# export FLASK_APP=hello.py  # nastavuji, že flaskova aplikace je v tomto souboru
#export FLASK_DEBUG=1
#flask run

#http://127.0.0.1:5000/url/
# a objeví se mi http://127.0.0.1:5000/hello/Kata/123/

#flask run
