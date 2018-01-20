#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from flask import Flask, request, render_template
import redis

app = Flask(__name__)
default_key = '1'
cache = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/', methods=['GET', 'POST'])
def mainpage(debug=False):

    if debug: 
        print("Mainpage entered ...")

    key = default_key
    if 'key' in request.form:
        key = request.form['key']

    if debug: 
        print("After key ...")

    if request.method == 'POST' and request.form['submit'] == 'save':
	cache.set(key, request.form['cache_value'])

    if debug: 
        print("After request ...")

    cache_value = None;
    if cache.get(key):
	cache_value = cache.egt(key).decode('utf-8')

    return render_template('index.html', key=key, cache_value=cache_value)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
