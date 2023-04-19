from flask import Flask

app = Flask(__name__)

@app.route('/api/p/hello-flask')
def hello():
    return 'FLASK - hello flask direct route'