from pprint import pprint
import re
import textwrap as tw
import openai
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import os
app = Flask(__name__)
openai.api_key = os.environ.get('API_KEY')

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

# OpenAI function


def GenerateBudget(userName, state, income, expenses):
    # prompt that will be sent to AI
    prompt = f"Generate a detailed 50/30/20 budget for {userName} and divide the after-tax income into three categories: 50% for needs, 30% for wants and 20% for savings and debt repayment. Take the given pre-tax salary of {income} and apply {state}'s state tax. Take in consideration the fixed expenses' value of {expenses}. Make it seem personalized by repeating the person's name."
    completion = openai.Completion.create(
        engine="text-davinci-002", max_tokens=256, prompt=prompt)
    results = completion.choices[0].text.strip()

    return prompt, results


# AJAX FUNCTIONS
@app.route('/saveEntry', methods=['GET', 'POST'])
def generateBudget():

    global receivedUserInput
    json_data = request.get_json()
    receivedUserInput = json_data

    for key, value in receivedUserInput.items():
        userName = receivedUserInput['name']
        state = receivedUserInput['state']
        income = receivedUserInput['income']
        expenses = receivedUserInput['expenses']

        # print(key, value)

    # calling on openai
    GenerateBudget(userName, state, income, expenses)
    prompt, result = GenerateBudget(userName, state, income, expenses)
    # print("input: " + receivedUserInput)
    print("prompt: " + prompt)
    print(result)

    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
