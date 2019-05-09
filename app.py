from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return 'wena wena compareee'

if __name__ == '__main__':
    app.run()