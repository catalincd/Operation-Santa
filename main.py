import os
import sys
from flask import Flask, render_template, send_file

sys.path.append('./src')
import PageGenerator


app = Flask(__name__)

@app.route("/")
def indexRoute():
    return PageGenerator.GetPageString('index.html', {'clatiteString':'bonchisString'})


@app.route('/res/<path:subpath>')
def show_subpath(subpath):
    path = './templates/res/' + subpath
    if os.path.exists(path):
        return send_file(path)
    else:
        return PageGenerator.GetPageString('404.html')
    

