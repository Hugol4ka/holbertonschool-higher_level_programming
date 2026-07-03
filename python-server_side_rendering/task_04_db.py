#!/usr/bin/env python3

import csv
import json
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/products')
def products():
    source = request.args.get('source')
    get_id = request.args.get('id')
    error = None
    products_data = []

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        with open('products.json', 'r') as file:
            products_data = json.load(file)

    if source == 'csv':
        with open('products.csv', 'r') as file:
            products_data = list(csv.DictReader(file))

    elif source == 'sql':
        try:
            connect = sqlite3.connect('products.db')
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM Products")
            products_data = cursor.fetchall()
            products_data = [
                {"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in products_data
            ]
            
            connect.close()
        except sqlite3.Error:
            return render_template('product_display.html', error="Database error")

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
