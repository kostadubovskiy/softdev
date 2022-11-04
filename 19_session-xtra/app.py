from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request, session, redirect, url_for

app = Flask(__name__)    #create Flask object

app.secret_key = 'hi'


@app.route("/")
def foo():
    if "username" in session:
        return f"logged in as {session['usernames']}"
    return "youre not logged in bud"


@app.route("/login", methods=["GET", "POST"])
def foo2():
    if request.method == "POST":
        print("hello")
        session['username'] = request.form['username']
        return redirect(url_for('foo'))
    return render_template('login.html')

    usernames=['yee', 'ah']
    passwords=['goofy', 'ah']
    usr_in=request.form['username']
    pwd_in=request.form['pwd']
    print(pwd_in)
    print(usr_in)
    # print(passwords[usernames.index(usr_in)])
    response_var = ""
    if usr_in in usernames and pwd_in == passwords[usernames.index(usr_in)]:
        login=True
        return render_template('response.html',v1="Kosta is a *****")
    else:
        return render_template('login.html',fail_login='password or username is wrong, please try again')
    
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()