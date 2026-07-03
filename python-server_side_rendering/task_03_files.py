#!/usr/bin/env python3

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/products')
def products():
    source = request.args.get('source')
    get_id = request.args.get('id')
    error = None
    products_data = []

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        with open('products.json', 'r') as file:
            products_data = json.load(file)

    if source == 'csv':
        with open('products.csv', 'r') as file:
            products_data = list(csv.DictReader(file))

    if get_id is not None:
        filtered_products = []
        for product in products_data:
            if str(product.get('id')) == get_id:
                filtered_products.append(product)

        if not filtered_products:

            return render_template('product_display.html',
                                   error="Product not found")

        products_data = filtered_products

    return render_template('product_display.html',
                           products=products_data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
