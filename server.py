from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# ROUTES


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/budgetPage', methods=['GET', 'POST'])
def budget():

    return render_template('budget.html')


@app.route('/tipsPage', methods=['GET', 'POST'])
def tips():

    return render_template('tips.html')


if __name__ == '__main__':
    app.run(debug=True)
