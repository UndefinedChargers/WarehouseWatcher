# FILE : main.py
# PROGRAMMER : William Anderson
# FIRST VERSION : 2025-03-23
# DESCRIPTION : Communicates the current threshold data to the grafana api to update panel thresholds.

# Basic scaffolding and example HTTP method taken from https://www.geeksforgeeks.org/flask-http-method/?ref=next_article

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/square', methods=['GET'])
def squarenumber():
    num = request.args.get('num')

    if num is None:  # No number entered, show input form
        return render_template('squarenum.html')
    elif num.strip() == '':  # Empty input
        return "<h1>Invalid number. Please enter a number.</h1>"
    try:
        square = int(num) ** 2
        return render_template('answer.html', squareofnum=square, num=num)
    except ValueError:
        return "<h1>Invalid input. Please enter a valid number.</h1>"

if __name__ == '__main__':
    app.run(debug=True)