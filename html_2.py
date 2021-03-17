from flask import Flask, url_for, request, render_template
import os
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index/<username>')
def index(username):
    return render_template('index.html', title=username)


if __name__ == '__main__':
    app.run(port=8080, host='192.168.1.59')