from app import app as application
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html', current_page='About')

@app.route('/resume')
def resume():
    return render_template('resume.html', current_page='Resume')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', current_page='Portfolio')

@app.route('/blog')
def blog():
    return render_template('blog.html', current_page='Blog')

@app.route('/contact')
def contact():
    return render_template('contact.html', current_page='Contact')

if __name__ == '__main__':
    app.run(debug=True)