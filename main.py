from flask import Flask
from config import Config

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.PORT)