from flask import Flask, render_template, request
from json import load, dumps
from csv import DictReader

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open("items.json", "r", encoding="utf-8") as file:
        items = load(file).get("items", [])
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    type = request.args.get("source", "")
    id = request.args.get("id")
    if type == "json":
        with open("products.json", "r", encoding="utf-8") as file:
            items = load(file)
    elif type == "csv":
        with open("products.csv", "r", encoding="utf-8") as file:
            reader = DictReader(file)
            items = [a for a in reader]
    else:
        return render_template('product_display.html', err="Wrong source")
    if id is None:
        return render_template('product_display.html', items=items)
    item = next((sub for sub in items if str(sub['id']) == str(id)), None)
    if item is not None:
        return render_template('product_display.html', items=[item])
    return render_template('product_display.html', err="Product not found")



if __name__ == '__main__':
    app.run(debug=True, port=5000)
