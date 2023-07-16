# Question 1 - 
# Answer 1 - Flask is a microframework for developers, designed to enable them to create and scale web apps quickly and simply
# Flask is a small and lightweight Python web framework that provides useful tools and features that make creating 
# web applications in Python easier. It gives developers flexibility and is a more accessible framework 
# for new developers since you can build a web application quickly using only a single Python file.

# Advantages of Flask Framework
# 1. Lightweight: Flask is a lightweight framework because it is independent of external libraries and it gives a
#    quick start for web development having complex applications.
# 2. Compatible: Flask is compatible with the latest technologies such as machine learning, agile development, 
#    cloud technologies, etc.
# 3. Independent: Flask allows full control to the developers for creating web applications.
#    A developer can do the experiment with the libraries and architecture of the framework.
# 4. Integrated Unit Testing: Flask offers an integrated unit testing feature that helps in faster debugging, 
#    robust development, and independence to do experiments.
# 5. Flexible and Scalable: Flask supports WSGI templates that help in flexibility and scalability in the 
#    web development process.
# 6. Secure Cookies: Secure cookie is an attribute of an HTTP request that enables the security of channels 
#    and ensures no unauthorized person has access to the text. Flask supports the feature of secure cookies. 

# Question 2-
# Answer 2 - 
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")

# Question 3

# Answer 3 - App routing in Flask
# App routing is the technique used to map the specific URL with the associated function intended to perform some task.
# use of app routesis that the latest Web frameworks use the routing technique to help users remember application URLs.
# It is helpful to access the desired page directly without navigating from the home page.