'''
DISCO:
* Our program does not work for unanticipated reasons
* We host the app locally
QCC:
0. Java init functions are similar, the __[]__ usually symbolizes something default
1. It means root directory often
2. To the app root directory, since we routed everything there
3. No hablo queso!
4. Probably on the website, since we routed the app there
5. We've seen similar stuff in Flutter and React/JS
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 * 
'''
from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?
