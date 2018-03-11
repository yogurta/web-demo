from flask import Flask, url_for, render_template
import getpass
import requests
import configparser
import click

app = Flask(__name__)

config = configparser.ConfigParser()
with open('auth.cfg') as f:
    config.read_file(f)
token = config['github']['token']
username = 'yogurta' # username
password = token
session = requests.Session()
session.get('https://api.github.com/users', auth = (username,password))
session.headers = {'Authorization':'token '+ token, 'User-Agent':'Python'}

@app.route('/')# dekorátor z funkce udělá routu (pohledovou funkci)
def index(): # pohledová funkce neboli view - obhospodařovává konktrétní požadavky
    return 'Ahoj Pyladies!'

@app.route('/web-demo/')
def webdemo():
    response = session.post(
        'https://api.github.com/repos/yogurta/web-demo/issues/1/reactions',
        headers={'Accept': 'application/vnd.github.squirrel-girl-preview+jso'},
        json={'content': 'laugh'}
    )
    response.raise_for_status()
    return 'Laugh added to https://api.github.com/repos/yogurta/web-demo/issues/1/reactions'


@app.route('/test-repo/')
def testrepo():
    response = session.post(
        'https://api.github.com/repos/encukou/test-repo/issues/1/reactions',
        headers={'Accept': 'application/vnd.github.squirrel-girl-preview+jso'},
        json={'content': 'laugh'}
    )
    response.raise_for_status()
    return 'Laugh added to https://api.github.com/repos/encukou/test-repo/issues/1/reactions'
