from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request  
from flask import session


app = Flask(__name__)    #create Flask object

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# from flask import Flask             #facilitate flask webserving
# from flask import render_template   #facilitate jinja templating
# from flask import request           #facilitate form submission

# #the conventional way:
# #from flask import Flask, render_template, request

# app = Flask(__name__)    #create Flask object


# @app.route("/", methods=["GET","POST"])
# def foo():
#     return render_template('login.html')


# @app.route("/response", methods=["GET","POST"])
# def foo2():
#     usernames=['yee', 'ah']
#     passwords=['goofy', 'ah']
#     usr_in=request.args['username']
#     pwd_in=request.args['password']
#     print(pwd_in)
#     print(usr_in)
#     print(passwords[usernames.index(usr_in)])
#     if pwd_in == passwords[usernames.index(usr_in)]:
#         return render_template('response.html')
#     else:
#         return None
    
    
# if __name__ == "__main__": #false if this file imported as module
#     #enable debugging, auto-restarting of server when this file is modified
#     app.debug = True 
#     app.run()