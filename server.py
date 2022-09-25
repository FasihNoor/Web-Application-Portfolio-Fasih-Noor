from cgitb import html
from urllib import request
from flask import Flask, render_template, request
app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    # Flask looks for these templates in the templates file. So index.html must be in a file called templates. We must create this file.
    return render_template('./index.html')

# Accessing all the pages


@app.route('/<string:page>')
def html_page(page):
    # Flask looks for these templates in the templates file. So index.html must be in a file called templates. We must create this file.
    return render_template(page)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return render_template('thankyou.html')
    else:
        return "something is wrong"


# @app.route('/components.html')
# def components():
#     return render_template('./components.html')
