# Question 4

# Answer 4 -
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def standard_msg():
    return "<h1> Company Name: ABC Corporation </h1><wbr> <h2> Location: India </h2> <wbr><h3> Contact Detail: 999-999-9999 </h3> "

@app.route("/welcome")
def welcome():
    return "<h1> Welcome to ABC Corporation </h1>"


if __name__=="__main__":
    app.run(host="0.0.0.0")
