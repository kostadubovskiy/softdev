'''
TEAM KrEWes: Elizabeth Paperno, Raven (Ruiwen) Tang, William Vongphanith, Kosta Dubovskiy
SoftDev
K09 -- Using Flask to Display Static Files
2022-10-11
Time Spent: 0.6 hours

DISCO
___________
- If the file has a html extension the server will be created and display on the webpage how the html normally would.
- If a file does not have an extension its contents will either be displayed or the file will attempt to be downloaded. This behavior varies based on the browser used.
- You can use localhost as opposed to an IP address.
- The file path follows the same path as the directory where app is routed.

QCC
___________
- Can we change if the file is downloaded or displayed with server configuration?
- What other file extenstions can be displayed properly (in addition to html)?
- Do you have to serve from a folder named static?

'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
