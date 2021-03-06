from flask import Flask, render_template, send_from_directory, url_for, redirect
import os


app = Flask(__name__)
# , static_url_path='/static', static_folder='/static'


@app.route('/')
def home():
    return render_template('home.html')

#
# @app.route('/resume')
# def resume():
#     return render_template('resume.html')
#
#
# @app.route('/portfolio')
# def portfolio():
#     return render_template('portfolio.html')
#
#
# @app.route('/contact')
# def contact():
#     return render_template('contactme.html')


@app.route('/static/<path:path>')
def statics(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run()
