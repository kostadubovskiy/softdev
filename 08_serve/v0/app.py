# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # creates instance of class Flask

@app.route("/") # routes to root directory
def hello_world():
    print(__name__) # prints to console
    return "No hablo queso!"  # prints to created server

app.run()  # creates web server
