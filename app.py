
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html', current_page='About')

@app.route('/resume')
def resume():
    return render_template('resume.html', current_page='Resume')

if __name__ == '__main__':
    app.run(debug=True)