'''
TEAM KrEWes: Elizabeth Paperno, Raven (Ruiwen) Tang, William Vongphanith, Kosta>
SoftDev
K11 -- Forms
2022-10-14
Time Spent: 0.75 hours

DISCO
__________
- In the 'dictionary'-like object that contains the tuples of input form names and values, the key-value pairs are generated as they are passed in, not a priori
- methods parameter can specifiy what type of requests we make from the flask app, by default it's both GET and POST

QCC
___________
- What's the difference between GET and POST requests?
- How do we get a POST request to work?

'''


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage(): # only called on disp. page
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***") 
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***") # these don't work here because there hasn't been any inputs yet, the tuple pairs are created as input is passed in, they're chronologicallyt created 
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth") # /auth is referenced in form action in the html #, methods=['GET', 'POST']) # By default the user can both post and request info but passing the methods parameter specifies which operations can be done
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***") # meta info about the requests/inputs
    print(request)
    print("***DIAG: request.args ***")
    print(request.args) # array of the specific requests/inputs in the vanilla html, comes as array of tuple pairs: ([HTML NAME], [INPUT VAL])
    print("***DIAG: request.args['username']  ***")
    print(request.args['username']) # access specific value in request.args array
    print("***DIAG: request.headers ***")
    print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
