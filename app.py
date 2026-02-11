from flask import Flask, render_template, request
from questions import QUESTIONS
from inference import get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html', questions=QUESTIONS)

@app.route('/result', methods=['POST'])
def result():
    answers = {}
    for key, value in request.form.items():
        if key.startswith('q'):
            answers[key] = int(value)
    recommendations = get_recommendations(answers)
    return render_template('result.html', recommendations=recommendations, questions=QUESTIONS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')