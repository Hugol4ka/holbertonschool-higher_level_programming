#!/usr/bin/env python3

import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        items_data = json.load(file)
        rendered_html = render_template('items.html', items=items_data.get('items', []))
    return rendered_html

if __name__ == '__main__':
    app.run(debug=True, port=5000)