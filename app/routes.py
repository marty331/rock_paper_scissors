from app import app
from flask import render_template, url_for, request, jsonify

import random

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/_random_num')
def random_num():
    print("random num")
    random_pic = random.randint(0,2)
    if random_pic == 0:
        picture = 'paper.jpeg'
    elif random_pic == 1:
        picture = 'rock.jpg'
    else:
        picture = 'scissors.jpg'
    print(f"picture {picture}")
    return jsonify(result="images/" + picture)