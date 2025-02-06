from flask import Flask, render_template, request
import os

app = Flask(__name__)


poll_data = {
    'question': 'What is yor favorite programming lnaguage?',
    'fields': ['Python', 'Ruby', 'Java', 'Other'],}

dish_data = {
    'question': 'What is your favorite dish? ',
    'fields': ['Pizza', 'Pasta', 'Lasagna', 'Wine with parmesan cheese']}

@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)

@app.route('/dish')
def dish():
    return render_template("index.html", data_dish=dish_data)

@app.route('/poll')
def poll():
    vote = request.args.get('field')
    with open('data.txt', 'a') as file:
        file.write(vote + '\n')
    return vote


if __name__ == '__main__':
    app.run(debug=True)
