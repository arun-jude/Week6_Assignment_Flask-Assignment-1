# Question 5

# Answer 5 - 

# The url_for() function is used to build a URL to the specific function dynamically. 
# The first argument is the name of the specified function, and then we can pass any number of 
# keywords as arguments corresponding to the variable part of the URL.
# This function is helpful because we can avoid hard-coding the URLs into the templates by dynamically building them.

# Python code to demonstrate the working of the url_for() function.

from flask import Flask
from flask import request, redirect, url_for


app = Flask(__name__)

@app.route("/")
def standard_msg():
    return "<h1> Company Name: ABC Corporation </h1><wbr> <h2> Location: India </h2> <wbr><h3> Contact Detail: 999-999-9999 </h3> "

@app.route("/ABC_Corp")
def ABC_Corp():
    return "<h1> Company Name: ABC Corp Selected</h1>"

@app.route("/Other_Company")
def Other_Company():
    return "<h1> Company Name: Other Company Selected</h1>"

@app.route('/welcome/<name>')
def welcome(name):
    if (name=="ABC Corp"):
        return redirect(url_for('ABC_Corp'))
    else:
        return redirect(url_for('Other_Company'))


if __name__=="__main__":
    app.run(host="0.0.0.0")
