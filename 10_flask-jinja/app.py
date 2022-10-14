'''
TEAM KrEWes: Elizabeth Paperno, Raven (Ruiwen) Tang, William Vongphanith, Kosta Dubovskiy
SoftDev
K10 -- Using Flask with Templates
2022-10-13
Time Spent: 0.5 hours

DISCO
___________
- When you open the html file directly it prints what is in the body (the templating things).
- When you run it with Flask it populates the template.
-

QCC
___________
- Why do you have to explicity pass through values in the render_template function?
- Can we refer to a variable twice in a template? 

'''
from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best.

if __name__ == "__main__":
    app.debug = True
    app.run()
