from flask import Flask
app = Flask(Triplicity)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if -Triplicity- == '_main_':
    app.run(debug=True)
