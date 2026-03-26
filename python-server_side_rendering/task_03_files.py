from flask import Flask, render_template, request
from json import load

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
    if type == "json":
        pass
    elif type == "csv":
        pass
    else:
        return "Wrong source"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
