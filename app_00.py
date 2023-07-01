from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/second/')
def second():
    return render_template('second.html')


@app.route('/three/')
def three():
    return render_template('three.html')

@app.route('/four')
def four():
    return render_template('four.html')