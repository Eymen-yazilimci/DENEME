from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

ideas = []

@app.route('/')
def index():
    return render_template('index.html', ideas=ideas)

@app.route('/submit', methods=['POST'])
def submit():
    title = request.form['title']
    description = request.form['description']
    if title and description:
        ideas.append({'title': title, 'description': description})
    return render_template('index.html', ideas=ideas)

@app.route('/idea/<int:index>')
def idea(index):
    idea = ideas[index]
    return render_template('idea.html', idea=idea)

if __name__ == '__main__':
    app.run(debug=True)
