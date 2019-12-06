from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/about-me/')
def about_me():
    return render_template("about-me.html")

# @app.route('/contact/')
# def contact():
#     return render_template("contact.html")

@app.route('/test/')
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run()
