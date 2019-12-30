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

# @app.route('/test/')
# def test():
    # return render_template('test.html')

@app.route('/epicycler/')
@app.route('/projects/drawing-epicycler/')
def epicycler():
    # return render_template('epicycler\\index.html')
    # main_folder = os.path.dirname(os.path.abspath(__file__))
    # templates_folder = os.path.join(main_folder, 'templates')
    # return render_template('epicycler/index.html')
    # return render_template('epicycler/index.html')
    return render_template('epicycler.html')

if __name__ == "__main__":
    app.run()
